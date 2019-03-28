from flask_wtf import FlaskForm

from wtforms import StringField,IntegerField,SubmitField



class AddOwner(FlaskForm):

	name = StringField('Enter name of owner')


	pup_id=IntegerField('enter id:')

	
	submit = SubmitField('submit')
