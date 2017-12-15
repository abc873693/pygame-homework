from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

timeCount = 0
root = Tk()
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
print(timeCount)

#==================================METHODS============================================
def setTime(num):
    timeCount = num
    

def Database():
    global conn, cursor
    conn = sqlite3.connect('pythontut.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `rank` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, time INTEGER)")
    
def Create():
    if  NAME.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        Database()
        print(timeCount)
        cursor.execute("INSERT INTO `rank` (name, time) VALUES(?, ?)", (str(NAME.get()),timeCount))
        conn.commit()
        NAME.set("")
        TIME.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Created a data!", fg="green")

def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `rank` ORDER BY `time` DESC")
    fetch = cursor.fetchall()
    
    i = 0
    for data in fetch:
        print(data.count)
        i = i + 1
        tree.insert('', 'end', values=(i,data[1], data[2]))
    cursor.close()
    conn.close()
    txt_result.config(text="Successfully read the data from database", fg="black")
    
def Exit():
    result = tkMessageBox.askquestion('Python: Simple CRUD Applition', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABLES==========================================
NAME = StringVar()
TIME = StringVar()

#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Python: Simple CRUD Application")
txt_title.pack()
txt_firstname = Label(Forms, text="Name:", font=('arial', 16), bd=15)
txt_firstname.grid(row=0, stick="e")
txt_lastname = Label(Forms, text="Time:", font=('arial', 16), bd=15)
txt_lastname.grid(row=1, stick="e")
time = Label(Forms, textvariable=TIME, width=30)
time.grid(row=1, column=1)
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================ENTRY WIDGET=======================================
name = Entry(Forms, textvariable=NAME, width=30)
name.grid(row=0, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=Create)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=Read )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=Exit)
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("rank","name", "time"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('rank', text="rank", anchor=W)
tree.heading('name', text="name", anchor=W)
tree.heading('time', text="time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.pack()

def loop():
    root.mainloop()

#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()
    print(timeCount)
