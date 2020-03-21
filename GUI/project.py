# importing required packages
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import os
import shutil
from tkinter import messagebox


def update_password():
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT *, oid  FROM username")
    records = c.fetchall()

    for record in records:
        if record[1] == old_pass:
            id = record[2]

    conn.execute("""UPDATE username set password = :new_pass
     where oid = :oid""",
                 {
                     'new_pass':new_pass,
                     'oid':id
                 })

    conn.commit()
    conn.close()
    return


# function to change password [backend]
def cp_f():
    global new_pass
    global old_pass

    new_pass = field7.get()
    old_pass = field6.get()
    con_pass = field8.get()

    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    # updating user and password list
    user_login()

    # checking password and replacing it with new password
    if check(password_list, old_pass) & ~isBlank(new_pass) & (con_pass == new_pass):
        update_password()
        # clearing user and password list to avoid problems
        user_list.clear()
        password_list.clear()

        lb1 = Label(fr2, text="Password has been changed successfully", fg="green", font=("arial black", 30))
        lb1.place(x=100, y=100)
        lb1.configure(bg="white")

        b1 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
        b1.place(x=640, y=300)

    else:
        lb1 = Label(fr2, text="password in correct or new password is blank", fg="red", font=("arial black", 30))
        lb1.place(x=100, y=100)
        lb1.configure(bg="white")

        b2 = Button(fr2, text="Retry", font=("Arial ", 20), width=20, command=change_password)
        b2.place(x=640, y=300)

        b1 = Button(fr2, text="Home", font=("Arial ", 20), width=20, command=main_screen)
        b1.place(x=640, y=400)


# function to change password [GUI]
def change_password():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    global field6
    global field7
    global field8

    lb2 = Label(fr2, text="Change Password", fg="black", font=("arial black", 30))
    lb2.place(x=640, y=20)
    lb2.configure(bg="white")

    lb4 = Label(fr2, text="Current Password:", fg="black", font=("arial", 15))
    lb4.place(x=60, y=200)
    lb4.configure(bg="white")

    field6 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field6.place(x=250, y=200)

    lb5 = Label(fr2, text="New Password:", fg="black", font=("arial", 15))
    lb5.place(x=60, y=250)
    lb5.configure(bg="white")

    field7 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field7.place(x=250, y=250)

    lb6 = Label(fr2, text="Confirm Password:", fg="black", font=("arial", 15))
    lb6.place(x=60, y=300)
    lb6.configure(bg="white")

    field8 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field8.place(x=250, y=300)

    b3 = Button(fr2, text="Submit", font=("Arial ", 10), relief='solid', width=26, command=cp_f)
    b3.place(x=640, y=400)

    b4 = Button(fr2, text="back", font=("Arial ", 10), relief='solid', width=26, command=main_screen)
    b4.place(x=640, y=700)


# function to upload an image
def upload_i():
    root = Tk()

    root.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                         filetypes=[("png files", "*.png"),("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("all files", "*.*")])
    if root.filename:
        shutil.copy(root.filename, 'C:/xampp/htdocs/Project/Assets/images')
        head, tail = os.path.split(root.filename)
        upload_t('image_name', tail)

    root.destroy()


# function to upload a video
def upload_v():
    root = Tk()

    root.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                         filetypes=[("mp4 files", "*.mp4"), ("all files", "*.*")])
    if root.filename:
        shutil.copy(root.filename, 'C:/xampp/htdocs/Project/Assets/videos')
        head, tail = os.path.split(root.filename)
        upload_t('video_name', tail)
        """video_address.append(root.filename)
        video_flag.append('True')
        print('lalalal')"""

    root.destroy()


# function to upload a pdf
def upload_pdf():
    root = Tk()

    root.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                         filetypes=[("pdf files", "*.pdf"), ("all files", "*.*")])
    if root.filename:
        shutil.copy(root.filename, 'C:/xampp/htdocs/Project/Assets/pdf')
        head, tail = os.path.split(root.filename)
        upload_t('pdf_name', tail)

    root.destroy()


# function to upload data to database
def upload_t(column_name, data):
    empty = ''
    conn = sqlite3.connect(path)
    c = conn.cursor()
    if column_name == 'video_name':
        c.execute("INSERT INTO notification VALUES (:circular, :image_name, :video_name, :pdf_name)",
                  {
                      'circular': empty,
                      'image_name': empty,
                      'video_name': data,
                      'pdf_name': empty
                  })
    elif column_name == 'image_name':
        c.execute("INSERT INTO notification VALUES (:circular, :image_name, :video_name, :pdf_name)",
                  {
                      'circular': empty,
                      'image_name': data,
                      'video_name': empty,
                      'pdf_name': empty
                  })
    elif column_name == 'circular':
        c.execute("INSERT INTO notification VALUES (:circular, :image_name, :video_name, :pdf_name)",
                  {
                      'circular': data,
                      'image_name': empty,
                      'video_name': empty,
                      'pdf_name': empty
                  })
    else:
        c.execute("INSERT INTO notification VALUES (:circular, :image_name, :video_name, :pdf_name)",
                  {
                      'circular': empty,
                      'image_name': empty,
                      'video_name': empty,
                      'pdf_name': data
                  })

    conn.commit()
    conn.close()


