from flask import Blueprint, render_template, jsonify
from utils.decorators import login_required
from src.handlers.year_handler import current_year
from models.attack_model import get_attack_by_id
from models.mapping.attack_mapping import template_map

PAGE_404 = "404.html"
PAGE_404_CSS = "css/styles_404.css"
PAGE_FOUND_CSS = "css/styles_main.css"

attack_bp = Blueprint("attacks", __name__, url_prefix="/attacks")


@attack_bp.route("/<attack_id>", methods=["GET"])
@login_required
def renderAttack(attack_id):
    css_style = PAGE_404_CSS
    try:
        if not attack_id.isdigit() or len(attack_id) > 1:
            return render_template(PAGE_404, custom_css=css_style)
        attack_by_id = get_attack_by_id(attack_id)
        if not attack_by_id:
            return render_template(PAGE_404, custom_css=css_style)
        # Choose html template based on attack name
        template = template_map.get(attack_by_id[1], PAGE_404)
        if template != PAGE_404:
            css_style = PAGE_FOUND_CSS
        return render_template(
            template,
            custom_css=css_style,
            attack=attack_by_id,
            current_year=current_year(),
        )
    except Exception as e:
        return (
            jsonify({"source": "Attack Router", "success": False, "error": str(e)}),
            500,
        )
