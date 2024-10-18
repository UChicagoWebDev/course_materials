insert into posts_and_comments
(post_id,
is_post,
body,
author)
VALUES
    select post_id,
    0,
    body,
    author
    from comments;