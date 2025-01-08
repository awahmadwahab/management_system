from pathlib import Path
import webbrowser
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import sqlite3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("user_login/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def switch_to_admin_login():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_login.py"')

def check_credentials():
    username = entry_2.get()
    password = entry_1.get()
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()
    conn.close()

    if user_data and user_data[1] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        window.destroy()
        os.system(f'python "c:/Users/AW/Documents/SE/project/user_dashboard.py" {username}')
    else:
        messagebox.showerror("Login Failed", "Invalid credentials, please try again.")

window = Tk()

window.geometry("1600x900")
window.configure(bg = "#C1C1C1")
window.title("Management System")

canvas = Canvas(
    window,
    bg = "#C1C1C1",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    520.0,
    192.0,
    1079.0,
    780.0,
    fill="#E1E1E1",
    outline="")

canvas.create_rectangle(
    520.0,
    192.0,
    1079.0,
    248.0,
    fill="#1C62A0",
    outline="")

canvas.create_text(
    556.0,
    525.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("InriaSans Regular", 32 * -1)
)

canvas.create_text(
    553.0,
    410.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("InriaSans Regular", 32 * -1)
)

canvas.create_text(
    746.0,
    294.0,
    anchor="nw",
    text="LOG-IN",
    fill="#000000",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    536.0,
    196.0,
    anchor="nw",
    text="USER",
    fill="#FFFFFF",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    574.0,
    73.0,
    anchor="nw",
    text="MUAWIA ENGINEERING WORKS",
    fill="#000000",
    font=("InriaSans Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://muawiaengineeringwork.netlify.app/"),
    relief="flat"
)
button_1.place(
    x=1340.0,
    y=799.0,
    width=175.484130859375,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=switch_to_admin_login,
    relief="flat"
)
button_2.place(
    x=925.0,
    y=707.48291015625,
    width=133.8212127685547,
    height=51.54829025268555
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=check_credentials,
    relief="flat"
)
button_3.place(
    x=723.0,
    y=638.0,
    width=167.65606689453125,
    height=49.26149368286133
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    891.3666687011719,
    544.7722053527832,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=751.0,
    y=525.0,
    width=280.73333740234375,
    height=37.544410705566406
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    891.3666687011719,
    431.7722053527832,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=751.0,
    y=412.0,
    width=280.73333740234375,
    height=37.544410705566406
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    88.0,
    73.0,
    image=image_image_1
)

window.mainloop()
