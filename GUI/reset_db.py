import os
import sqlite3
import platform


def reset_db():
    name = 'v'
    password = '1'
    flag = 'original'

    if os.path.exists(path):
        os.remove(path)

    conn = sqlite3.connect(path)

    c = conn.cursor()

    c.execute("""CREATE TABLE username(
             name text,
             password text
             )
    """)

    c.execute("""CREATE TABLE video(
             name text,
             description text,
             time text,
             uploader text
             )
    """)

    c.execute("""CREATE TABLE pdf(
             name text,
             time text,
             uploader text
             )
    """)

    c.execute("""CREATE TABLE image(
            name text,
            description text,
            time text,
            uploader text
            )
    """)

    c.execute("""CREATE TABLE admin(
              name text
              ) """)

    c.execute("INSERT INTO admin VALUES (:name)",
              {
                  'name': name
              })

    c.execute("INSERT INTO username VALUES (:name, :password)",
              {
                  'name': name,
                  'password': password
              })

    c.execute("""CREATE TABLE flag(
              status text
              ) """)

    c.execute("INSERT INTO flag VALUES (:status)",
              {
                  'status': flag
              })

    conn.commit()
    conn.close()

    return


def get_platform():

    global path

    if platform.system() == 'Windows':
        path = r'C:/xampp/htdocs/Project/project.db'

    if platform.system() == 'Linux':
        path = r'/opt/lampp/htdocs/Project/project.db'

    return


get_platform()
reset_db()
