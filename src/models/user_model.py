from flask import jsonify
from src.db_conn import get_db_connection


def get_user_by_username(username):
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT
                        u.username,
                        u.password,
                        u.active,
                        u.locked,
                        r.name AS 'role_name'
                    FROM
                        users u
                        INNER JOIN roles r ON r.id = u.permission_id
                    WHERE
                        u.username = ?""",
                (username,),
            )
        return cursor.fetchone()
    except Exception as e:
        return jsonify({"source":"User Model","success": False, "error": str(e)}), 500
    
    
