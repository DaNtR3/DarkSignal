from flask import (
    Blueprint,
    render_template,
)
from src.utils.decorators import login_required
from src.handlers.year_handler import current_year
from src.models.attack_model import get_all_attacks


home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/", methods=["GET"])
@login_required
def homepage():
    attacks = get_all_attacks()
    return render_template('home_page.html', custom_css='css/styles_main.css', current_year=current_year(), attacks=attacks)