# function to upload a text
def upload_text():
    circular = field5.get("1.0", END)
    field5.delete("1.0", END)
    file1 = open(r"C:/xampp/htdocs/Project/Assets/circular.txt", "r+")
    file1.truncate(0)
    file1.write(circular)
    file1.close()


# function to print error to screen
def error(string):
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb3 = Label(fr2, text=string, fg="Red", font=("arial black", 30))
    lb3.place(x=600, y=20)
    lb3.configure(bg="white")

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=40, y=350)


# function find a blank string
def isBlank (myString):
    return not (myString and myString.strip())


# function to main screen after login
def main_screen():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    b3 = Button(fr2, text="Upload image", font=("Arial ", 20), width=20, command=upload_i)
    b3.place(x=40, y=250)

    b4 = Button(fr2, text="Upload video", font=("Arial ", 20), width=20, command=upload_v)
    b4.place(x=40, y=350)

    b7 = Button(fr2, text="Upload PDF", font=("Arial ", 20), width=20, command=upload_pdf)
    b7.place(x=400, y=250)

    global field5

    lb3 = Label(fr2, text="Text Circular", fg="black", font=("Times New Roman", 25))
    lb3.place(x=60, y=425)
    lb3.configure(bg="white")

    field5 = Text(fr2)
    field5.place(x=40, y=500, height=150, width =600)

    b5 = Button(fr2, text="submit", font=("Arial ", 20), width=20, command=upload_text)
    b5.place(x=40, y=700)

    b2 = Button(fr2, text="logout", fg='white', font=("Arial ", 20), width=20, command=home)
    b2.place(x=1040, y=750)
    b2.configure(bg="green")

    b6 = Button(fr2, text="Change Password", fg='white', font=("Arial ", 20), width=20, command=change_password)
    b6.place(x=40, y=760)
    b6.configure(bg="green")


# function to check username and password
def check(list, key):
    if key in list:
        return True
    else:
        return False


# function to add user to database
def user_register():
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("INSERT INTO username VALUES (:name, :password)",
                 {
                  'name': Name,
                     'password':password
                 })
    conn.commit()
    conn.close()


# function to get the users from database
def user_login():
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT *, oid  FROM username")
    records = c.fetchall()

    for record in records:
        user_list.append(record[0])
        password_list.append(record[1])

    conn.commit()
    conn.close()


# function to login to main screen[backend]
def Login_f():
    Login_Name = field4.get()
    Login_password = field5.get()

    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)
    user_login()

    if check(user_list, Login_Name) & check(password_list, Login_password):
        user_list.clear()
        password_list.clear()
        main_screen()

    else:
        lb3 = Label(fr2, text="Unauthorized User", fg="red", font=("arial black", 30))
        lb3.place(x=600, y=20)
        lb3.configure(bg="white")

        b2 = Button(fr2, text="home", fg='white', font=("Arial ", 20), width=20, command=home)
        b2.place(x=640, y=600)
        b2.configure(bg="green")


# function to check required details of user before adding it to database
def signup_f():
    global Name
    global password

    Name = field1.get()
    password = field2.get()
    confirm_password = field3.get()

    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    if password != confirm_password:
        lb3 = Label(fr2, text="User Registration failed", fg="red", font=("arial black", 30))
        lb3.place(x=600, y=20)
        lb3.configure(bg="white")

        lb4 = Label(fr2, text="Password doesn't match", fg="black", font=("arial black", 30))
        lb4.place(x=600, y=100)
        lb4.configure(bg="white")

        lb5 = Label(fr2, text="Please try again", fg="black", font=("arial black", 30))
        lb5.place(x=600, y=180)
        lb5.configure(bg="white")

        b1 = Button(fr2, text="Retry", font=("Arial ", 20), width=20, command=signup)
        b1.place(x=640, y=300)

    elif isBlank(Name) | isBlank(password):

        lb3 = Label(fr2, text="User Registration failed", fg="red", font=("arial black", 30))
        lb3.place(x=600, y=20)
        lb3.configure(bg="white")

        lb4 = Label(fr2, text="No field should be empty", fg="black", font=("arial black", 30))
        lb4.place(x=600, y=100)
        lb4.configure(bg="white")

        lb5 = Label(fr2, text="Please try again", fg="black", font=("arial black", 30))
        lb5.place(x=600, y=180)
        lb5.configure(bg="white")

        b1 = Button(fr2, text="Retry", font=("Arial ", 20), width=20, command=signup)
        b1.place(x=640, y=300)

    else:
        lb3 = Label(fr2, text="User registered", fg="Green", font=("arial black", 30))
        lb3.place(x=640, y=20)
        lb3.configure(bg="white")

        lb4 = Label(fr2, text="You can Login now", fg="black", font=("arial black", 30))
        lb4.place(x=600, y=100)
        lb4.configure(bg="white")

        b1 = Button(fr2, text="Login", font=("Arial ", 20), width=20, command=Login)
        b1.place(x=640, y=300)

        user_register()


