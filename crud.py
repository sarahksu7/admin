# crud.py
from sqlalchemy.orm import Session
from models import Doctor, Patient, Admin

def add_doctor(db: Session, name: str, contact_info: str, date_of_birth):
    db_doctor = Doctor(name=name, contact_info=contact_info, date_of_birth=date_of_birth)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def add_patient(db: Session, name: str, contact_info: str, date_of_birth):
    db_patient = Patient(name=name, contact_info=contact_info, date_of_birth=date_of_birth)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def add_admin(db: Session, name: str, contact_info: str, date_of_birth):
    db_admin = Admin(name=name, contact_info=contact_info, date_of_birth=date_of_birth)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_all_doctors(db: Session):
    return db.query(Doctor).all()

def get_all_patients(db: Session):
    return db.query(Patient).all()

def update_doctor(db: Session, doctor_id: int, name: str = None, contact_info: str = None, date_of_birth = None):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        if name:
            db_doctor.name = name
        if contact_info:
            db_doctor.contact_info = contact_info
        if date_of_birth:
            db_doctor.date_of_birth = date_of_birth
        db.commit()
        return db_doctor
    return None

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
        return True
    return False

def assign_patient_to_doctor(db: Session, patient_id: int, doctor_id: int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if db_doctor and db_patient:
        db_doctor.patients.append(db_patient)
        db.commit()
        return True
    return False
