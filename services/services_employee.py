from models.models_employee import Employee
from models.db import db

def add_employee_service(data):

    employee = Employee(
        name=data["name"],
        age=data["age"],
        phone=data["phone"],
        address=data["address"],
        department=data["department"] 
    )

    db.session.add(employee)
    db.session.commit()