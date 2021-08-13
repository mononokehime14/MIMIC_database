
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()

class core_admission(Base):
    __tablename__ = 'core_admission'
    ROW_ID = Column(Integer)
    SUBJECT_ID = Column(Integer)
    HADM_ID = Column(Integer)
    ADMITTIME = Column(String)
    DISCHTIME = Column(String)
    DEATHTIME = Column(String)
    ADMISSION_TYPE = Column(String)
    ADMISSION_LOCATION = Column(String)
    DISCHARGE_LOCATION = Column(String)
    INSURANCE = Column(String)
    LANGUAGE = Column(String)
    RELIGION = Column(String)
    MARITAL_STATUS = Column(String)
    ETHNICITY = Column(String)
    EDREGTIME = Column(String)
    EDOUTTIME = Column(String)
    DIAGNOSIS = Column(String)
    HOSPITAL_EXPIRE_FLAG = Column(Integer)
    HAS_CHARTEVENTS_DATA = Column(Integer)

    def __repr__(self):
        return "<core_admission(hadm_id='{}', admission_location='{}'>".format(self.HADM_ID, self.ADMISSION_LOCATION)

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d