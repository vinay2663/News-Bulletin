# importing required packages
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import os
import shutil
from tkinter import messagebox
import time


def get_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


def update_password():
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("""UPDATE username set password = :new_pass
     where password = :old_password""",
                 {
                     'new_pass': new_pass,
                     'old_password': old_pass
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


def upload_p():
    name = n_p.get()
    n_p.delete(0, END)

    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    time1 = get_time()

    c.execute("INSERT INTO pdf VALUES (:name, :time, :uploader)",
              {
                  'name': name,
                  'time': time1,
                  'uploader': Login_Name
              })

    conn.commit()
    conn.close()


def upload_vi():
    name = n_v.get()
    n_v.delete(0, END)
    des = t_v.get("1.0", END)
    t_v.delete("1.0", END)

    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    time1 = get_time()

    c.execute("INSERT INTO video VALUES (:name, :des, :time, :uploader)",
              {
                  'name': name,
                  'des' : des,
                  'time': time1,
                  'uploader': Login_Name
              })

    conn.commit()
    conn.close()


def upload_im():
    name = n_i.get()
    des = t_i.get("1.0", END)
    n_i.delete(0, END)
    t_i.delete("1.0", END)
    label.destroy()

    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    time1 = get_time()

    c.execute("INSERT INTO image VALUES (:name, :description, :time, :uploader)",
              {
                  'name': name,
                  'description': des,
                  'time': time1,
                  'uploader': Login_Name
              })

    conn.commit()
    conn.close()


# function to upload an image
def upload_i():
    global img
    global label
    window.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                               filetypes=[("png files", "*.png"), ("jpg files", "*.jpg"),
                                                          ("jpeg files", "*.jpeg"), ("all files", "*.*")])

    if window.filename:
        head, tail = os.path.split(window.filename)
        n_i.delete(0, END)
        n_i.insert(0, tail)
        shutil.copy(window.filename, 'C:/xampp/htdocs/Project/Assets/Uploads/images')
        img = ImageTk.PhotoImage(Image.open(window.filename))
        label = Label(window, image=img)
        label.place(x=950, y=250, width = 500, height= 400)


# function to upload a video
def upload_v():
    window.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                               filetypes=[("mp4 files", "*.mp4"), ("all files", "*.*")])

    if window.filename:
        head, tail = os.path.split(window.filename)
        n_v.delete(0, END)
        n_v.insert(0, tail)
        shutil.copy(window.filename, 'C:/xampp/htdocs/Project/Assets/Uploads/videos')


# function to upload a pdf
def upload_pdf():
    window.filename = filedialog.askopenfilename(initialdir="F:/major_project/GUI", title="Choose a file",
                                                 filetypes=[("pdf files", "*.pdf"), ("all files", "*.*")])

    if window.filename:
        head, tail = os.path.split(window.filename)
        n_p.delete(0, END)
        n_p.insert(0, tail)
        shutil.copy(window.filename, 'C:/xampp/htdocs/Project/Assets/Uploads/pdf')


# function to upload a text
def upload_text():
    circular = t_t.get("1.0", END)
    t_t.delete("1.0", END)
    file1 = open(r"C:/xampp/htdocs/Project/Assets/Uploads/circular.txt", "r+")
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


def image():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    b1 = Button(fr2, text="Choose File", font=("Arial ", 20), width=20, command=upload_i)
    b1.place(x=100, y=250)
    b1.configure(bg="white")

    global n_i
    global t_i

    lb3 = Label(fr2, text="Name", font=("TimesNewRoman", 18))
    lb3.place(x=150, y=350)
    lb3.configure(bg = "white")

    n_i = Entry(fr2, fg="black", font=("arial", 20))
    n_i.place(x=250,y=350)

    lb4 = Label(fr2, text="Description", font=("TimesNewRoman", 18))
    lb4.place(x=100, y=450)
    lb4.configure(bg = "white")

    t_i = Text(fr2, font= ("TimesNewRoman", 18))
    t_i.place(x=250,y=450, height=150, width =600)

    b2 = Button(fr2, text="Submit", font=("Arial ", 20), width=20, command=upload_im)
    b2.place(x=100, y=700)
    b2.configure(bg="white")

    b3 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b3.place(x=900, y=700)
    b3.configure(bg="green")


