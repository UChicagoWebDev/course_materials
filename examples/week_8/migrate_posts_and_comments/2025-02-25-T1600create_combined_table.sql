
-- create table posts (
--   id INTEGER PRIMARY KEY,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT
-- );
-- create table comments (
--   id INTEGER PRIMARY KEY,
--   post_id INTEGER,
--   body TEXT,
--   author VARCHAR(30),
--   FOREIGN KEY(post_id) REFERENCES posts(id)
-- );

create table posts_and_comments (
  id INTEGER PRIMARY KEY,
  old_post_id INTEGER,
  slug VARCHAR(30),
  title VARCHAR(255),
  body TEXT,
  comments_on_post_id INTEGER,
  author VARCHAR(30),
  FOREIGN KEY(comments_on_post_id) REFERENCES posts_and_comments(id)
);