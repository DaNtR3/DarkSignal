from flask import Blueprint, request, jsonify
from src.utils.decorators import login_required
from src.services.attacks.haveibeenpwned_service import HaveIbeenPwned
from src.metrics.metrics import haveIbeenPwned

pwned_bp = Blueprint("pwned", __name__, url_prefix="/pwned")


@pwned_bp.route("/check-password", methods=["POST"])
def check_password():
    try:
        password = request.form.get("password", "").strip()

        if len(password) <= 0:
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": False,
                        "warning": "Password field cannot be empty",
                    }
                ),
                400,
            )
        found, count = HaveIbeenPwned(password)
        if found:
            haveIbeenPwned.add(1, {"result": "You've been Pwned!! Consider using a stronger password next time : )"})
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": True,
                        "warning": "You've been Pwned!!",
                        "count": count
                    }
                ),
                200,
            )
        else:
            haveIbeenPwned.add(1, {"result": "All clear!.  Your password looks strong!"})
            return (
                jsonify(
                    {
                        "source": "Attack Routes",
                        "success": True,
                        "message": "All clear!",
                        "count": count
                    }
                ),
                200,
            )
    except Exception as e:
        return (
            jsonify({"source": "Attack Routes", "success": False, "error": str(e)}),
            500,
        )
