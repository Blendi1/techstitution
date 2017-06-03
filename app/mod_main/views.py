from flask import Blueprint, render_template, request, redirect, url_for

mod_main = Blueprint('main', __name__)

from werkzeug import secure_filename

from os.path import join, dirname, realpath, os


@mod_main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

    
@mod_main.route('/login', methods=['GET'])
def login():
	return render_template('login.html')
