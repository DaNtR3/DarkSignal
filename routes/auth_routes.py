# auth routes for handling authentication

from flask import (
    Blueprint,
    request,
    jsonify,
    session,
    redirect,
    url_for,
    render_template,
)
from services.auth_service import AuthService, ActiveSession
from utils.decorators import login_required
from src.handlers.year_handler import current_year

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/session", methods=["GET"])
@login_required
def authenticate():
    return redirect(url_for("home.homepage"))


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "").strip()
            if AuthService(username, password):
                return redirect(url_for("home.homepage"))
            else:
                return jsonify({"source":"Auth Routes" ,"success": False, "error": "Invalid credentials"}), 401
        elif request.method == "GET":
            if not ActiveSession():
                return render_template(
                    "login.html",
                    custom_css="css/styles_login.css",
                    current_year=current_year(),
                )
            else:
                return redirect(url_for("home.homepage"))
    except Exception as e:
        return jsonify({"source":"Auth Routes","success": False, "error": str(e)}), 500
