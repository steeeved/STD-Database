import tkinter.messagebox
from tkinter.ttk import *
from tkinter import *
import Database

root = Tk()
root.title('Digikids Student DataBase')
root.iconbitmap("digikids.ico")
root.geometry("1250x650")

# Using RGB colors
def rgb(rgb):
    return "#%02x%02x%02x" % rgb

# functions


def Exit():
    exit = tkinter.messagebox.askyesno(
        "Exit", "Confirm if you want to exit"
    )
    if exit > 0:
        root.destroy()
        return


def clearData():
    admissionNoEntry.delete(0, END)
    fullNameEntry.delete(0, END)
    birthDateEntry.delete(0, END)
    ageEntry.delete(0, END)
    parentsContactEntry.delete(0, END)
    studentList.delete(0, END)


def addData():
    if (len(admissionNoEntry.get()) == 0 or len(fullNameEntry.get()) == 0 or len(birthDateEntry.get()) == 0 or len(ageEntry.get()) == 0
            or len(parentsContactEntry.get()) == 0 or len(comboGender.get()) == 0 or len(comboCourse.get()) == 0):
        messagebox.showinfo("Incomplete Data", "Please fill all the fields")
    else:
        Database.addStudentRecord(
            admissionNoEntry.get(), fullNameEntry.get(), birthDateEntry.get(), ageEntry.get(), parentsContactEntry.get(), comboGender.get(), comboCourse.get())
    studentList.delete(0, END)
    studentList.insert(END, (admissionNoEntry.get(), fullNameEntry.get(), birthDateEntry.get(
    ), ageEntry.get(), parentsContactEntry.get(), comboGender.get(), comboCourse.get()))


def displayData():
    studentList.delete(0, END)
    for row in Database.viewData():
        studentList.insert(END, row, str(""))


def studentRec(event):
    global sd
    searchStd = studentList.curselection()[0]
    sd = studentList.get(searchStd)

    admissionNoEntry.delete(0, END)
    admissionNoEntry.insert(END, sd[1])

    fullNameEntry.delete(0, END)
    fullNameEntry.insert(END, sd[2])

    birthDateEntry.delete(0, END)
    birthDateEntry.insert(END, sd[3])

    ageEntry.delete(0, END)
    ageEntry.insert(END, sd[4])

    parentsContactEntry.delete(0, END)
    parentsContactEntry.insert(END, sd[5])

    comboGender.delete(0, END)
    comboGender.insert(END, sd[6])

    comboCourse.delete(0, END)
    comboCourse.insert(END, sd[7])


def deleteData():
    if (len(admissionNoEntry.get()) != 0):
        Database.deleteRec(sd[0])
        clearData()
        displayData()


def searchData():
    studentList.delete(0, END)
    for row in Database.searchData(admissionNoEntry.get(), fullNameEntry.get(), birthDateEntry.get(), ageEntry.get(), parentsContactEntry.get(), comboGender.get(), comboCourse.get()):
        studentList.insert(END, row, str(""))


def updateData():
    if (len(admissionNoEntry.get()) !=0):
        Database.deleteRec(sd[0])
        Database.addStudentRecord(admissionNoEntry.get(), fullNameEntry.get(), birthDateEntry.get(
        ), ageEntry.get(), parentsContactEntry.get(), comboGender.get(), comboCourse.get())
        studentList.delete(0, END)
        studentList.insert(END, (admissionNoEntry.get(), fullNameEntry.get(), birthDateEntry.get(
        ), ageEntry.get(), parentsContactEntry.get(), comboGender.get(), comboCourse.get()))


# frames
mainFrame = Frame(root,  bg=rgb((255, 0, 79)))
mainFrame.grid()

TitFrame = Frame(mainFrame, bd=2, padx=54, pady=8,
                 bg="cadet blue", relief=RIDGE)
TitFrame.pack(side=TOP)

buttonFrame = Frame(mainFrame, bd=2, width=1350, height=70,
                    padx=18, pady=10, bg="Red", relief=RIDGE)
buttonFrame.pack(side=BOTTOM)

dataFrame = Frame(mainFrame, bd=1, width=1300, height=400,
                  padx=20, pady=20, bg="Grey", relief=RIDGE)
dataFrame.pack(side=BOTTOM)

dataFrameLeft = LabelFrame(dataFrame,  width=1000, height=600, padx=20, bg="Grey", relief=RIDGE,
                           font=("aerial", 18, "bold"), text="Student Information:\n")
dataFrameLeft.pack(side=LEFT)

