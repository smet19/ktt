from flask import Blueprint,render_template
from flask_login import  login_required


test_changing = Blueprint('test_changing',__name__,template_folder='templates')

@test_changing.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("testchosing.html")