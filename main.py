
import tkinter.messagebox
from tkinter.ttk import *
from tkinter import *
import Database


root = Tk()
root.title("Student DataBase")
root.iconbitmap("images1.ico")
root.geometry("1350x750")
#functions
def iExit():
    iExit = tkinter.messagebox.askyesno("Student Database", "Confirm if you want to exit")
    if iExit > 0:
    	root.destroy()
    	return

def clearData():
    txtstdAdmission.delete(0,END)
    txtfullname.delete(0,END)
    txtAge.delete(0,END)
    txtDoB.delete(0,END)
    txtParents_Contact.delete(0,END)

def addData():
    if(len(txtstdAdmission.get())==0) or (len(txtfullname.get())==0) or (len(txtDoB.get())==0) or (len(txtAge.get())==0) or (len(txtParents_Contact.get())==0):
        messagebox.showinfo("Incomplete Data", "Please fill in all the fields")
    elif(len(txtstdAdmission.get())!=0):
        Database.addStudentRecord(txtstdAdmission.get(), txtfullname.get(), txtDoB.get(), txtAge.get(), comboGender.get(), txtParents_Contact.get(), \
                    comboclass.get())
        studentlist.delete(0, END)
        studentlist.insert(END, (txtstdAdmission.get(), txtfullname.get(), txtDoB.get(), txtAge.get(), comboGender.get(), txtParents_Contact.get(), \
                    comboclass.get()))

def DispalyData():
    studentlist.delete(0, END)
    for row in Database.viewData():
        studentlist.insert(END,row, str("")) 

def StudentRec(event):
    global sd
    searchStd = studentlist.curselection()[0]
    sd = studentlist.get(searchStd)

    txtstdAdmission.delete(0, END)
    txtstdAdmission.insert(END,sd[1])

    txtfullname.delete(0, END)
    txtfullname.insert(END,sd[2])

    txtAge.delete(0, END)
    txtAge.insert(END,sd[3])

    txtDoB.delete(0, END)
    txtDoB.insert(END,sd[4])

    comboGender.delete(0, END)
    comboGender.insert(END,sd[5])

    txtParents_Contact.delete(0, END)
    txtParents_Contact.insert(END,sd[6])
    
    comboclass.delete(0, END)
    comboclass.insert(END,sd[7])

def DeleteData():
    if(len(txtstdAdmission.get())!=0):
        Database.deleteRec(sd[0])
        clearData()
        DispalyData()

def searchData():
    studentlist.delete(0, END)
    for row in Database.searchData(txtstdAdmission.get(), txtfullname.get(), txtDoB.get(), txtAge.get(), comboGender.get(), txtParents_Contact.get(), comboclass.get()):
        studentlist.insert(END, row, str(""))

def updateData():
    if(len(txtstdAdmission.get())!=0):
        Database.deleteRec(sd[0])
    if(len(txtstdAdmission.get())!=0):
        Database.addStudentRecord(txtstdAdmission.get(), txtfullname.get(), txtDoB.get(), txtAge.get(), comboGender.get(), txtParents_Contact.get(), comboclass.get())
        studentlist.delete(0, END)
        studentlist.insert(END, (txtstdAdmission.get(), txtfullname.get(), txtDoB.get(), txtAge.get(), comboGender.get(), txtParents_Contact.get(), comboclass.get()))

# #frames
MainFrame = Frame(root,  bg="cadet blue")
MainFrame.grid()

TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="cadet blue", relief=RIDGE)
TitFrame.pack(side=TOP)

ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost white", relief=RIDGE)
ButtonFrame.pack(side=BOTTOM)

DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="Grey", relief=RIDGE)
DataFrame.pack(side=BOTTOM)

DataFrameLeft = LabelFrame(DataFrame,  width=1000, height=600, padx=20, bg="Grey", relief=RIDGE,
font=("aerial", 18,"bold"), text="Student Information:\n") 
DataFrameLeft.pack(side=LEFT)

