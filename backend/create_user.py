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
        # (5, 'moderator', 'pass@123', 'moderator@gmail.com', 5),
        (6, 'student2', 'pass@123', 'student2@gmail.com',1),
        # (1, 'piyush', 'piyush@1234', 'agrawalpiyushjpr8@gmail.com', 1),
        # (2, 'puravasu', 'puravasu@1234', 'puravasu@gmail.com', 1),
        # (3, 'abhay', 'abhay@1234', 'abhay@gmail.com', 1),
        # (4, 'harshil', 'harshil@1234', 'harshil@gmail.com', 1),
        # (5, 'khushee', 'khushee@1234', 'khusheenamdeo@gmail.com', 1),
        # (6, 'jigyasa', 'jigyasa@1234', 'jigyasa@gmail.com', 1),
        # (7, 'dhruv', 'dhruv@1234', 'dhruv@gmail.com', 1),
        # (8, 'suppor_agent', 'pass@1234', 'support@gmail.com', 2),
        # (9, 'admin_user', 'pass@1234', 'admin@gmail.com', 3),
        # (10, 'manager', 'pass@1234', 'manager@gmail.com', 4),
        # (11, 'moderator', 'pass@1234', 'moderator@gmail.com', 5)
    ]

    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Drop the users table if it exists
    cursor.execute('''DROP TABLE IF EXISTS user''')

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
