import sys
from pathlib import Path
import os
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from transaction_database import fetch_transactions

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\AW\Documents\SE\project\user_dashboard\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/user_login.py"')

def edit_profile():
    window.destroy()
    os.system(f'python "c:/Users/AW/Documents/SE/project/user_profile.py" {username}')

def go_transactions():
    window.destroy()
    os.system(f'python "c:/Users/AW/Documents/SE/project/transaction.py" {username}')

def go_reports():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/reports.py"')

def fetch_user_data(username):
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, password, full_name FROM users WHERE username=?", (username,))
    user_info = cursor.fetchone()
    conn.close()
    return user_info

def fetch_transaction_data(username):
    return fetch_transactions(username)

def refresh_dashboard_ui(username):
    user_data = fetch_user_data(username)
    if user_data:
        canvas.itemconfig(username_text, text=user_data[0])  # username
        canvas.itemconfig(email_text, text=user_data[1])     # email
        canvas.itemconfig(password_text, text=user_data[2])  # password
    
    transactions = fetch_transaction_data(username)
    y_position = 650
    for transaction in transactions:
        sr_no, date, client, amount, debit = transaction
        canvas.create_text(464, y_position, anchor="nw", text=sr_no, fill="#000000", font=("InriaSans Regular", 24 * -1))
        canvas.create_text(596, y_position, anchor="nw", text=date, fill="#000000", font=("InriaSans Regular", 24 * -1))
        canvas.create_text(791, y_position, anchor="nw", text=client, fill="#000000", font=("InriaSans Regular", 24 * -1))
        canvas.create_text(1019, y_position, anchor="nw", text=amount, fill="#000000", font=("InriaSans Regular", 24 * -1))
        canvas.create_text(1245, y_position, anchor="nw", text=debit, fill="#000000", font=("InriaSans Regular", 24 * -1))
        y_position += 50

def refresh_dashboard(username):
    refresh_dashboard_ui(username)

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

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1600.0,
    124.0,
    fill="#C1C1C1",
    outline="")

canvas.create_rectangle(
    427.0,
    589.0,
    1238.0,
    645.0,
    fill="#1C62A0",
    outline="")

canvas.create_rectangle(
    0.0,
    124.0,
    259.0,
    900.0,
    fill="#1C62A0",
    outline="")

canvas.create_rectangle(
    521.0,
    34.0,
    1080.0,
    90.0,
    fill="#5E5E5E",
    outline="")

# Get the username from command-line arguments
username = sys.argv[1] if len(sys.argv) > 1 else "user"

user_data = fetch_user_data(username)
username = user_data[0] if user_data else "User"
email = user_data[1] if user_data else "abc@mail.com"
password = user_data[2] if user_data else "user123"

canvas.create_text(
    625.0,
    332.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

canvas.create_text(
    620.0,
    234.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

canvas.create_text(
    652.0,
    283.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

password_text = canvas.create_text(
    788.0,
    332.0,
    anchor="nw",
    text=password,
    fill="#000000",
    font=("InriaSans Regular", 24 * -1)
)

username_text = canvas.create_text(
    788.0,
    234.0,
    anchor="nw",
    text=username,
    fill="#000000",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    464.0,
    598.0,
    anchor="nw",
    text="Sr.No",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    596.0,
    598.0,
    anchor="nw",
    text="Date",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    791.0,
    598.0,
    anchor="nw",
    text="Client",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    1019.0,
    598.0,
    anchor="nw",
    text="Amount",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    1245.0,
    598.0,
    anchor="nw",
    text="Debit",
    fill="#D9D9D9",
    font=("InriaSans Regular", 24 * -1)
)

email_text = canvas.create_text(
    788.0,
    283.0,
    anchor="nw",
    text=email,
    fill="#000000",
    font=("InriaSans Regular", 24 * -1)
)

canvas.create_text(
    700.0,
    129.0,
    anchor="nw",
    text="User Profile",
    fill="#000000",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    664.0,
    38.0,
    anchor="nw",
    text="User Dashboard",
    fill="#FFFFFF",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    642.0,
    512.0,
    anchor="nw",
    text="Transactions History",
    fill="#000000",
    font=("InriaSans Regular", 36 * -1)
)

button_view_transaction_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_view_transaction = Button(
    image=button_view_transaction_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_transactions,
    relief="flat"
)
button_view_transaction.place(
    x=771.0,
    y=792.0,
    width=123.0,
    height=41.0
)

button_logout_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_logout = Button(
    image=button_logout_image,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_logout.place(
    x=1436.0,
    y=60.0,
    width=117.62870788574219,
    height=51.54829025268555
)

button_edit_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_edit = Button(
    image=button_edit_image,
    borderwidth=0,
    highlightthickness=0,
    command=edit_profile,
    relief="flat"
)
button_edit.place(
    x=1100.0,
    y=268.0,
    width=98.93389892578125,
    height=51.54829025268555
)

button_home_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_home = Button(
    image=button_home_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_home clicked"),
    relief="flat"
)
button_home.place(
    x=70.0,
    y=268.0,
    width=140.0,
    height=51.54829025268555
)
button_profile_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_profile = Button(
    image=button_profile_image,
    borderwidth=0,
    highlightthickness=0,
    command=edit_profile,
    relief="flat"
)
button_profile.place(
    x=69.0,
    y=375.0,
    width=140.0,
    height=51.54829025268555
)

button_transaction_image = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_transaction = Button(
    image=button_transaction_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_transactions,
    relief="flat"
)
button_transaction.place(
    x=68.0,
    y=482.0,
    width=140.0,
    height=51.54829025268555
)

button_reports_image = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_reports = Button(
    image=button_reports_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_reports,
    relief="flat"
)
button_reports.place(
    x=70.0,
    y=589.0,
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
    322.0,
    171.0,
    548.0,
    397.0,
    fill="#000000",
    outline="")

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

window.resizable(False, False)

refresh_dashboard(username)

window.mainloop()
