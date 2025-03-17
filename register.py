from tkinter import *
from tkinter import messagebox
import sqlite3
import os

# Database Connection
def connect_db():
    conn = sqlite3.connect("srms.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

connect_db()

# Register Function
def register_user():
    username = entry_reg_user.get()
    password = entry_reg_pass.get()
    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        conn = sqlite3.connect("srms.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchone():
            messagebox.showerror("Error", "Username already exists!")
        else:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful!")
        conn.close()

def login_user():
    username = entry_log_user.get()
    password = entry_log_pass.get()
    conn = sqlite3.connect("srms.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if cur.fetchone():
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        try:
            import srms_main  # Assuming the main SRMS code is in 'srms_main.py'
        except ModuleNotFoundError:
            os.system("python srms.py")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")
    conn.close()

root = Tk()
root.title("Login & Register")
root.geometry("400x500")

# Register Frame
frame_reg = LabelFrame(root, text="Register", padx=10, pady=10)
frame_reg.pack(pady=20)
Label(frame_reg, text="Username:").grid(row=0, column=0)
entry_reg_user = Entry(frame_reg)
entry_reg_user.grid(row=0, column=1)
Label(frame_reg, text="Password:").grid(row=1, column=0)
entry_reg_pass = Entry(frame_reg, show="*")
entry_reg_pass.grid(row=1, column=1)
Button(frame_reg, text="Register", command=register_user).grid(columnspan=2)

# Login Frame
frame_log = LabelFrame(root, text="Login", padx=10, pady=10)
frame_log.pack(pady=20)
Label(frame_log, text="Username:").grid(row=0, column=0)
entry_log_user = Entry(frame_log)
entry_log_user.grid(row=0, column=1)
Label(frame_log, text="Password:").grid(row=1, column=0)
entry_log_pass = Entry(frame_log, show="*")
entry_log_pass.grid(row=1, column=1)
Button(frame_log, text="Login", command=login_user).grid(columnspan=2)

root.mainloop()
