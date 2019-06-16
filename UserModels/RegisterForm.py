from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField
from wtforms.validators import InputRequired, Length
from File_DB import exportgroup4Choice



class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    firstname = StringField('Имя', validators=[InputRequired(), Length(min=2, max=80)])
    lastname = StringField('Фамилия', validators=[InputRequired(), Length(min=2, max=80)])
    ugroup = SelectField('Группа', choices= exportgroup4Choice())