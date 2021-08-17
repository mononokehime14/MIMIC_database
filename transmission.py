import sys

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import core_admission
from model import core_patients
from model import core_transfers

CHUNK_SIZE = 5000
DB_URL = "postgresql://postgres:1030@localhost/mimic"

engine = create_engine(DB_URL)
session = sessionmaker(bind = engine)()

relation = core_transfers

def get_chunk(df, n):
    if n < 1:
        raise ValueError('Minimum chunk size is 1')

    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(df), n):
        yield df[i:i + n]

def batch_insert(df, chunk_size, session):
    ind =  0
    num_inserted = 0
    for chunk in get_chunk(df, chunk_size):
        try:
            session.bulk_save_objects(
                    [ relation(**d.to_dict()) for r, d in chunk.iterrows() ]
                )
            session.commit()
            num_inserted += len(chunk)
        except:
            session.rollback()
            print("We encouter unknown situation at chunk {} ({} - {})".format(ind, chunk_size*ind, (ind+1)*chunk_size-1))
            raise
        finally:
            session.close()

        ind += 1
    print("chunk:{} finished".format(ind))
    return num_inserted

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You have provided an empty data path")
        sys.exit(1)
    else:
        input_file_path = sys.argv[1]
    # if len(sys.argv) < 3:
    #     print("You need to specify relation's name")
    # else:
    #     relation_name = sys.argv[2]

    try:
        chunks_list = []
        for chunk in pd.read_csv(input_file_path, sep=',', chunksize = CHUNK_SIZE, low_memory=False):
            chunks_list.append(chunk)
            del chunk
        df = pd.concat(chunks_list)
        # assert(
        #     len(df.columns) == len(relation.__table__.columns.keys())
        # )
    except Exception as e:
        print(e)
        sys.exit("reading failes")
    print("reading over")

    # print(df.head(10))
    # print(df.shape)
    # print(list(df.columns.values))
    # print(dict(df.dtypes))
    # sys.exit("util here is ok")

    num_inserted = batch_insert(df, CHUNK_SIZE, session)
    assert(
        num_inserted == len(df)
    )