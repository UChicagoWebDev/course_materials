-- sqlite3 weblog.sqlite3 < 20200224T184700-create_tables.sql

create table posts (
  id INTEGER PRIMARY KEY,
  slug VARCHAR(30) NOT NULL,
  title VARCHAR(255) NOT NULL,
  body TEXT
);

create table comments (
  id INTEGER PRIMARY KEY,
  post_id INTEGER,
  body TEXT,
  author VARCHAR(30),
  FOREIGN KEY(post_id) REFERENCES posts(id)
);