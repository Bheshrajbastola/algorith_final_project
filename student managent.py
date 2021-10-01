from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox


#================================Main Window=================================#
db = Database("Student.db")
root = Tk()
root.title("Student  Management System")
root.iconbitmap('C:/Users/swika/Desktop/tution.ico')
root.geometry("4000x400")
root.config(bg="#2c3e50")
root.state("zoomed")

###################Variable###########################
name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()




#################### Main Body #######################

entries_frame = Frame(root, bg="green")
entries_frame.pack(side=TOP, fill=X)

title = Label(entries_frame, text="Student Management System", font=("Calibri", 20, "bold"), bg="green", fg="white")
title.grid(row=0,column=2, columnspan=5, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="green", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")

txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="green", fg="white")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")

txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="green", fg="white")
lbldob.grid(row=2, column=0, padx=10, pady=10, sticky="w")

txtDob = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
txtDob.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="green", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")

txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="green", fg="white")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")

comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="green", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")

txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="green", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")


############################## Fetching Data from data base######################
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]

    #print(row)

    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])


################ Function to display the recorded data #######################3w
def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


########################function to add student###################3333

def add_student():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" \
            or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDob.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()


####################Function to upadte the student data######################

def update_student():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDob.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


##########function for delete##############

def delete_student():
    db.remove(row[0])
    messagebox.showinfo("Success", "Record Deleted")
    clearAll()
    dispalyAll()

########################## Function To clear the screen ###############################

def clearAll():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="green")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

btnAdd = Button(btn_frame, command=add_student, text="Add Data", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)

btnEdit = Button(btn_frame, command=update_student, text="Update Data", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)

btnDelete = Button(btn_frame, command=delete_student, text="Delete Data", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)

btnClear = Button(btn_frame, command=clearAll, text="Clear Data", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)



##################################Table Frame#############################
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()

style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body

style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings

###############tree view is used to make the data come in order##################3

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

######################### End #########################
dispalyAll()
root.mainloop()