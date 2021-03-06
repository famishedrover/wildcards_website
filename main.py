from flask import render_template , url_for , redirect , request, session , abort , flash , g , jsonify, Flask 
from sqlalchemy import exc
import json
# g in flask exists globally
from functools import wraps
from werkzeug.utils import secure_filename
from time import time
app = Flask(__name__)

# acts as a decorator which tells the application 
# which URL should call the associated function.

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/info')
def info():
	return "info"
# @app.route('/hello/<miss>')
# def hello_world(miss):
# 	return 'Hello World '+miss

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
# 	return 'Blog Number: '+str(postID)

# @app.route('/rev/<float:revNo>')
# def devision(revNo):
# 	return 'Revision Number %f'%revNo

# @app.route('/flask')
# def hello_flask():
#    return 'Hello Flask'

# # canonical URL by appending '/' at the end
# # therefore can be accessed by both /python and /python/
# @app.route('/python/')
# def hello_python():
#    return 'Hello Python'

# @app.route('/admin/')
# def hello_admin():
# 	return "'sup Admin !"

# @app.route('/guest/<guest>/')
# def hello_guest(guest):
# 	return 'Hi %s'%guest

# @app.route('/user/<name>/')
# def hello_user(name):
# 	if name =='admin':
# 		return redirect(url_for('hello_admin'))
# 	else :
# 		return redirect(url_for('hello_guest',guest=name))

# @app.route('/getjson')
# def getjson():
# 	return {{'key1':'one','key2':'two'}}



if __name__ == "__main__":
	# app.run(host = '0.0.0.0' , port=5000 , debug=True)
	app.run(host='0.0.0.0', port=80) 