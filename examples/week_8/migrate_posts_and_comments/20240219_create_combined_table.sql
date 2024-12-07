create table posts_and_comments (
    id INTEGER PRIMARY KEY,
    original_post_id INTEGER,
    original_comment_id INTEGER,
    comments_on_post_id INTEGER,
    slug VARCHAR(30) NOT NULL,
    title VARCHAR(255) NOT NULL,
    body TEXT,
      author VARCHAR(30)
)