def video():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    b1 = Button(fr2, text="Choose File", font=("Arial ", 20), width=20, command=upload_v)
    b1.place(x=100, y=250)
    b1.configure(bg="white")

    global n_v
    global t_v

    lb3 = Label(fr2, text="Name", font=("TimesNewRoman", 18))
    lb3.place(x=150, y=350)
    lb3.configure(bg = "white")

    n_v = Entry(fr2, fg="black", font=("arial", 20))
    n_v.place(x=250,y=350)

    lb4 = Label(fr2, text="Description", font=("TimesNewRoman", 18))
    lb4.place(x=100, y=450)
    lb4.configure(bg="white")

    t_v = Text(fr2, font=("TimesNewRoman", 18))
    t_v.place(x=250, y=450, height=150, width=600)

    b2 = Button(fr2, text="Submit", font=("Arial ", 20), width=20, command=upload_vi)
    b2.place(x=100, y=700)
    b2.configure(bg="white")

    b3 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b3.place(x=900, y=700)
    b3.configure(bg="green")


def pdf():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    b1 = Button(fr2, text="Choose File", font=("Arial ", 20), width=20, command=upload_pdf)
    b1.place(x=100, y=250)
    b1.configure(bg="white")

    global n_p

    lb3 = Label(fr2, text="Name", font=("TimesNewRoman", 18))
    lb3.place(x=150, y=350)
    lb3.configure(bg="white")

    n_p = Entry(fr2, fg="black", font=("arial", 20))
    n_p.place(x=250, y=350)

    b2 = Button(fr2, text="Submit", font=("Arial ", 20), width=20, command=upload_p)
    b2.place(x=100, y=700)
    b2.configure(bg="white")

    b3 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b3.place(x=900, y=700)
    b3.configure(bg="green")


def text():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb4 = Label(fr2, text="Flash News", font=("TimesNewRoman", 26))
    lb4.place(x=100, y=250)
    lb4.configure(bg="white")

    global t_t

    t_t = Text(fr2, font=("TimesNewRoman", 20))
    t_t.place(x=100, y=300, height=370, width=600)

    b2 = Button(fr2, text="Submit", font=("Arial ", 20), width=20, command=upload_text)
    b2.place(x=100, y=700)
    b2.configure(bg="white")

    b3 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b3.place(x=900, y=700)
    b3.configure(bg="green")


def about():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text="Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)


def flag(key):
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("INSERT INTO flag VALUES (:status)",
              {
                  'status' : key
              })

    conn.commit()
    conn.close()

    lb3 = Label(window, text=key+' is selected', font=("TimesNewRoman", 30))
    lb3.place(x=100, y=650)
    lb3.configure(bg="white", fg= "Blue")


def get_admin():
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT *, oid  FROM admin")
    records = c.fetchall()

    for record in records:
        admin_list.append(record[0])

    conn.commit()
    conn.close()
    return


def add_admin(admin_name):
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("INSERT INTO admin VALUES (:name)",
              {
                  'name': admin_name
              })

    conn.commit()
    conn.close()
    return


def remove_admin(admin_name):
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("SELECT *, oid  FROM admin")
    records = c.fetchall()

    conn.execute("""DELETE FROM admin
        where name = :name""",
                 {
                     'name': admin_name
                 })

    conn.commit()
    conn.close()

    return


def control():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Control Panel ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=270)
    lb3.configure(bg="white", fg= "Blue")

    b3 = Button(fr2, text="Image", font=("Arial ", 20), width=20, command=lambda: flag('image'))
    b3.place(x=100, y=400)
    b3.configure(bg="white")

    b2 = Button(fr2, text="Video", font=("Arial ", 20), width=20, command=lambda: flag('video'))
    b2.place(x=600, y=400)
    b2.configure(bg="white")

    b1 = Button(fr2, text="Default", font=("Arial ", 20), width=20, command=lambda: flag('original'))
    b1.place(x=100, y=550)
    b1.configure(bg="white")

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=600, y=550)
    b4.configure(bg="white")

    b5 = Button(fr2, text="Logs", font=("Arial ", 20), width=20, command=Logs)
    b5.place(x=1100, y=400)
    b5.configure(bg="white")

    return


