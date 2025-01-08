from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from transaction_database import fetch_transactions
import pandas as pd
from fpdf import FPDF

# Ensure openpyxl is installed
try:
    import openpyxl
except ImportError:
    os.system('pip install openpyxl')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("reports/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_login.py"')

def go_home():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_dashboard.py"')

def go_transactions():
    window.destroy()
    os.system('python "c:/Users/AW/Documents/SE/project/admin_transaction.py"')

def download_excel():
    transactions = fetch_transactions(username)
    df = pd.DataFrame(transactions, columns=["Sr.No", "Date", "Client", "Amount", "Debit"])
    file_path = Path.home() / "Desktop" / "transactions.xlsx"
    df.to_excel(file_path, index=False)
    messagebox.showinfo("Success", f"Excel file saved to {file_path}")

def download_pdf():
    transactions = fetch_transactions(username)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Transaction Report", ln=True, align="C")
    pdf.ln(10)
    for transaction in transactions:
        pdf.cell(200, 10, txt=str(transaction), ln=True)
    file_path = Path.home() / "Desktop" / "transactions.pdf"
    pdf.output(str(file_path))
    messagebox.showinfo("Success", f"PDF file saved to {file_path}")

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
    721.0,
    157.0,
    anchor="nw",
    text="REPORTS",
    fill="#000000",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    363.0,
    252.0,
    anchor="nw",
    text="Generate reports",
    fill="#000000",
    font=("InriaSans Regular", 40 * -1)
)

canvas.create_text(
    664.0,
    38.0,
    anchor="nw",
    text="Admin Dashboard",
    fill="#FFFFFF",
    font=("InriaSans Regular", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_1.place(
    x=1436.0,
    y=60.0,
    width=117.62870788574219,
    height=51.54829025268555
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=download_excel,
    relief="flat"
)
button_2.place(
    x=656.0,
    y=360.0,
    width=98.93389892578125,
    height=51.54829025268555
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=download_pdf,
    relief="flat"
)
button_3.place(
    x=363.0,
    y=360.0,
    width=98.93389892578125,
    height=51.54829025268555
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=go_home,
    relief="flat"
)
button_4.place(
    x=70.0,
    y=268.0,
    width=140.0,
    height=51.54829025268555
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=go_transactions,
    relief="flat"
)
button_5.place(
    x=69.0,
    y=375.0,
    width=140.0,
    height=51.54829025268555
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=print("button_7 clicked"),
    relief="flat"
)
button_6.place(
    x=68.0,
    y=482.0,
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
    587.0,
    230.0,
    1014.0,
    231.0,
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

# Define the username variable
username = "user"  # Replace with the actual username if needed

window.mainloop()
