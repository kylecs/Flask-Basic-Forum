from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from forum import app
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	email = db.Column(db.Text, unique=True)
	posts = db.relationship("Post", backref="user")
	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	def __init__(self, title, content, poster):
		self.title = title
		self.content = content
		self.user_id = poster.id
	def get_user():
		return db.query.filter(User.id == user_id).first()