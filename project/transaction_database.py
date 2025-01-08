import sqlite3

def initialize_transactions():
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/transaction_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            sr_no INTEGER,
            date TEXT,
            client TEXT,
            amount REAL,
            debit REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_transaction(username, sr_no, date, client, amount, debit):
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/transaction_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (username, sr_no, date, client, amount, debit)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (username, sr_no, date, client, amount, debit))
    conn.commit()
    conn.close()

def fetch_transactions(username):
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/transaction_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT sr_no, date, client, amount, debit FROM transactions WHERE username=?", (username,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def delete_transaction(username, sr_no):
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/transaction_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM transactions WHERE username=? AND sr_no=?
    ''', (username, sr_no))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_transactions()
