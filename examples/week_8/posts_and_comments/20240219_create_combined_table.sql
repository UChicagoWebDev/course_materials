create table posts_and_comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER,
    is_post BOOLEAN,
    body TEXT,
    slug VARCHAR(30),
    title VARCHAR(30),
    author VARCHAR(30)
)