def Logs():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Logs ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=270)
    lb3.configure(bg="white", fg="Blue")

    b3 = Button(fr2, text="Image", font=("Arial ", 20), width=20, command=Image_logs)
    b3.place(x=100, y=400)
    b3.configure(bg="white")

    b2 = Button(fr2, text="Video", font=("Arial ", 20), width=20, command=Video_logs)
    b2.place(x=600, y=400)
    b2.configure(bg="white")

    b1 = Button(fr2, text="PDF", font=("Arial ", 20), width=20, command=PDF_logs)
    b1.place(x=100, y=550)
    b1.configure(bg="white")

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=600, y=550)
    b4.configure(bg="white")

    return


def get_logs(key):
    if key == 'image':
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("SELECT *, oid  FROM image")
        records = c.fetchall()
        for record in records:
            image_log_box.insert(INSERT,'Name: '+record[0])
            image_log_box.insert(INSERT, '\n')

            image_log_box.insert(INSERT, 'Description: ' + record[1])

            image_log_box.insert(INSERT, 'Time: ' + record[2])
            image_log_box.insert(INSERT, '\n')

            image_log_box.insert(INSERT, 'Uploader: ' + record[3])
            image_log_box.insert(INSERT, '\n')
            image_log_box.insert(INSERT, '\n')

        conn.commit()
        conn.close()

    if key == 'video':
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("SELECT *, oid  FROM video")
        records = c.fetchall()

        for record in records:
            video_log_box.insert(INSERT, 'Name: ' + record[0])
            video_log_box.insert(INSERT, '\n')

            video_log_box.insert(INSERT, 'Description: ' + record[1])

            video_log_box.insert(INSERT, 'Time: ' + record[2])
            video_log_box.insert(INSERT, '\n')

            video_log_box.insert(INSERT, 'Uploader: ' + record[3])
            video_log_box.insert(INSERT, '\n')
            video_log_box.insert(INSERT, '\n')

        conn.commit()
        conn.close()

    if key == 'pdf':
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("SELECT *, oid  FROM pdf")
        records = c.fetchall()

        for record in records:
            pdf_log_box.insert(INSERT, 'Name: ' + record[0])
            pdf_log_box.insert(INSERT, '\n')

            pdf_log_box.insert(INSERT, 'Time: ' + record[1])
            pdf_log_box.insert(INSERT, '\n')

            pdf_log_box.insert(INSERT, 'Uploader: ' + record[2])
            pdf_log_box.insert(INSERT, '\n')
            pdf_log_box.insert(INSERT, '\n')

        conn.commit()
        conn.close()

    return


def Image_logs():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Logs ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=270)
    lb3.configure(bg="white", fg="Blue")

    global image_log_box

    image_log_box = Text(fr2, fg="black", font=("arial", 20), relief='solid')
    image_log_box.place(x=100, y=350, width=600, height=400)

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=1000, y=550)
    b4.configure(bg="white")

    get_logs('image')

    return


def Video_logs():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Logs ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=270)
    lb3.configure(bg="white", fg="Blue")

    global video_log_box

    video_log_box = Text(fr2, fg="black", font=("arial", 20), relief='solid')
    video_log_box.place(x=100, y=350, width=600, height=400)

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=1000, y=550)
    b4.configure(bg="white")

    get_logs('video')

    return


def PDF_logs():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Logs ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=270)
    lb3.configure(bg="white", fg="Blue")

    global pdf_log_box

    pdf_log_box = Text(fr2, fg="black", font=("arial", 20), relief='solid')
    pdf_log_box.place(x=100, y=350, width=600, height=400)

    b4 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b4.place(x=1000, y=550)
    b4.configure(bg="white")

    get_logs('pdf')

    return


