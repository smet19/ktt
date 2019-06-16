from config import *
import tesdata
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logindatabase.db'

bootstrap = Bootstrap(app)
db = flask_sqlalchemy.SQLAlchemy(app)
app.config['SECRET_KEY'] = 'G01R1A8C9H4MK16RT68C6H37Y48A6N!'
from User import User
global index
global testResult
index = 0
testResult = 0
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

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
        new_user = User(username=form.username.data,
                        password=hashed_password,
                        firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        ugroup=form.ugroup.data
                        )
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form)


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    if request.method=="POST" and request.form['addtest']=='addtest':
        return render_template('addtest.html')
    if current_user.ugroup == 'Admin':
        return render_template('admin.html',testlist = tesdata.testlist)
    else:
        return 'You are not admin'

@app.route('/testing',methods=['GET', 'POST'])
@login_required
def testing():
    global index
    global testResult
    question = tesdata.question
    if request.method=="POST":
        if int(request.form['answer']) == int(question[index]['truevalue']):
            testResult += 1
        index += 1
    if request.method=="POST" and index == question.__len__():
        testResultExport = (int((testResult/question.__len__()*100)))
        print(testResultExport)
        testResult = 0
        index = 0
        return render_template('result.html', testRestult=testResultExport)
    return render_template('testing.html', question=question, index=index)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)