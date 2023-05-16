from flask import render_template, request, redirect
from services.sessions_info import current_user
from models.review import new_review
def create_review(book_title):
    review = request.form.get('review')
    print(review)
    print(book_title)
    new_review(book_title,review)
    return redirect('/books')
  

    
  