dataFrameRight = LabelFrame(dataFrame, width=450, height=300, padx=31, pady=3, bg="Grey", relief=RIDGE,
                            font=("aerial", 18, "bold"), text="View Info:\n")
dataFrameRight.pack(side=RIGHT)

# create a label
l_1 = Label(TitFrame, text="STUDENT DATABASE",
            font=('Coiny', 47), bg="cadet blue")
l_1.grid()


# Entry Widgets
admissionNo = Label(dataFrameLeft, font=(
    "aerial", 15, "bold"), text="Student Adm No:", padx=2, pady=2, bg="Grey")
admissionNo.grid(row=0, column=0, sticky=W)
admissionNoEntry = Entry(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"),  width=39)
admissionNoEntry.grid(row=0, column=1, sticky=W)

fullName = Label(dataFrameLeft, font=("aerial", 15, "bold"),
                 text="Full Name:", padx=2, pady=2, bg="Grey")
fullName.grid(row=1, column=0, sticky=W)
fullNameEntry = Entry(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"),  width=39)
fullNameEntry.grid(row=1, column=1, sticky=W)


birthDate = Label(dataFrameLeft, font=("aerial", 15, "bold"),
                  text="Date of Birth:", padx=2, pady=2, bg="Grey")
birthDate.grid(row=2, column=0, sticky=W)
birthDateEntry = Entry(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"), width=39)
birthDateEntry.grid(row=2, column=1, sticky=W)

age = Label(dataFrameLeft, font=("aerial", 15, "bold"),
            text="Age:", padx=2, pady=2, bg="Grey")
age.grid(row=3, column=0, sticky=W)
ageEntry = Entry(dataFrameLeft, font=("Comfortaa Light", 15, "bold"), width=39)
ageEntry.grid(row=3, column=1, sticky=W)

parentsContact = Label(dataFrameLeft, font=(
    "aerial", 15, "bold"), text="Parents Contact:", padx=2, pady=2, bg="Grey")
parentsContact.grid(row=4, column=0, sticky=W)
parentsContactEntry = Entry(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"),  width=39)
parentsContactEntry.grid(row=4, column=1, sticky=W)

Gender = Label(dataFrameLeft, font=("aerial", 15, "bold"),
               text="Gender:", padx=2, pady=2, bg="Grey")
Gender.grid(row=5, column=0, sticky=W)
comboGender = Combobox(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"), width=37)
comboGender["values"] = ("--choose--", "Male", "Female")
comboGender.current(0)
comboGender.grid(row=5, column=1, sticky=W)

course = Label(dataFrameLeft, font=(
    "aerial", 15, "bold"), text="Current Grade:", padx=2, pady=2, bg="Grey")
course.grid(row=6, column=0, sticky=W)
comboCourse = Combobox(dataFrameLeft, font=(
    "Comfortaa Light", 15, "bold"), width=37)
comboCourse["values"] = ("--choose--", "Roblox Game Development",
                         "Python", "Introduction to web development", "Scratch")
comboCourse.current(0)
comboCourse.grid(row=6, column=1, sticky=W)

# LISTBOX and SCROLLBAR WIDGET
scrollbar = Scrollbar(dataFrameRight)
# scrollbar.grid(row=0, column=1, sticky="NS")

studentList = Listbox(dataFrameRight, width=40, height=8, font=(
    "Comfortaa Light", 15, "bold"), yscrollcommand=scrollbar.set)
studentList.bind("<<ListboxSelect>>", studentRec)
studentList.grid(row=0, column=0, padx=8)
scrollbar.config(command=studentList.yview)

# BUTTON WIDGETS
AddData = Button(buttonFrame, text="Add New", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=addData)
AddData.grid(row=0, column=0)

DisplayData = Button(buttonFrame, text="Display", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=displayData)
DisplayData.grid(row=0, column=1)

ClearData = Button(buttonFrame, text="Clear", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=clearData)
ClearData.grid(row=0, column=2)

DeleteData = Button(buttonFrame, text="Delete", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=deleteData)
DeleteData.grid(row=0, column=3)

SearchData = Button(buttonFrame, text="Search", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=searchData)
SearchData.grid(row=0, column=4)

UpdateData = Button(buttonFrame, text="Update", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=updateData)
UpdateData.grid(row=0, column=5)

Exit = Button(buttonFrame, text="Exit", font=(
    "aerial", 20, "bold"), width=10, height=1, bd=4, command=Exit)
Exit.grid(row=0, column=6)


root.mainloop()
