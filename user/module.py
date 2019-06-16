from flask import Blueprint, request, render_template
from flask_login import login_required, current_user


profile = Blueprint('profile', __name__, template_folder="templates")



@profile.route('/', methods=['GET', 'POST'])
@login_required
def index():
  return render_template("account.html")