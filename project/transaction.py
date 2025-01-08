from pathlib import Path
import os
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from transaction_database import insert_transaction, fetch_transactions, delete_transaction

# Get the username from command-line arguments
username = sys.argv[1] if len(sys.argv) > 1 else "user"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("transaction/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/user_login.py"')

def edit_profile():
    window.destroy()
    os.system(f'python "c:/Users/AW/Documents/SE/project/user_profile.py" {username}')

def go_home():
    window.destroy()
    os.system(f'python "c:/Users/AW/Documents/SE/project/user_dashboard.py" {username}')

def go_reports():
    window.destroy()
    os.system(f'python "c:/Users/AW/Documents/SE/project/reports.py" {username}')

def add_transaction():
    sr_no = int(entry_sr_no.get())
    date = entry_date.get()
    client = entry_client.get()
    amount = float(entry_amount.get())
    debit = float(entry_debit.get())
    insert_transaction(username, sr_no, date, client, amount, debit)
    update_transaction_list()

def delete_transaction_ui():
    sr_no = int(entry_sr_no.get())
    delete_transaction(username, sr_no)
    update_transaction_list()

def update_transaction_list():
    transactions = fetch_transactions(username)
    y_position = 650
    total_credit = 0
    total_debit = 0
    canvas.delete("transaction")
    for transaction in transactions:
        sr_no, date, client, amount, debit = transaction
        total_credit += amount
        total_debit += debit
        canvas.create_text(464, y_position, anchor="nw", text=sr_no, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="transaction")
        canvas.create_text(596, y_position, anchor="nw", text=date, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="transaction")
        canvas.create_text(791, y_position, anchor="nw", text=client, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="transaction")
        canvas.create_text(1019, y_position, anchor="nw", text=amount, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="transaction")
        canvas.create_text(1245, y_position, anchor="nw", text=debit, fill="#000000", font=("InriaSans Regular", 24 * -1), tags="transaction")
        y_position += 50

    # Update total credit and debit on the screen
    canvas.itemconfig(total_credit_text, text=str(total_credit))
    canvas.itemconfig(total_debit_text, text=str(total_debit))

if __name__ == "__main__":
    window = Tk()

    window.geometry("1600x900")
    window.configure(bg = "#C1C1C1")

    canvas = Canvas(
        window,
        bg = "#C1C1C1",
        height = 900,
        width = 1600,
        bd = 0,
        highlightthickness=0,
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
        442.0,
        235.0,
        1396.0,
        291.0,
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

    canvas.create_text(
        479.0,
        244.0,
        anchor="nw",
        text="Sr.No",
        fill="#D9D9D9",
        font=("InriaSans Regular", 24 * -1)
    )

    canvas.create_text(
        611.0,
        244.0,
        anchor="nw",
        text="Date",
        fill="#D9D9D9",
        font=("InriaSans Regular", 24 * -1)
    )

    canvas.create_text(
        945.0,
        534.0,
        anchor="nw",
        text="Total",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    total_credit_text = canvas.create_text(
        1046.0,
        531.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    total_debit_text = canvas.create_text(
        1304.0,
        527.0,
        anchor="nw",
        text="0",
        fill="#000000",
        font=("InriaSans Regular", 24 * -1)
    )

    canvas.create_text(
        806.0,
        244.0,
        anchor="nw",
        text="Client",
        fill="#D9D9D9",
        font=("InriaSans Regular", 24 * -1)
    )

    canvas.create_text(
        1034.0,
        244.0,
        anchor="nw",
        text="Credit",
        fill="#D9D9D9",
        font=("InriaSans Regular", 24 * -1)
    )

    canvas.create_text(
        1268.0,
        244.0,
        anchor="nw",
        text="Debit",
        fill="#D9D9D9",
        font=("InriaSans Regular", 24 * -1)
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
        657.0,
        158.0,
        anchor="nw",
        text="Transactions History",
        fill="#000000",
        font=("InriaSans Regular", 36 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=add_transaction,
        relief="flat"
    )
    button_1.place(
        x=442.0,
        y=531.0,
        width=123.0,
        height=41.0
    )

    
    button_delete = Button(
        window,
        text="Delete Transaction",
        borderwidth=0,
        highlightthickness=0,
        command=delete_transaction_ui,
        relief="flat",
        bg="#FF0000",
        fg="#FFFFFF",
        font=("InriaSans Regular", 16)
    )
    
    button_delete.place(
        x=600.0,
        y=531.0,
        width=200.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=logout,
        relief="flat"
    )
    button_2.place(
        x=1436.0,
        y=60.0,
        width=117.62870788574219,
        height=51.54829025268555
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=go_home,
        relief="flat"
    )
    button_3.place(
        x=70.0,
        y=268.0,
        width=140.0,
        height=51.54829025268555
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=edit_profile,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=375.0,
        width=140.0,
        height=51.54829025268555
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=68.0,
        y=482.0,
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

    # Entry fields for transaction data
    entry_sr_no = Entry(window, bd=0, bg="#FFFFFF", highlightthickness=0)
    entry_sr_no.place(x=479, y=300, width=100, height=30)

    entry_date = Entry(window, bd=0, bg="#FFFFFF", highlightthickness=0)
    entry_date.place(x=611, y=300, width=100, height=30)

    entry_client = Entry(window, bd=0, bg="#FFFFFF", highlightthickness=0)
    entry_client.place(x=806, y=300, width=100, height=30)

    entry_amount = Entry(window, bd=0, bg="#FFFFFF", highlightthickness=0)
    entry_amount.place(x=1034, y=300, width=100, height=30)

    # New debit entry
    entry_debit = Entry(window, bd=0, bg="#FFFFFF", highlightthickness=0)
    entry_debit.place(x=1160, y=300, width=100, height=30)

    update_transaction_list()

    window.resizable(False, False)
    window.mainloop()
