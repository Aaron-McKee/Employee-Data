"""Seed file to make sample data for database"""

from models import Department, Employee, Project, EmployeeProject, db 
from app import app

#Create all tables
db.drop_all()
db.create_all()

#Seed Departments
d1 = Department(dept_code="mktg", dept_name="Marketing", phone="897-9999")
d2 = Department(dept_code="acct", dept_name="Accounting", phone="899-5429")
d3 = Department(dept_code="sales", dept_name="Sales", phone="423-6912")
d4 = Department(dept_code="it", dept_name="Information Technology", phone="898-4229")
d5 = Department(dept_code="r&d", dept_name="Research and Development", phone="905-7979")


#Seed Employees
river = Employee(name="River Bottom", state="NY", dept_code="mktg")
summer = Employee(name="Summer Winter", state="OR", dept_code="mktg")
joaquin = Employee(name="Joaquin Phoenix", state="CA", dept_code="acct")
aaron = Employee(name="Aaron McKee", state="KY", dept_code="it")
vincent = Employee(name="Vincent Ngondi", state="WA", dept_code="r&d")
maggie = Employee(name= "Maggie Orozco", state="CA", dept_code="sales")

#Add and Commit Departments and Employees
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)   #You can also do: db.session.add_all([d1, d2, d3, d4, d5])
db.session.add(d4)
db.session.add(d5)

db.session.commit()    #Must commit Departments and Employees separately

db.session.add(river)
db.session.add(joaquin)
db.session.add(summer)   #You can also do: db.session.add_all([river, joaquin, summer, aaron, vincent])
db.session.add(aaron)
db.session.add(vincent)


db.session.commit()     #Must commit Departments and Employees separately

#Seed for Projects
pw = Project(proj_code='website', proj_name='Make website for MHI',
             assignments=[EmployeeProject(emp_id=aaron.id, role='Internet'),
                          EmployeeProject(emp_id=vincent.id, role='Internet')])    
ps = Project(proj_code='server', proj_name='Deploy Server',
             assignments=[EmployeeProject(emp_id=summer.id, role='Auditor'),
                          EmployeeProject(emp_id=river.id, role='Auditor')])

db.session.add(pw)
db.session.add(ps)
db.session.commit()
         


#To execute this seed.py (Go to Python3 and type)  ~/EmployeeDB$ python3 seed.py