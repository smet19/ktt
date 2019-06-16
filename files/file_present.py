from flask import Flask, flash, request, redirect, url_for,Blueprint,render_template,send_file
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
from File_DB import allFilesCheck,deletefilewithID

file_download = Blueprint('file_download', __name__, template_folder="templates")
files = Blueprint('files', __name__, template_folder="templates")

@file_download.route('/', methods=['GET','POST'])
@login_required
def index():

    return send_file('files/'+str(request.args.get('filename')))

@files.route('/', methods=['GET','POST'])
@login_required
def index():
    if request.method == 'POST' and request.form['delete'] !='':
        print(request.form['delete'])
        deletefilewithID(request.form['delete'])
        return render_template('files.html', fileslist=allFilesCheck())
    return render_template('files.html', fileslist = allFilesCheck())