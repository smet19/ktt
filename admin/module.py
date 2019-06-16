from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from File_DB import checkgroup, creategroupdb, checktestlist, addtacttable,checktact,checkfulltact
import time
import ast

administration = Blueprint('administartion', __name__, template_folder="templates")
creategroup = Blueprint('creategroup', __name__, template_folder="templates")


@administration.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "POST" and request.form['test'] != '':
        testinf = ast.literal_eval(request.form["test"])
        status = checktact(testinf[0])[0][2]
        if status =='Active':
            addtacttable(testinf[0], testinf[1],'Stop')
        else:

            addtacttable(testinf[0], testinf[1],'Active')
        return render_template('admin.html', testlist=checktestlist(), grouplist=checkgroup(),status =checkfulltact())
    if current_user.ugroup == 'Admin' or current_user.ugroup == 'Superadmin':
        return render_template('admin.html', testlist=checktestlist(), grouplist=checkgroup(),status =checkfulltact())
    else:
        return 'You are not admin'


@creategroup.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "POST" and request.form['groupname'] != '':

        id = int(time.time())
        creategroupdb(id, str(request.form['groupname']))
        addtacttable(str(request.form['groupname']),id, 'Stop')
        return render_template('addgroup.html', info='Создана группа: ' + request.form['groupname'])
    if current_user.ugroup == 'Admin' or current_user.ugroup == 'Superadmin':
        return render_template('addgroup.html')
    else:
        return 'ОП, ВЫ НАШЛИ ПАСХАЛКУ ヾ(= ω´ =)'