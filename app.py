from flask import Flask, render_template, redirect, url_for, session,app,request
import flask_sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user
from UserModels.LoginForm import LoginForm
from UserModels.RegisterForm import RegisterForm
from flask_bootstrap import Bootstrap
import os
from testing.engine import testing
from testing.changing import test_changing
from admin.module import administration,creategroup
from datetime import timedelta
from admin.addadmin import addadmin
from testing.addquestion import addquestion
from testing.testsavebp import testsavebp
from files.file_present import file_download,files
from files.file_upload import file_upload
from user.module import profile

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logindatabase.db'
app.config['SECRET_KEY'] = os.urandom(24)
UPLOAD_FOLDER = '/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = flask_sqlalchemy.SQLAlchemy(app)

from UserModels import User

bootstrap = Bootstrap(app)

app.register_blueprint(administration, url_prefix='/admin')
app.register_blueprint(addadmin, url_prefix='/addadmin')
app.register_blueprint(profile, url_prefix='/profile')
app.register_blueprint(creategroup, url_prefix='/creategroup')
app.register_blueprint(testing, url_prefix='/testing')
app.register_blueprint(test_changing, url_prefix='/testchange')
app.register_blueprint(testsavebp, url_prefix='/testsavebp')
app.register_blueprint(addquestion, url_prefix='/testcreator')
app.register_blueprint(file_upload, url_prefix='/file_upload')
app.register_blueprint(file_download, url_prefix='/file_download')
app.register_blueprint(files, url_prefix='/files')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def make_session_permanent():
    session.permanent =True
    app.permanent_session_lifetime = timedelta(hours=24)


@login_manager.user_loader
def load_user(user_id):
    return User.User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def start():
    session['testResult'] = 0
    session['index'] = 0
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('start'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('start'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User.User(username=form.username.data,
                             password=hashed_password,
                             firstname=form.firstname.data,
                             lastname=form.lastname.data,
                             ugroup=form.ugroup.data
                             )
        db.session.add(new_user)
        db.session.commit()
        return render_template('succesregister.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()