import sqlite3

def init_database():
    conn = sqlite3.connect('c:/Users/AW/Documents/SE/project/user_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            full_name TEXT
        )
    ''')

    sample_users = [
        ('user1', 'pass123', 'user1@example.com', 'John Doe'),
        ('user2', 'pass456', 'user2@example.com', 'Jane Smith'),
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO users (username, password, email, full_name)
        VALUES (?, ?, ?, ?)
    ''', sample_users)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()