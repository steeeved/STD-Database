import sqlite3

# create table
def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, 
    	Admission integer, 
        fullname text, 
        DoB text, 
        Age text, 
        Gender text, 
        Parents_Contact text, 
        Class text
        )""")
    con.commit()
    con.close()


def addStudentRecord(Admission, fullname, DoB, Age, Gender, Parents_Contact, Class):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?)",
                (Admission,
                 fullname,
                 DoB,
                 Age,
                 Gender,
                 Parents_Contact,
                 Class))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close
    return rows


def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close


def searchData(Admission="",
               fullname="",
               DoB="",
               Age="",
               Gender="",
               Parents_Contact="",
               Class=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE Admission=? OR fullname=? OR  DoB=? OR Age=? OR Gender=? OR Parents_Contact=? OR \
            Class=? ",
                (Admission,
                 fullname,
                 DoB,
                 Age,
                 Gender,
                 Parents_Contact,
                 Class))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, Admission="",
               fullname="",
               DoB="",
               Age="",
               Gender="",
               Parents_Contact="",
               Class=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET Admission=?, fullname=?, DoB=?, Age=?, Gender=?, Parents_Contact=?, Class=?, WHERE id=?",
                (Admission,
                 fullname,
                 DoB,
                 Age,
                 Gender,
                 Parents_Contact,
                 Class, id))
    con.commit()
    con.close()


studentData()