# Creating signup screen [GUI]
def signup():
    global field1
    global field2
    global field3

    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb2 = Label(fr2, text="User Registration", fg="black", font=("arial black", 30))
    lb2.place(x=640, y=20)
    lb2.configure(bg="white")

    lb3 = Label(fr2, text="Username:", fg="black", font=("arial", 20))
    lb3.place(x=60, y=150)
    lb3.configure(bg="white")

    field1 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field1.place(x=250, y=150)

    lb4 = Label(fr2, text="Password:", fg="black", font=("arial", 15))
    lb4.place(x=60, y=200)
    lb4.configure(bg="white")

    field2 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field2.place(x=250, y=200)

    lb5 = Label(fr2, text="Confirm Password:", fg="black", font=("arial", 15))
    lb5.place(x=60, y=250)
    lb5.configure(bg="white")

    field3 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field3.place(x=250, y=250)

    b3 = Button(fr2, text="Submit", font=("Arial ", 10), relief='solid', width=26, command=signup_f)
    b3.place(x=640, y=400)

    b4 = Button(fr2, text="home", fg='white', font=("Arial ", 20), width=15, command=home)
    b4.place(x=640, y=600)
    b4.configure(bg="green")


# Creating login screen [GUI]
def Login():
    global field4
    global field5

    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb2 = Label(fr2, text="LOGIN", fg="black", font=("arial black", 30))
    lb2.place(x=700, y=20)
    lb2.configure(bg="white")

    lb3 = Label(fr2, text="Username:", fg="black", font=("arial", 20))
    lb3.place(x=60, y=150)
    lb3.configure(bg="white")

    field4 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field4.place(x=250, y=150)

    lb4 = Label(fr2, text="Password:", fg="black", font=("arial", 15))
    lb4.place(x=60, y=200)
    lb4.configure(bg="white")

    field5 = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    field5.place(x=250, y=200)

    b3 = Button(fr2, text="Submit", font=("Arial ", 10), relief='solid', width=26, command=Login_f)
    b3.place(x=640, y=300)

    b4 = Button(fr2, text="home", fg='white', font=("Arial ", 20), width=15, command=home)
    b4.place(x=640, y=600)
    b4.configure(bg="green")


def confirm_exit():
    response = messagebox.askokcancel("Confirm Exit","Do You Want to Exit")
    if response == 1:
        sys.exit()


# Creating home screen [GUI]
def home():
    fr = Frame(window, bg = "white", bd=2, width=1920, height=1080)
    fr.place(x=1, y=1)

    #img = ImageTk.PhotoImage(Image.open("download.png"))
    #label = Label(fr, image=img)
    #label.place(x=640, y=200)

    lb1 = Label(fr, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    b1 = Button(fr, text="Login", fg='white', font=("Arial ", 20), width=15, command=Login)
    b1.place(x=100, y=600)
    b1.configure(bg="green")

    b2 = Button(fr, text="Signup", fg='white', font=("Arial ", 20), width=15, command=signup)
    b2.place(x=600, y=600)
    b2.configure(bg="green")

    b3 = Button(fr, text="exit", fg='white', font=("Arial ", 20), width=15, command=confirm_exit)
    b3.place(x=1100, y=600)
    b3.configure(bg="green")


# creating main window
window = Tk()
window.geometry('1920x1080')
window.title("News Bulletin")
window.configure(bg="white")
window.iconbitmap('download.ico')

# globalizing list to store username and password for easy access
global user_list
global password_list

global path

path = 'C:/xampp/htdocs/Project/project.db'

user_list = []
password_list = []
"""video_address = []
video_flag = ['False']"""
# displaying home screen at start
home()

# running main window in endless loop
window.mainloop()
