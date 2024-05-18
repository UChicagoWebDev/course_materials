insert into posts_and_comments(
    old_post_id,
    slug,
    title,
    body
)  select id, slug, title, body from posts;