# view.py
from flask import Blueprint

view_bp = Blueprint('view', __name__)

@view_bp.route("/")
def home():
    return "This is the home page"
