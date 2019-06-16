from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_required,current_user

addquestion = Blueprint('addquestion', __name__, template_folder="templates")

@addquestion.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST' :
        if request.form['amount']!= '':
            return render_template('addquestion.html',info = [request.form['testname'],request.form['amount']])
    return redirect(url_for('test_changing.index'))