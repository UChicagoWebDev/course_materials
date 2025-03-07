
-- create table posts (
--   id INTEGER PRIMARY KEY,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT
-- );

-- create table posts_and_comments (
--   id INTEGER PRIMARY KEY,
--   old_post_id INTEGER,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT,
--   comments_on_post_id INTEGER,
--   author VARCHAR(30),
--   FOREIGN KEY(comments_on_post_id) REFERENCES (id)
--     -- TODO
-- )

insert into posts_and_comments 
    (old_post_id, slug, title, body)
    select id, slug, title, body from posts;