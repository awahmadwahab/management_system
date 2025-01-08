from pathlib import Path
import os
import sys
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("user_profile/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/user_login.py"')

def go_home():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/user_dashboard.py"')

def go_transactions():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/transaction.py"')

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

old_user = None

def save_profile():
    global old_user
    new_username = entry_username.get()
    new_email = entry_email.get()
    new_password = entry_password.get()
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username=?", (old_user,))
    # Keeping full_name as a placeholder
    cursor.execute('''
        INSERT INTO users (username, email, password, full_name)
        VALUES (?, ?, ?, ?)
    ''', (new_username, new_email, new_password, "Updated User"))
    conn.commit()
    conn.close()
    refresh_profile(new_username)

def refresh_profile(username="user"):
    global old_user
    old_user = username
    user_data = fetch_user_data(username)
    username_text = user_data[0] if user_data else "User"
    email_text = user_data[1] if user_data else "abc@mail.com"
    password_text = user_data[2] if user_data else "user123"
    
    entry_username.delete(0, 'end')
    entry_username.insert(0, username_text)
    entry_email.delete(0, 'end')
    entry_email.insert(0, email_text)
    entry_password.delete(0, 'end')
    entry_password.insert(0, password_text)

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

canvas.create_text(
    642.0,
    556.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

canvas.create_text(
    637.0,
    458.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

canvas.create_text(
    669.0,
    507.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("InriaSans Bold", 24 * -1)
)

entry_username = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_username.place(
    x=805.0,
    y=458.0,
    width=200.0,
    height=30.0
)

entry_email = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_email.place(
    x=805.0,
    y=507.0,
    width=200.0,
    height=30.0
)

entry_password = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_password.place(
    x=805.0,
    y=556.0,
    width=200.0,
    height=30.0
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

button_logout_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
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

button_edit_profile_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_edit_profile = Button(
    image=button_edit_profile_image,
    borderwidth=0,
    highlightthickness=0,
    command=save_profile,
    relief="flat"
)
button_edit_profile.place(
    x=751.0,
    y=704.0,
    width=98.93389892578125,
    height=51.54829025268555
)

button_home_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_home = Button(
    image=button_home_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_home,
    relief="flat"
)
button_home.place(
    x=70.0,
    y=268.0,
    width=140.0,
    height=51.54829025268555
)

button_profile_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_profile = Button(
    image=button_profile_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_profile clicked"),
    relief="flat"
)
button_profile.place(
    x=69.0,
    y=375.0,
    width=140.0,
    height=51.54829025268555
)

button_transactions_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_transactions = Button(
    image=button_transactions_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_transactions,
    relief="flat"
)
button_transactions.place(
    x=68.0,
    y=482.0,
    width=140.0,
    height=51.54829025268555
)

button_report_image = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_report = Button(
    image=button_report_image,
    borderwidth=0,
    highlightthickness=0,
    command=go_reports,
    relief="flat"
)
button_report.place(
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
    687.0,
    203.0,
    913.0,
    429.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    586.0,
    624.0,
    1013.0,
    625.0,
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

if __name__ == "__main__":
    current_user = sys.argv[1] if len(sys.argv) > 1 else "user"
    refresh_profile(current_user)
    window.mainloop()
