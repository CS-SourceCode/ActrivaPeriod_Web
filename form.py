from flask.ext.wtf import Form
from wtform import StringField, BooleanField
from wtforms.validators import DataRequired

Class FirePut(Form):
    title = StringField('title', validators=[Datarequired()])
    year = StringField('year', validators=[Datarequired()])
    rating = StringField('rating', validators=[Datarequired()])
