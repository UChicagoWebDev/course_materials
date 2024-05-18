insert into posts_and_comments (
    parent_post_id,
    body,
    author
) select post_id, body, author from comments;