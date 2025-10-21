from flask import jsonify
from db_conn import get_db_connection


def get_all_attacks():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, description, img_url FROM attacks")
        rows = cursor.fetchall()
        return rows