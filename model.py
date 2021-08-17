
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float

Base = declarative_base()

class core_admission(Base):
    __tablename__ = 'core_admission'
    subject_id = Column(Integer, primary_key = True, index = True)
    hadm_id = Column(Integer)
    admittime = Column(DateTime(timezone=False), nullable = False)
    dischtime = Column(DateTime(timezone=False), nullable = False)
    deathtime = Column(String)
    admission_type = Column(String)
    admission_location = Column(String)
    discharge_location = Column(String)
    insurance = Column(String)
    language = Column(String)
    marital_status = Column(String)
    ethnicity = Column(String)
    edregtime = Column(String)
    edouttime = Column(String)
    hospital_expire_flag = Column(Integer)

    def __repr__(self):
        return "<core_admission(hadm_id='{}', subject_id='{}'>".format(self.hadm_id, self.subject_id)

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d

class core_patients(Base):
    __tablename__ = 'core_patients'
    subject_id = Column(Integer, primary_key = True)
    gender = Column(String)
    anchor_age = Column(Integer)
    anchor_year = Column(Integer)
    anchor_year_group = Column(String)
    dod = Column(String)

    def __repr__(self):
        return "<core_patients(subject_id='{}', gender='{}'>".format(self.subject_id, self.gender)

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d

class core_transfers(Base):
    __tablename__ = 'core_transfers'
    subject_id = Column(Integer)
    hadm_id = Column(String)
    transfer_id = Column(Integer, primary_key = True)
    eventtype = Column(String)
    careunit = Column(String)
    intime = Column(DateTime(timezone=False), nullable = False)
    outtime = Column(String)

    def __repr__(self):
        return "<core_patients(subject_id='{}', transfer_id='{}'>".format(self.subject_id, self.transfer_id)

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d

class icu_chartevents(Base):
    __tablename__ = 'icu_chartevents'
    subject_id = Column(Integer)
    hadm_id = Column(Integer)
    stay_id = Column(Integer)
    charttime = Column(String)
    storetime = Column(String)
    itemid = Column(Integer, primary_key = True)
    value = Column(Float) 
    valuenum = Column(Float)
    valueuom = Column(String) 
    warning = Column(Integer)

    def __repr__(self):
        return "<core_patients(subject_id='{}', charttime='{}'>".format(self.subject_id, self.charttime)

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d