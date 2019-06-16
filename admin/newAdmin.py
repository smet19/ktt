import sqlite3
def newAdmin(nickname):
    conn = sqlite3.connect('logindatabase.db')
    cur = conn.cursor()
    csql = 'UPDATE user SET ugroup=? WHERE username=?'
    cur.execute(csql,["Admin",str(nickname)])
    conn.commit()