create table posts_and_comments (
    id INTEGER PRIMARY KEY,
    old_post_id INTEGER,
    parent_post_id INTEGER,
    slug VARCHAR(30),
    title VARCHAR(255) NOT NULL,
    body TEXT,
    author VARCHAR(30)
);

