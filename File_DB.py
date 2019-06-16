import sqlite3
import time

def file_to_db(path,filename,description,current_user,datetime):
    conn = sqlite3.connect('filedatabase.sqlite')

    cur = conn.cursor()
    cur.execute("INSERT INTO filesdatabase (path,filename, description, username, datetime) VALUES (?,?,?,?,?); ",["filespath/"+path,filename,description,current_user,datetime])
    conn.commit()

def allFilesCheck():
    conn = sqlite3.connect('filedatabase.sqlite')
    cur = conn.cursor()
    csql = 'SELECT * FROM filesdatabase '
    cur.execute(csql)
    result = cur.fetchall()
    conn.close()
    return result

def deletefilewithID(filename):
    conn = sqlite3.connect('filedatabase.sqlite')
    cur = conn.cursor()
    cur.execute("DELETE FROM  filesdatabase WHERE filename =?; ", [filename])
    conn.commit()

def create_testlist():
    conn = sqlite3.connect('testing.sqlite')

    cur = conn.cursor()
    cur.execute("CREATE TABLE testlist(testid INT,testname TEXT,tdata TEXT)")
    conn.commit()

def createtacttable():
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    cur.execute("CREATE TABLE tact(groupname TEXT UNIQUE,testid INT,status TEXT)")
    conn.commit()

def creategrouplist():
    conn = sqlite3.connect('testing.sqlite')

    cur = conn.cursor()
    cur.execute("CREATE TABLE grouplist(id INT,groupname TEXT)")
    conn.commit()

def creategroupdb(id,groupname):
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO grouplist (id,groupname) VALUES (?,?); ", [id, groupname])
    conn.commit()

def createTest(id, testname, tdata):
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO testlist (testid,testname,tdata) VALUES (?,?,?); ", [id, testname, tdata])
    conn.commit()

def addtacttable(groupname,testid,status):
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO tact (groupname,testid,status) VALUES (?,?,?); ", [groupname, testid, status])
    conn.commit()

def checktact(groupname):
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    sql = "SELECT * FROM tact WHERE groupname LIKE ?"
    cur.execute(sql,[groupname])
    result = cur.fetchall()
    conn.close()
    return result

def checkfulltact():
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    csql = 'SELECT * FROM tact ORDER BY groupname ASC '
    cur.execute(csql)
    result = cur.fetchall()
    conn.close()
    return result

def checkgroup():
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    csql = 'SELECT * FROM grouplist ORDER BY groupname ASC'
    cur.execute(csql)
    result = cur.fetchall()
    conn.close()
    return result

def checktest():
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    csql = 'SELECT * FROM testlist'
    cur.execute(csql)
    result = cur.fetchall()
    conn.close()
    return result

def checktestlist():
    conn = sqlite3.connect('testing.sqlite')
    cur = conn.cursor()
    csql = 'SELECT * FROM testlist '
    cur.execute(csql)
    result = cur.fetchall()
    conn.close()
    return result

def exportgroup4Choice():
    listimp = checkgroup()
    listexp = []
    for element in listimp:
        etuple = (element[1],element[1])
        listexp.append(etuple)
    return listexp