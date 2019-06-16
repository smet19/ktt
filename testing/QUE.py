class QUE:
    def __init__(self, data):
        self.data = data

    def get_question_number(self, index):
        return self.data[index]['number']

    def get_question_name(self, index):
        return self.data[index]['question']

    def get_question_list(self, index):
        return self.data[index]['data']

    def check_result(self, r, session):
        if r.method == "POST":
            if int(r.form['answer']) == int(self.data[session['index']]['true_value']):
                return True

    def check_finally(self, session):
        if session['index'] == len(self.data):
            return True

    def get_result(self, session):
        return int((session['testResult'] / len(self.data) * 100))

    def len(self):
        return len(self.data)