from flask import Blueprint
from controllers.reviews_controller import create_review


reviews_routes = Blueprint('reviews_routes', __name__)

reviews_routes.route('/create_review/<book_title>', methods=['POST'])(create_review)


