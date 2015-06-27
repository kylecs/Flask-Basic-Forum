from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

@app.route('/')
def index():
	return "hello world"

if __name__ == "__main__":
	app.run()
