from app import db

class User(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		username = db.Column(db.String(80), unique=True, nullable=False)
		password = db.Column(db.String(120), unique=False, nullable=False)
		trainer = db.Column(db.String(80), unique=False, nullable=False)
		
		def __init__(self, username, password, trainer):
				self.username = username
				self.password = password
				self.trainer = trainer

		def __repr__(self):
				return '<User %r>' % self.username
