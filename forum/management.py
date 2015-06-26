

from database import *

def add_subforum(title, description):
	sub = Subforum(title, description)
	db.session.add(sub)
	db.session.commit()
def init_site():
	add_subforum("Admin", "This is a test subforum")
	add_subforum("Other", "Discuss other things here")