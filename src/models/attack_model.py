from flask import jsonify
from src.db_conn import get_db_connection


def get_all_attacks():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description, img_url FROM attacks")
        rows = cursor.fetchall()
        return rows


def get_attack_by_id(attack_id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, description, img_url FROM attacks WHERE id = ?",
            (attack_id),
        )
        return cursor.fetchone()
