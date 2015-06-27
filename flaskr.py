# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash
<<<<<<< HEAD

# configuration
DATABASE = '/tmp/flaskr.db'
=======
from contextlib import closing
	
# configuration
DATABASE = 'flaskr.db'
>>>>>>> c8e6bfe5b6d0a9b8143398f17e83de75b6022d1c
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

<<<<<<< HEAD
# create our little application :)
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# db connect
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run(debug=True)
=======

# create our little application :)
app= Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTING', silent=True)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
	
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exeption):
	db = getarr(g, 'db', None)
	if db is not None:
		db.close()
	
if __name__ == '__main__':
	app.run()

