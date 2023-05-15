from db.db import sql

def all_books():
  return sql('SELECT * FROM books ORDER BY id')

def get_book(id):
  books = sql("SELECT * FROM books WHERE id = %s", [id])
  return books[0]

def create_book(title, image_url,author_name,published_year):
  sql('INSERT INTO books(title, image_url,author_name,published_year) VALUES(%s, %s,%s, %s) RETURNING *', [title, image_url,author_name,published_year])

def update_book(id, title, image_url,author_name,published_year):
  sql('UPDATE books SET title=%s, image_url=%s ,author_name=%s,published_year=%s WHERE id=%s RETURNING *', [title, image_url,author_name,published_year, id])

def delete_book(id):
  sql('DELETE FROM books WHERE id=%s RETURNING *', [id])

def title_book(title):
  books = sql("SELECT * FROM books WHERE title= %s", [title])
  return books[0]

