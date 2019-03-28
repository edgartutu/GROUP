
#set up my db in __init__.py under my projects folder

from myprojects import db


################ CREAT MODELS ######################

class Puppy(db.Model):

	__tablename__='puppies'

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.Text)

	owner=db.relationship('Owner',backref='puppy',uselist=False)

	def __init__(self,name):
		self.name=name

	def __repr__(self):
		if self.owner:
			return 'the puppy is called {} and owner is {}'.format(self.name,self.owner.name)
		else:
			return 'the {} has no owner'.format(self.name)

class Owner(db.Model):

	__tablename__='owners'

	id = db.Column(db.Integer,primary_key=True)
	name=db.Column(db.Text)

	puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))

	def __init__(self,name,puppy_id):
		self.name=name
		self.puppy_id=puppy_id

	def __repr__(self):
		return 'owner name:{}'.format(self.name)
		
