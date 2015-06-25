from flask import *
from flask.ext.login import LoginManager, current_user, login_user, UserMixin, logout_user, login_required
from config import *
#from database import *

#CONFIG

#SETUP
app = Flask(__name__)
app.config.from_object(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


#DATABASE STUFF
@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)


#test
@app.route('/test')
def test():
	user = User.query.first()
	return str(user.posts[1].title)


#VIEWS

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/loginform')
def loginform():
	return render_template("login.html")


@login_required
@app.route('/addpost')
def addpost():
	return render_template("createpost.html")

#ACTIONS
@login_required
@app.route('/action_post', methods=['POST'])
def action_post():
	user = current_user
	title = request.form['title']
	content = request.form['content']
	#check for valid posting
	post = Post(title, content, user)
	user.posts.append(post)
	db.session.add(post)
	db.session.commit()
	return redirect(url_for("index"))


@app.route('/action_login', methods=['POST'])
def action_login():
	username = request.form['username']
	password = request.form['password']
	user = User.query.filter(User.username == username).first()
	if user and user.password == password:
		login_user(user)
	return redirect(url_for("index"))


@login_required
@app.route('/action_logout')
def action_logout():
	#todo
	logout_user()
	return redirect(url_for("index"))

@app.route('/action_createaccount', methods=['POST'])
def action_createaccount():
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']
	user = User(email, username, password)
	db.session.add(user)
	db.session.commit()
	login_user(user)
	return redirect(url_for("index"))


#RUN
if __name__ == "__main__":
	#db.create_all()
	port = int(os.environ.get("PORT", 33507))
	app.run(host='0.0.0.0', port=port)
#app.run(debug=True)