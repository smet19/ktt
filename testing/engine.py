from flask import Blueprint, request, session, render_template
from flask_login import login_required, current_user
from testing.QUE import QUE
from datetime import datetime
from File_DB import checkfulltact,checktest
from ast import literal_eval
import time
testing = Blueprint('testing', __name__, template_folder='templates')

@testing.route('/', methods=['GET', 'POST'])
@login_required
def index():
    tcheck = checkfulltact()
    testcheck = checktest()
    for test in tcheck:
        if current_user.ugroup == test[0] and test[2]=='Active':
            for element in testcheck:
                if test[1]== element[0]:
                    que = QUE(literal_eval(element[2]))
                    if request.method == "POST" and que.check_result(request, session):
                            session['testResult'] += 1
                            session['index'] += 1
                    if que.check_finally(session):
                        f = open(
                        str('result:' + str(datetime.utcnow().strftime('%Y-%m-%d')) + '-' + str(current_user.ugroup) + '.txt'),
                        'a')
                        f.write(str(current_user.firstname) + ' ' +str(current_user.lastname) + ' '+ str(session['testResult'])+'\n')
                        return render_template('result.html', testRestult=que.get_result(session))
                    return render_template('testing.html', que=que, index=session['index'])
                return render_template('testerror.html', )
        return render_template('testerror.html', )
