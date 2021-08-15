import sys

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import core_admission

CHUNK_SIZE = 4000
DB_URL = "postgresql://postgres:1030@localhost/mimic"

engine = create_engine(DB_URL)
session = sessionmaker(bind = engine)()

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
                    [ core_admission(**d.to_dict()) for r, d in chunk.iterrows() ]
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

    return num_inserted

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You have provided an empty data path")
        sys.exit(1)
    else:
        input_file_path = sys.argv[1]
    
    try:
        df = pd.read_csv(
            input_file_path,
            compression = 'gzip',
        )
        assert(
            len(df) == len(core_admission.__table__.columns.keys())
        )
    except Exception as e:
        print(e)
        sys.exit("reading failes")
    # print(df.head(10))
    # print(df.shape)
    # print(list(df.columns.values))
    # print(dict(df.dtypes))

    num_inserted = batch_insert(df, CHUNK_SIZE, session)
    assert(
        num_inserted == len(df)
    )