DataFrameRight = LabelFrame(DataFrame, width=450, height=300, padx=31, pady=3,bg="Grey", relief=RIDGE,
font=("aerial", 18,"bold"), text="Veiw Info:\n")
DataFrameRight.pack(side=RIGHT)

#create a lable
l_1 = Label(TitFrame, text="Entry Form", font=('Coiny', 47), bg="cadet blue")
l_1.grid()


#Entry Widgets
lblstdAdmission = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Student Adm No:", padx=2, pady=2, bg="Grey")
lblstdAdmission.grid(row=0, column=0, sticky=W)
txtstdAdmission = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"),  width=39)
txtstdAdmission.grid(row=0, column=1, sticky=W)

lblfullname = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Full Name:",padx=2, pady=2, bg="Grey")
lblfullname.grid(row=1, column=0, sticky=W)
txtfullname = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"),  width=39)
txtfullname.grid(row=1, column=1, sticky=W)


lblDoB = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Date of Birth:",padx=2, pady=2, bg="Grey")
lblDoB.grid(row=2, column=0, sticky=W)
txtDoB = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"),width=39)
txtDoB.grid(row=2, column=1, sticky=W)

lblAge = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Age:",padx=2, pady=2, bg="Grey")
lblAge.grid(row=3, column=0, sticky=W)
txtAge = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), width=39)
txtAge.grid(row=3, column=1, sticky=W)

lblGender = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Gender:",padx=2, pady=2, bg="Grey")
lblGender.grid(row=4, column=0, sticky=W)
comboGender = Combobox(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), width=39)
comboGender["values"]=("Male", "Female")
comboGender.current(0)
comboGender.grid(row=4, column=1, sticky=W)

txtParents_Contact = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Parents Contact:",padx=2, pady=2, bg="Grey")
txtParents_Contact.grid(row=5, column=0, sticky=W)
txtParents_Contact = Entry(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"),  width=39)
txtParents_Contact.grid(row=5, column=1, sticky=W)

current_class = Label(DataFrameLeft, font=("aerial", 15 ,"bold"), text="Current Grade:",padx=2, pady=2, bg="Grey")
current_class.grid(row=6, column=0, sticky=W)
comboclass = Combobox(DataFrameLeft, font=("Comfortaa Light", 15 ,"bold"), width=39)
comboclass["values"]=("Grade 1", "Grade 2", "Grade 3","Grade 4","Grade 5","Grade 6", "Grade 7","Grade 8","PP1", "PP2")
comboclass.current(0)
comboclass.grid(row=6, column=1, sticky=W)

#LISTBOX and SCROLLBAR WIDGET
scrollbar = Scrollbar(DataFrameRight)
# scrollbar.grid(row=0, column=1, sticky="NS")

studentlist = Listbox(DataFrameRight, width=40, height=8, font=("Comfortaa Light", 15 ,"bold"),yscrollcommand=scrollbar.set) 
studentlist.bind("<<ListboxSelect>>", StudentRec)
studentlist.grid(row=0, column=0, padx=8)
scrollbar.config(command = studentlist.yview)

#BUTTON WIDGTES
btnAddData = Button(ButtonFrame, text="Add New", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=addData)
btnAddData.grid(row=0, column=0)

btnDisplayData = Button(ButtonFrame, text="Display", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=DispalyData)
btnDisplayData.grid(row=0, column=1)

btnClearData = Button(ButtonFrame, text="Clear", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=clearData)
btnClearData.grid(row=0, column=2)

btnDeleteData = Button(ButtonFrame, text="Delete", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=DeleteData)
btnDeleteData.grid(row=0, column=3)

btnSearchData = Button(ButtonFrame, text="Search", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=searchData)
btnSearchData.grid(row=0, column=4)

btnUpdateData = Button(ButtonFrame, text="Update", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=updateData)
btnUpdateData.grid(row=0, column=5)

btnExit = Button(ButtonFrame, text="Exit", font=("aerial", 20 ,"bold"), width=10, height=1, bd=4, command=iExit)
btnExit.grid(row=0, column=6)

root.mainloop()   
