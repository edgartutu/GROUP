

from flask import Blueprint,render_template,redirect,url_for

from myprojects import db
from myprojects.models import Owner
from myprojects.owners.forms import AddOwner

owners_blueprints=Blueprint('owners',__name__,template_folder='templates/owners')

@owners_blueprints.route('/addowner',methods=['GET','POST'])		
def addowner():
	
	form=AddOwner()

	if form.validate_on_submit():

		name=form.name.data

		pup_id=form.pup_id.data

		addown=Owner(name,pup_id)

		db.session.add(addown)
		db.session.commit()

		return redirect(url_for('puppies.list'))


	return render_template('addowner.html',form=form)