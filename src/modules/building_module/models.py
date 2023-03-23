from flask_sqlalchemy import SQLAlchemy
import datetime
from src.database.db_instance import db

class BuildingModel(db.Model):
	__tablename__ = 'buildings'
 
	id = db.Column(db.Integer, primary_key=True)
	bid = db.Column(db.String(10), nullable=False, unique=True)
	name = db.Column(db.Text, nullable=False)
	desc = db.Column(db.Text, nullable=False)
	is_node = db.Column(db.Boolean, nullable=False, default=False)
	image = db.Column(db.String(255), nullable=True)
	lat = db.Column(db.Numeric(precision=18, scale=15), nullable=False)
	lng = db.Column(db.Numeric(precision=18, scale=15), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now())

	"""
	The __repr__() method in the BuildingModel class is a special method 
	in Python that returns a string representation of the object. 
	It is often used for debugging and logging purposes.

	In this case, the __repr__() method returns a string representation of a 
	BuildingModel object in the format <User {name}>. The curly braces {} 
	are used to indicate a placeholder for the value of the name attribute of the object.

	When you print a BuildingModel object or call repr() on it, the __repr__() 
	method is called to generate the string representation of the object. For example:

	building = BuildingModel(name='Building A', desc='A tall building', lat=37.7749, lng=-122.4194)
	print(building)  # Output: <User Building A>
	"""
 
	def __repr__(self):
		return '<BuildingModel {}>'.format(self.name)
	
	def to_dict(self):
		return {
			'id': self.id,
			'bid': self.bid,
			'name': self.name,
			'is_node':self.is_node,
			'desc': self.desc,
			'image': self.image,
			'lat': self.lat,
			'lng': self.lng,
		}

	"""
	The to_dict() function in the BuildingModel class is a method that returns a 
	dictionary representation of a BuildingModel object.

	This method converts the properties of the BuildingModel object into a dictionary with keys 
	corresponding to the property names and values corresponding to the property values. 
	The keys in the dictionary are: id, name, desc, lat, and lng.

	This method can be useful when you need to convert BuildingModel objects to dictionaries, 
	for example, when you want to return the object as JSON in a Flask API response. By using the to_dict() method,
	you can easily convert the BuildingModel object to a dictionary that can be serialized as JSON.

	Here's an example of how you can use the to_dict() method to convert a BuildingModel object to a dictionary

	############

	building = BuildingModel(name='Building A', desc='A tall building', lat=37.7749, lng=-122.4194)
	building_dict = building.to_dict()
	print(building_dict)
	# Output: {'id': None, 'name': 'Building A', 'desc': 'A tall building', 'lat': 37.7749, 'lng': -122.4194}

	#############

	"""



