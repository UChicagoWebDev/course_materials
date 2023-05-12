-- create table posts (
--   id INTEGER PRIMARY KEY,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT
-- );
--
-- create table comments (
--   id INTEGER PRIMARY KEY,
--   post_id INT,
--   body TEXT,
--   author VARCHAR(30),
--   FOREIGN KEY(post_id) REFERENCES posts(id)
-- );

create table posts_and_comments (
  id INTEGER PRIMARY KEY,
  slug VARCHAR(30),
  title VARCHAR(255),
  body TEXT,
  post_id INTEGER,
  author VARCHAR(30)
);
