from forum import app, db
#MANAGEMENT
def add_subforum(title, description, parent=None):
	sub = Subforum(title, description)
	if parent:
		parent.subforums.append(sub)
	else:
		db.session.add(sub)

	db.session.commit()
	return sub
def init_site():
	admin = add_subforum("Forum", "Announcements, bug reports, and general discussion about the forum belongs here")
	add_subforum("Announcements", "View forum announcements here",admin)
	add_subforum("Bug Reports", "Report bugs with the forum here", admin)
	add_subforum("General Discussion", "Use this subforum to post anything you want")
	add_subforum("Other", "Discuss other things here")