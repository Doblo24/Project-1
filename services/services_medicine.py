from models.models_medicine import Medicine
from models.db import db

def add_medicine_service(data):

    medicine = Medicine(
        name=data["name"],
        quantity=data["quantity"],
        price=data["price"]
    )

    db.session.add(medicine)
    db.session.commit()