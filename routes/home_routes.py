from flask import (
    Blueprint,
    render_template,
)
from utils.decorators import login_required
from src.handlers.year_handler import current_year


home_bp = Blueprint("home", __name__, url_prefix="/home")


@home_bp.route("/", methods=["GET"])
@login_required
def homepage():
    return render_template('home_page.html', custom_css='css/styles_main.css', current_year=current_year())
