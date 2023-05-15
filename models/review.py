from db.db import sql
def new_review(book_title,review):
  sql('INSERT INTO reviews(book_title,review) VALUES(%s, %s) RETURNING *', [book_title,review])

def get_reviews(title):
  reviews= sql('SELECT * FROM reviews WHERE book_title =%s',[title])
  print(reviews)
  return reviews
