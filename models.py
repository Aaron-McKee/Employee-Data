from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

#Models Go Below 

class Department(db.Model):
    """Department Model"""
    __tablename__="departments"

    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)

    employees = db.relationship('Employee')

    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name} {self.phone}>"

class Employee(db.Model):
    """Employee Model"""
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=False, default='CA')
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))

    dept = db.relationship('Department')
    assignments = db.relationship('EmployeeProject', backref='employee')  #This does not work!
    
    projects = db.relationship('Project', secondary ='employee_projects', backref='employees')

    def __repr__(self):
        return f"<Employee {self.name} {self.state} {self.dept_code}>"
    
class Project(db.Model):
    __tablename__ = "projects"
    proj_code = db.Column(db.Text, primary_key=True)
    proj_name = db.Column(db.Text, nullable=False, unique=True)

    assignments = db.relationship('EmployeeProject', backref='project')  #This does not work!

    def __repr__(self):
        return f"<Project {self.proj_code} {self.proj_name}>"

class EmployeeProject(db.Model):
    __tablename__ = "employee_projects"
    emp_id = db.Column(db.Integer, db.ForeignKey("employees.id"), primary_key=True)
    proj_code = db.Column(db.Text, db.ForeignKey("projects.proj_code"), primary_key=True)
    role = db.Column(db.Text)

#Below is inefficient, as it makes a query for each department. 

def get_directory():
    all_emps = Employee.query.all()

    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else: 
            print(emp.name)
            
def get_directory_join():
    directory = db.session.query(Employee.name, Department.dept_name, Department.phone).join(Department).all()
    for name, dept, phone in directory:
        print(name, dept, phone)    
    