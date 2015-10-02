import os

SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SITE_NAME = "Default Forum Name"
SITE_DESCRIPTION = "Change this value in config.py"
#SQLALCHEMY_DATABASE_URI = "sqlite:///../data/database.db";

