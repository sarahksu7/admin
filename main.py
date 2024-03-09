# main.py
import streamlit as st
from database import get_db, init_db
from crud import (add_doctor, get_all_doctors, add_patient, add_admin, 
                  assign_patient_to_doctor, update_doctor, delete_doctor)
init_db()

# Streamlit code to create the frontend goes here

st.title('Healthcare Dashboard')

# Function to add a doctor
def add_doctor_form():
    with st.form('Add Doctor'):
        name = st.text_input('Name')
        contact_info = st.text_input('Contact Info')
        date_of_birth = st.date_input('Date of Birth')
        submit_button = st.form_submit_button('Add Doctor')
        
        if submit_button:
            with get_db() as db:
                doctor = add_doctor(db, name, contact_info, date_of_birth)
                if doctor:
                    st.success('Doctor added successfully!')
                else:
                    st.error('Failed to add doctor.')

# Function to add a patient
def add_patient_form():
    with st.form('Add Patient'):
        name = st.text_input('Patient Name')
        contact_info = st.text_input('Patient Contact Info')
        date_of_birth = st.date_input('Patient Date of Birth')
        submit_button = st.form_submit_button('Add Patient')
        
        if submit_button:
            with get_db() as db:
                patient = add_patient(db, name, contact_info, date_of_birth)
                if patient:
                    st.success('Patient added successfully!')
                else:
                    st.error('Failed to add patient.')

# Function to view doctors
def view_doctors():
    with st.expander("View Doctors"):
        with get_db() as db:
            doctors = get_all_doctors(db)
            for doctor in doctors:
                st.text(f"Name: {doctor.name}, Contact Info: {doctor.contact_info}, DOB: {doctor.date_of_birth}")

# Function to assign a patient to a doctor
def assign_patient():
    with st.form("Assign Patient to Doctor"):
        doctor_id = st.number_input("Doctor ID", step=1)
        patient_id = st.number_input("Patient ID", step=1)
        submit_button = st.form_submit_button("Assign Patient")
        
        if submit_button:
            with get_db() as db:
                success = assign_patient_to_doctor(db, patient_id, doctor_id)
                if success:
                    st.success(f"Patient with ID {patient_id} assigned to doctor with ID {doctor_id}.")
                else:
                    st.error('Failed to assign patient.')

# Layout to select different operations
operation = st.selectbox("Choose Operation", ["Add Doctor", "Add Patient", "View Doctors", "Assign Patient to Doctor"])

if operation == "Add Doctor":
    add_doctor_form()
elif operation == "Add Patient":
    add_patient_form()
elif operation == "View Doctors":
    view_doctors()
elif operation == "Assign Patient to Doctor":
    assign_patient()

# Note: The function `assign_patient_to_doctor` needs to be defined in your crud.py file.
# It should take a database session, a patient ID, and a doctor ID as arguments.