def allow_privileges():
    admin_name = entry.get()
    entry.delete(0, END)

    user_login()
    get_admin()

    if check(user_list, admin_name):
        if  not check(admin_list, admin_name):
            add_admin(admin_name)

            lb3 = Label(window, text="Granted privileges", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white", fg="Blue")

        else:
            lb3 = Label(window, text="User already has admin privileges", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white", fg="Blue")

    else:
        lb3 = Label(window, text="No user found", font=("TimesNewRoman", 30))
        lb3.place(x=100, y=700)
        lb3.configure(bg="white", fg="Blue")

    user_list.clear()
    password_list.clear()
    admin_list.clear()


def revoke_privileges():
    admin_name = entry.get()
    entry.delete(0, END)

    if admin_name == 'v':
        lb3 = Label(window, text="Cannot remove privileges for default user", font=("TimesNewRoman", 30))
        lb3.place(x=100, y=700)
        lb3.configure(bg="white")

        return

    user_login()
    get_admin()

    if check(user_list, admin_name):
        if check(admin_list, admin_name):
            remove_admin(admin_name)

            lb3 = Label(window, text="Revoked privileges", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white")

        else:
            lb3 = Label(window, text="User does not have admin privileges", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white")

    else:
        lb3 = Label(window, text="No user found", font=("TimesNewRoman", 30))
        lb3.place(x=100, y=700)
        lb3.configure(bg="white", fg="Blue")

    user_list.clear()
    password_list.clear()
    admin_list.clear()


def remove_from_user(user_name):
    # connecting to database
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("""DELETE FROM username
           where name = :name""",
                 {
                     'name': user_name
                 })

    conn.commit()
    conn.close()


def remove_user():
    remove_name = entry.get()
    entry.delete(0, END)
    if remove_name == 'v':
        lb3 = Label(window, text=" Cannot remove default user ", font=("TimesNewRoman", 30))
        lb3.place(x=100, y=700)
        lb3.configure(bg="white")

        return

    user_login()
    get_admin()

    if check(user_list, remove_name):
        if check(admin_list, remove_name):
            remove_admin(remove_name)
            remove_from_user(remove_name)

            lb3 = Label(window, text="User Removed", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white")

        else:
            remove_from_user(remove_name)

            lb3 = Label(window, text="User Removed", font=("TimesNewRoman", 30))
            lb3.place(x=100, y=700)
            lb3.configure(bg="white")

    else:
        lb3 = Label(window, text="No user found", font=("TimesNewRoman", 30))
        lb3.place(x=100, y=700)
        lb3.configure(bg="white", fg="Blue")

    user_list.clear()
    password_list.clear()
    admin_list.clear()


def manage_users():
    fr2 = Frame(window, bg="white", bd=2, width=1920, height=1080)
    fr2.place(x=1, y=1)

    lb1 = Label(fr2, text=" Srinivas Institute of technology ", fg="white", font=("TimesNewRoman", 30), relief='sunken',
                width=70, height=2)
    lb1.place(x=1, y=10)
    lb1.configure(bg="dark blue")

    lb2 = Label(fr2, text="Department of Electronics and Communication Engineering  ", font=("TimesNewRoman", 30),
                width=70, height=2)
    lb2.place(x=1, y=100)

    lb3 = Label(fr2, text=" Manage Users ", font=("TimesNewRoman", 30))
    lb3.place(x=100, y=220)
    lb3.configure(bg="white", fg="Blue")

    b3 = Button(fr2, text="Add user", font=("Arial ", 20), width=20, command=signup)
    b3.place(x=100, y=320)
    b3.configure(bg = "white")

    lb4 = Label(fr2, text=" Enter User", font=("TimesNewRoman", 22))
    lb4.place(x=100, y=420)
    lb4.configure(bg="white")

    global entry

    entry = Entry(fr2, fg="black", font=("arial", 20), relief='solid')
    entry.place(x=300, y=420)

    b4 = Button(fr2, text="Allow Admin Privileges ", font=("Arial ", 20), width=20, command=allow_privileges)
    b4.place(x=100, y=480)
    b4.configure(bg = "white")

    b5 = Button(fr2, text="Provoke Admin Privileges", font=("Arial ", 20), width=20, command=revoke_privileges)
    b5.place(x=500, y=480)
    b5.configure(bg = "white")

    b7 = Button(fr2, text="Remove user", font=("Arial ", 20), width=20, command=remove_user)
    b7.place(x=900, y=480)
    b7.configure(bg="white")

    b6 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
    b6.place(x=600, y=600)
    b6.configure(bg="white")

    return


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

    lb3 = Label(fr2, text = "News Bulletin ", font=("Algerian", 26))
    lb3.place(x=40,y=230)
    lb3.configure(bg="white")

    lb4 = Label(fr2, text = "Project 2020", font=("Algerian", 24))
    lb4.place(x=700,y=230)
    lb4.configure(bg="white")

    b5 = Button(fr2, text="About", font=("Arial ", 20), width=20, command=about)
    b5.place(x=1100, y=230)
    b5.configure(bg = "white")

    b3 = Button(fr2, text="Image", font=("Arial ", 20), width=20, command=image)
    b3.place(x=100, y=400)
    b3.configure(bg = "white")

    b4 = Button(fr2, text="Video", font=("Arial ", 20), width=20, command=video)
    b4.place(x=100, y=550)
    b4.configure(bg = "white")

    b6 = Button(fr2, text="Flash News", font=("Arial ", 20), width=20, command=text)
    b6.place(x=600, y=550)
    b6.configure(bg = "white")

    b7 = Button(fr2, text="PDF", font=("Arial ", 20), width=20, command=pdf)
    b7.place(x=600, y=400)
    b7.configure(bg = "white")

    b8 = Button(fr2, text="Control", font=("Arial ", 20), width=20, command=control)
    b8.place(x=1100, y=400)
    b8.configure(bg = "white")

    get_admin()

    if check(admin_list, Login_Name):
        b9 = Button(fr2, text="Manage Users", font=("Arial ", 20), width=20, command=manage_users)
        b9.place(x=1100, y=550)
        b9.configure(bg = "white")

    b2 = Button(fr2, text="logout", fg='white', font=("Arial ", 20), width=20, command=home)
    b2.place(x=1040, y=750)
    b2.configure(bg="green")

    b8 = Button(fr2, text="Change Password", fg='white', font=("Arial ", 20), width=20, command=change_password)
    b8.place(x=40, y=760)
    b8.configure(bg="green")


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
    global Login_Name

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

    user_login()

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

    elif check(user_list, Name):
        lb3 = Label(fr2, text="User Registration failed", fg="red", font=("arial black", 30))
        lb3.place(x=600, y=20)
        lb3.configure(bg="white")

        lb4 = Label(fr2, text="Select an unique Username", fg="black", font=("arial black", 30))
        lb4.place(x=600, y=100)
        lb4.configure(bg="white")

        lb5 = Label(fr2, text="Please try again", fg="black", font=("arial black", 30))
        lb5.place(x=600, y=180)
        lb5.configure(bg="white")

        user_list.clear()
        password_list.clear()

        b1 = Button(fr2, text="Retry", font=("Arial ", 20), width=20, command=signup)
        b1.place(x=640, y=300)

    else:
        lb3 = Label(fr2, text="User registered", fg="Green", font=("arial black", 30))
        lb3.place(x=640, y=20)
        lb3.configure(bg="white")

        lb4 = Label(fr2, text="You can Login now", fg="black", font=("arial black", 30))
        lb4.place(x=600, y=100)
        lb4.configure(bg="white")

        user_register()

        b1 = Button(fr2, text="Login", font=("Arial ", 20), width=20, command=Login)
        b1.place(x=640, y=300)

        b2 = Button(fr2, text="Back", font=("Arial ", 20), width=20, command=main_screen)
        b2.place(x=640, y=400)


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

    b4 = Button(fr2, text="Back", fg='white', font=("Arial ", 20), width=15, command=manage_users)
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
    global image1
    fr = Frame(window, bg = "white", bd=2, width=1920, height=1080)
    fr.place(x=1, y=1)

    image1 = ImageTk.PhotoImage(Image.open("Assets/image.png"))
    label = Label(fr, image=image1)
    label.place(x=640, y=250)

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

    b2 = Button(fr, text="About", fg='white', font=("Arial ", 20), width=15, command=about)
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
window.iconbitmap('Assets/logo.ico')

# globalizing list to store username and password for easy access
global user_list
global password_list
global admin_list

global path

path = 'C:/xampp/htdocs/Project/project.db'

user_list = []
password_list = []
admin_list = []

# displaying home screen at start
home()

# running main window in endless loop
window.mainloop()
