from database import db, Subforum
from forum import init_site

db.create_all()
if not Subforum.query.all():
		init_site()