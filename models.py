# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association table for the many-to-many relationship between Doctors and Patients
doctor_patient_association = Table(
    'doctor_patient_association', Base.metadata,
    Column('doctor_id', Integer, ForeignKey('doctors.id')),
    Column('patient_id', Integer, ForeignKey('patients.id'))
)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_info = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    patients = relationship('Patient', secondary=doctor_patient_association, back_populates='doctors')

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_info = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    doctors = relationship('Doctor', secondary=doctor_patient_association, back_populates='patients')

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_info = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)

# Create an engine that stores data in the local directory's
# 'PD.db' file.
engine = create_engine('sqlite:///PD.db')

# Create all tables in the engine.
Base.metadata.create_all(engine)

if __name__ == '__main__':
    engine = create_engine('sqlite:///PD.db')
    Base.metadata.create_all(engine)