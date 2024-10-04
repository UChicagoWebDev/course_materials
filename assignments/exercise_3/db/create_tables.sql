create table posts (
  id INTEGER PRIMARY KEY,
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
