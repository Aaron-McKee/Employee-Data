from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email

class AddSnackForm(FlaskForm):

    name = StringField("Snack Name", validators =[InputRequired("Snack name cant be blank")])
    email = StringField("Email", validators=[Email()])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")


class EmployeeForm(FlaskForm):

    name = StringField("Employee Name", validators=[InputRequired(message="Name cannot be blank")])
    state = StringField("State")
    dept_code = SelectField("Department Code", choices=[('mktg', 'Marketing'), ('acct', 'Accounting'), ('sales', 'Sales'),
                                                        ('it', 'Information Technology'), ('r&d', 'Research and Development'),
                                                         ('lg', 'Legal')])