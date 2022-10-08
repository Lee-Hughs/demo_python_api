import psycopg2
import os

class DatabaseConnection(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv("DB_NAME"),
            user=os.getenv("PG_USERNAME"),
            password=os.getenv("PG_PASSWORD")
        )
    def __enter__(self):
        return self
    def __exit__(self):
        self.conn.close()
    def get_item_by_id(self, id):
        cur = self.conn.cursor()
        cur.execute(
        """
        SELECT * FROM items WHERE item_id=%s
        """,
        (id)
        )
        result = cur.fetchone()
        cur.close()
        return result