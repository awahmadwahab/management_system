from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\AW\Documents\SE\project\ADMIN_DASHBOARD\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fetch_users():
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, password FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def add_user():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, email, password, full_name)
        VALUES (?, ?, ?, ?)
    ''', (username, email, password, "New User"))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User added successfully.")
    refresh_user_list()

def delete_user():
    user_id = entry_user_id.get()
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User deleted successfully.")
    refresh_user_list()

def refresh_user_list():
    users = fetch_users()
    y_position = 350
    canvas.delete("user")
    for user in users:
        user_id, username, email, password = user
        canvas.create_text(464, y_position, anchor="nw", text=user_id, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="user")
        canvas.create_text(596, y_position, anchor="nw", text=username, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="user")
        canvas.create_text(791, y_position, anchor="nw", text=email, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="user")
        canvas.create_text(1019, y_position, anchor="nw", text=password, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="user")
        y_position += 50

def logout():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_login.py"')

def go_transactions():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_transaction.py"')

def go_reports():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_report.py"')

window = Tk()

window.geometry("1600x900")
window.configure(bg = "#C1C1C1")

canvas = Canvas(
    window,
    bg = "#C1C1C1",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1600.0,
    124.0,
    fill="#C1C1C1",
    outline=""
)

canvas.create_rectangle(
    447.0,
    235.0,
    1154.0,
    291.0,
    fill="#1C62A0",
    outline=""
)

canvas.create_rectangle(
    0.0,
    124.0,
    259.0,
    900.0,
    fill="#1C62A0",
    outline=""
)

canvas.create_rectangle(
    521.0,
    34.0,
    1080.0,
    90.0,
    fill="#5E5E5E",
    outline=""
)

canvas.create_text(
    479.0,
    244.0,
    anchor="nw",
    text="ID",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    611.0,
    244.0,
    anchor="nw",
    text="Username",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    806.0,
    244.0,
    anchor="nw",
    text="Email",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    1034.0,
    244.0,
    anchor="nw",
    text="Password",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    643.0,
    38.0,
    anchor="nw",
    text="Admin Dashboard",
    fill="#FFFFFF",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    750.0,
    158.0,
    anchor="nw",
    text="USERS",
    fill="#000000",
    font=("InriaSans Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_user,
    relief="flat"
)
button_1.place(
    x=442.0,
    y=613.0,
    width=123.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=delete_user,
    relief="flat"
)
button_2.place(
    x=620.0,
    y=613.0,
    width=123.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_3.place(
    x=1436.0,
    y=60.0,
    width=117.62870788574219,
    height=51.54829025268555
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=70.0,
    y=268.0,
    width=140.0,
    height=51.54829025268555
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=go_transactions,
    relief="flat"
)
button_5.place(
    x=70.0,
    y=371.0,
    width=140.0,
    height=51.54829025268555
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=go_reports,
    relief="flat"
)
button_6.place(
    x=70.0,
    y=474.0,
    width=140.0,
    height=51.54829025268555
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    92.0,
    62.0,
    image=image_image_1
)

canvas.create_rectangle(
    619.0,
    492.0,
    1046.0,
    493.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    123.0,
    1600.0,
    124.0,
    fill="#000000",
    outline="")

# Entry fields for user data
entry_user_id = Entry(window, bd=0, bg="#D9D9D9", highlightthickness=0)
entry_user_id.place(x=456.0, y=522.0, width=95.0, height=41.0)

entry_username = Entry(window, bd=0, bg="#D9D9D9", highlightthickness=0)
entry_username.place(x=581.0, y=522.0, width=162.0, height=41.0)

entry_email = Entry(window, bd=0, bg="#D9D9D9", highlightthickness=0)
entry_email.place(x=770.0, y=522.0, width=162.0, height=41.0)

entry_password = Entry(window, bd=0, bg="#D9D9D9", highlightthickness=0)
entry_password.place(x=992.0, y=522.0, width=162.0, height=41.0)

refresh_user_list()

window.resizable(False, False)
window.mainloop()
