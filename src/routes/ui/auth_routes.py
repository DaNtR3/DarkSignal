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
from src.services.auth_service import AuthService, ActiveSession
from src.utils.decorators import login_required
from src.handlers.year_handler import current_year
from src.metrics.metrics import auth_failures
from src.metrics.metrics import auth_success
from src.metrics.metrics import auth_logout

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/session", methods=["GET"])
@login_required
def authenticate():
    return redirect(url_for("home.homepage"))


@auth_bp.route("/logout", methods=["POST"])
def logout():
    auth_logout.add(1, {"username": session['user'], "event": "Logged out successfully!"})
    session.clear()
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    try:
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if request.method == "POST":
            if AuthService(username, password):
                auth_success.add(1, {"username": username, "reason": "Logged in successfully!"})
                return redirect(url_for("home.homepage"))
            else:
                auth_failures.add(1, {"username": username, "reason": "Invalid_credentials"})
                return jsonify({"source":"Auth Routes" ,"success": False, "message": "Invalid credentials"}), 401
        elif request.method == "GET":
            if not ActiveSession():
                return render_template(
                    "login.html",
                    custom_css="css/styles_login.css",
                    current_year=current_year(),
                )
            else:
                auth_success.add(1, {"username": session['user'], "reason": "User is already logged in!"})
                return redirect(url_for("home.homepage"))
    except Exception as e:
        return jsonify({"source":"Auth Routes","success": False, "error": str(e)}), 500
