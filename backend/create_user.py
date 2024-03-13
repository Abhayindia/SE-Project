import sqlite3
import os

# Define the database file path
db_file = os.path.join('db_directory', 'testdb.sqlite3')

# Function to recreate the users table and insert data
def recreate_users_table():
    # User data
    users_data = [
        # (1, 'student', 'pass@123', 'student@gmail.com', 1),
        # (2, 'suppor_agent', 'pass@123', 'support@gmail.com', 2),
        # (3, 'admin_user', 'pass@123', 'admin@gmail.com', 3),
        # (4, 'manager', 'pass@123', 'manager@gmail.com', 4),
        (5, 'moderator', 'pass@123', 'moderator@gmail.com', 5),
    ]

    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Drop the users table if it exists
    cursor.execute('''DROP TABLE IF EXISTS users''')

    # Create the users table
    # cursor.execute('''CREATE TABLE user (
    #                     user_id INTEGER PRIMARY KEY,
    #                     user_name TEXT NOT NULL,
    #                     password TEXT NOT NULL,
    #                     email_id TEXT NOT NULL,
    #                     role_id INTEGER NOT NULL
    #                 )''')

    # Insert users data into the table
    cursor.executemany('''INSERT INTO user (user_id, user_name, password, email_id, role_id)
                          VALUES (?, ?, ?, ?, ?)''', users_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Execute the function to recreate the users table and insert data
recreate_users_table()
print("Users table recreated successfully.")
