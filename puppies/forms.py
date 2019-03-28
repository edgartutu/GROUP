# forms in puppies

from flask_wtf import FlaskForm

from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
	name = StringField('Name of puppy :')
	submit = SubmitField('submit')

class DelForm(FlaskForm):
	
	id = IntegerField('Id number to remove')

	submit =  SubmitField('submit')
