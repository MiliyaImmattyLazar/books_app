CREATE DATABASE books_app_db;
\c books_app_db
CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title TEXT,
  image_url TEXT,
  author_name TEXT,
  published_year INTEGER

);
INSERT INTO books(title, image_url,author_name,published_year)
VALUES ('Harry Potter','https://images.ctfassets.net/usf1vwtuqyxm/3d9kpFpwHyjACq8H3EU6ra/85673f9e660407e5e4481b1825968043/English_Harry_Potter_4_Epub_9781781105672.jpg?w=914&q=70&fm=jpg','J.K Rowling','2000'),
('Lord of the rings','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1566425108l/33.jpg','J.R.R.Tolkein','1995'),
('Origin','https://www.booktopia.com.au/covers/big/9780552174169/0000/origin.jpg','Dan Brown','2017'),
('The shadow of the gods','https://www.hachette.co.uk/wp-content/uploads/2021/07/Shadow-of-the-Gods.jpg?w=1024','John Gwynne','2022'),
('Wings of fire','https://www.booktopia.com.au/covers/600/9789386235039/0503/wings-of-fire.jpg','APJ Abdul kalam','1999'),
('The da vinci code','https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F6%2F2018%2F08%2Fbrown3-2000.jpg','Dan brown','2003'),
('Two states','https://upload.wikimedia.org/wikipedia/en/3/3a/2_States_-_The_Story_Of_My_Marriage.jpg','chetan bhagath','2009'),('Dracula','https://images.thenile.io/r1000/9781847494870.jpg','Bram stoker','1897'),('The Fall Of Numenor','https://pictures.abebooks.com/isbn/9780001054905-us.jpg','JRR Tolkein','2022')('Dreams from my father','https://m.media-amazon.com/images/I/416pN5qvDWL._SX323_BO1,204,203,200_.jpg','Barak Obama','1995');


CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);
CREATE TABLE reviews(
  id SERIAL PRIMARY KEY,
  book_title TEXT,
  review TEXT);
  


  

