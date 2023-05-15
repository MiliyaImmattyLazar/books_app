from flask import render_template, request, redirect
from models.book import all_books, get_book, create_book, update_book, delete_book,title_book
from models.review import get_reviews
from services.sessions_info import current_user

def index():
  books = all_books()
  return render_template('books/index.html', books=books, current_user=current_user)
def title(title):
  book = title_book(title)
  reviews= get_reviews(title)
  return render_template('books/title.html', book=book ,reviews=reviews)

def new():
  return render_template('books/new.html')


def create():
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  author_name = request.form.get('author_name')
  published_year = request.form.get('published_year')
  create_book(title, image_url,author_name,published_year)
  return redirect('/')

def edit(id):
  book = get_book(id)
  return render_template('books/edit.html', book=book)

def update(id):
  title = request.form.get('title')
  image_url = request.form.get('image_url')
  author_name = request.form.get('author_name')
  published_year = request.form.get('published_year')
  update_book(id,title, image_url,author_name,published_year)
  return redirect('/')

def delete(id):
  delete_book(id)
  return redirect('/')




  


  