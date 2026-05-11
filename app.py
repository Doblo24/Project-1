from flask import Flask, render_template,request
from models.db import db

from routes.routes_patient import patient_bp

#THIS MUST BE REMOVED BY PERSON WORKING ON EMPLOYEE MODULE
from routes.routes_employee import employee_bp 

#THIS MUST BE REMOVED BY PERSON WORKING ON MEDICINE MODULE
from routes.routes_medicine import medicine_bp

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(patient_bp)

app.register_blueprint(employee_bp) 
app.register_blueprint(medicine_bp) 


@app.route('/')
def base():
    return render_template("base.html")


if __name__==('__main__'):
    app.run(debug=True)