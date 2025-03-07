-- create table comments (
--   id INTEGER PRIMARY KEY,
--   post_id INTEGER,
--   body TEXT,
--   author VARCHAR(30),
--   FOREIGN KEY(post_id) REFERENCES posts(id)
-- );

-- create table posts_and_comments (
--   id INTEGER PRIMARY KEY,
--   old_post_id INTEGER,
--   slug VARCHAR(30) NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   body TEXT,
--   comments_on_post_id INTEGER,
--   author VARCHAR(30),
--   FOREIGN KEY(comments_on_post_id) REFERENCES posts_and_comments(id)
-- );

insert into posts_and_comments 
    (comments_on_post_id, body, author)
    select p.id, c.body, c.author from 
        comments c left join posts_and_comments p on c.post_id = p.old_post_id;