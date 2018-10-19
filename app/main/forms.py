from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired,InputRequired,Email,Length, Regexp



class SignUp(FlaskForm):
    
    #Name
    first_name=StringField('What is your name?',validators=[DataRequired()])
    father_name=StringField('father name?',validators=[DataRequired()])
    family=StringField('family name?',validators=[DataRequired()])
    
    #ID Number
    id=StringField('id',
        render_kw={"pattern": "^\d{9}$",
        "type":"tel"},
        validators=[InputRequired(),
        
        Regexp("^\d{9}$",message='ID is wrong')])

    #Mobile Number  
    mobile=StringField('Mobile',
        render_kw= {
            "pattern":"^\+?\d{10,14}$",
            "type":"tel"},
        validators=[InputRequired(), 
        Regexp("^\+?\d{10,14}$",message='number is wrong')])

    #Email
    email=StringField('Email',
        render_kw= {
            "type":"email"},
        validators=[DataRequired(),
        Email(message=u'That\'s not a valid email address.')])

    #home_adress
    home_city = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])
    home_town = SelectField(u'Programming Language', 
        choices=[('','Village'),('del','del')],
        validators = [DataRequired()])

    #work_adress
    work_city = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])
    work_town = SelectField(u'Programming Language',
        choices=[('','town'), ('del','del')],
        validators = [DataRequired()])
    #car_taxi_private
    car_type = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])

    #car_year
    car_year = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])

    #car_company #car_model
    car_company = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])

    
    car_model = SelectField(u'Programming Language',
        choices=[('','carModeel'), ('del','del')],
        validators = [DataRequired()])
    #car_color
    car_color = SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])

    #car_condition
    car_condition =  SelectField(u'Programming Language', 
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')],
        validators = [DataRequired()])
    #SUBMIT
    submit = SubmitField('Submit')

    