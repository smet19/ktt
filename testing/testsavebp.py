from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_required,current_user
from File_DB import createTest
import time
testsavebp = Blueprint('testsavebp', __name__, template_folder="templates")


@testsavebp.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST' :
        print(request.form['testname'])
        rangef = int(len(list(request.form))/6)
        reqdict = dict(request.form)
        reslist = []
        for index in range(0,rangef):
            resdict = {'number':str(index+1),
            'question':reqdict.get('q'+str(index)),
            'data':[reqdict.get('a1:'+str(index)),reqdict.get('a2:'+str(index)),reqdict.get('a3:'+str(index)),reqdict.get('a4:'+str(index))],
            'true_value':reqdict.get('at:'+str(index))}
            reslist.append(resdict)
        createTest(int(time.time()),str(request.form['testname']),str(reslist) )

    return redirect(url_for('administartion.index'))