from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    surname = StringField('Pavarde', [DataRequired()])
    message = TextAreaField('Jūsų pranešimas', [DataRequired(), 
                                        Length(min=10, 
                                        message=('Per trumpas tekstas.'))])
    submit = SubmitField('Submit')