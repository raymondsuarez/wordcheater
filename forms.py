from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ScrabbleForm(FlaskForm):
	letters = StringField('Letters', validators=[DataRequired(), Length(min=1, max=7)])
	filter = StringField('Filter', validators=[DataRequired()])
	submit = SubmitField("Submit")

class SpellBeeForm(FlaskForm):
	required = StringField('Required Letter', validators=[DataRequired(), Length(min=1, max=1)])
	other = StringField('Other Letters', validators=[DataRequired(), Length(min=1, max=7)])
	submit = SubmitField("Submit")

