from flask import Blueprint
from controllers.books_controller import index, new, create, edit, update, delete

books_routes = Blueprint('books_routes', __name__)

books_routes.route('')(index)
books_routes.route('/new')(new)
books_routes.route('', methods=['POST'])(create)
books_routes.route('/<id>/edit')(edit)
books_routes.route('/<id>', methods=["POST"])(update)
books_routes.route('/<id>/delete', methods=["POST"])(delete)