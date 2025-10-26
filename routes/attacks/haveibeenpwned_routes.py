from flask import Blueprint, request, jsonify
from utils.decorators import login_required
from services.attacks.haveibeenpwned_service import HaveIbeenPwned
from src.handlers.year_handler import current_year
from models.attack_model import get_all_attacks

pwned_bp = Blueprint("pwned", __name__, url_prefix="/pwned")


@pwned_bp.route("/check-password", methods=["POST"])
@login_required
def check_password():
    try:
        password = request.form.get("password", "").strip()

        if len(password) <= 0:
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": False,
                        "warning": "You should enter a value",
                    }
                ),
                400,
            )
        print("The password is: " + str(password))
        if HaveIbeenPwned(password):
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": True,
                        "warning": "You've been Pwned!!",
                    }
                ),
                200,
            )
        else:
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": True,
                        "message": "All clear!",
                    }
                ),
                200,
            )
    except Exception as e:
        return (
            jsonify({"source": "Attack Routes", "success": False, "error": str(e)}),
            500,
        )
