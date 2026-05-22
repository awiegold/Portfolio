import sqlite3
from itertools import groupby


class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Return rows like dictionaries
        return conn

    # Add a new message to the database
    def add_message(self, name, message):
        with self.get_connection() as conn:
            conn.execute(
                "INSERT INTO messages (name, message) VALUES (?, ?)",
                (name, message)
            )
            conn.commit()  # Save changes

    # Get all messages (newest first)
    def get_messages(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM messages ORDER BY id DESC"
            )
            return cursor.fetchall()
        
    def delete_message(self, id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM messages WHERE id = ?", (id,))
            conn.commit()

    def get_message(self, id):
        with self.get_connection() as conn:
            return conn.execute("SELECT * FROM messages WHERE id = ?", (id,)).fetchone()

    def update_message(self, id, message):
        with self.get_connection() as conn:
            conn.execute("UPDATE messages SET message = ? WHERE id = ?", (message, id))
            conn.commit()