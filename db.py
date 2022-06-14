import sqlite3

# Creating table data


def studentData():
    con = sqlite3.connect('digikids.db')
    cur = con.cursor()
    cur.execute(
        """"CREATE TABLE IF NOT EXISTS digikids(id INTEGER PRIMARY KEY, 
        Admission integer, 
        fullname text, 
        dOB text, 
        age integer, 
        gender text,
        parentsContact text, 
        course text)""")
    con.commit()
    con.close()


def addStudent(Admission, fullname, dOB, age, gender, parentsContact, course):
    con = sqlite3.connect('digikids.db')
    cur = con.cursor()
    cur.execute("INSERT INTO digikids VALUES (NULL, ?,?,?,?,?,?,?)",
                (Admission, fullname, dOB, age, gender, parentsContact, course))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect('digikids.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM digikids")
    row = cur.fetchall()
    con.close()
    return rows


def searchData(Admission="", fullname="", dOB="", age="", gender="", parentsContact="", course=""):
    con = sqlite3.connect('digikids.db')
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM digikids WHERE Admission=? OR fullname=? OR dOB=? OR age=? OR gender=? OR parentsContact=? OR course=? ",
        (Admission, fullname, dOB, age, gender, parentsContact, course))
    rows = cur.fetchall()
    con.close()
    return rows


def updateData(id, Admission="", fullname="", dOB="", age="", gender="", parentsContact="", course=""):
    con = sqlite3.connect('digikids.db')
    cur = con.cursor()
    cur.execute(
        "UPDATE digikids SET Admission=? OR fullname=? OR dOB=? OR age=? OR gender=? OR parentsContact=? OR course=?",
        (Admission, fullname, dOB, age, gender, parentsContact, course, id))
    con.commit()
    con.close()

studentData()
# Add Password feature
