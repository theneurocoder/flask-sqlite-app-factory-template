from app.db import get_connection


def init_tables():
   
    conn = get_connection()
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT
        )
        """
    )

    conn.commit()
    conn.close()
