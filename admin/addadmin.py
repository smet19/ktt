from flask import Blueprint,request,render_template
from flask_login import login_required,current_user
from admin.newAdmin import newAdmin

addadmin = Blueprint('addadmin', __name__, template_folder="templates")


@addadmin.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST' and current_user.ugroup == 'Admin':
        newAdmin(request.form["nickname"])
    return render_template('addadmin.html')