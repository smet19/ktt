import os
import datetime

from flask import Flask, flash, request, redirect, url_for,Blueprint,render_template
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
from File_DB import file_to_db

UPLOAD_FOLDER = 'files/filespath'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

file_upload = Blueprint('file_upload', __name__, template_folder="templates")

@file_upload.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST' and current_user.ugroup == 'Superadmin':

        if 'file' not in request.files:
            flash('Нет файловой части')
            return redirect(request.url)
        file = request.files['file']
        file_name = request.form['filename']
        description = request.form['description']
        if file.filename == '':
            flash('Файл не выбран')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            file_to_db(filename,file_name,description,current_user.username,datetime.datetime.now())
    return render_template('file_upload.html')