from flask import Blueprint, render_template, request
from models.db import db
from models.models_patient import Patient
from services.services_patient import add_patient_service

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/add_patient', methods=["GET","POST"])
def add_patient():
    if(request.method=="POST"):
        data = {
            "name":    request.form["name"],
            "age":     request.form["age"],
            "phone":   request.form["phone"],
            "address": request.form["address"]
        }

        add_patient_service(data)
        return"Data Saved Successfully"
    
    return render_template("add_patient.html")

@patient_bp.route('/view_update_patient')
def view_update_patient():
    patients = Patient.query.all()
    return render_template("view_update_patient.html", patients=patients)

@patient_bp.route('/edit_patient/<int:id>', methods=["GET", "POST"])
def edit_patient(id):

    patient = Patient.query.get(id)

    if request.method == "POST":

        patient.name = request.form["name"]
        patient.age = request.form["age"]
        patient.phone = request.form["phone"]
        patient.address = request.form["address"]

        db.session.commit()

        return "UPDATED SUCCESSFULLY"

    return render_template("edit_patient.html", patient=patient)