-- create table posts_and_comments (
--   id INT PRIMARY KEY,
--   title VARCHAR(255),
--   slug VARCHAR(30),
--   body TEXT,
--   author VARCHAR(30),
--   post_id INTEGER
-- );

-- migrate the posts first

insert into posts_and_comments (id, title, slug, body, author, post_id)
  select id, title, slug, body, NULL, NULL from posts;

insert into posts_and_comments (body, author, post_id)
  select body, author, post_id from comments;


select 
  id, slug, comment_count
  from posts_and_comments p 
  left join
  (select post_id, count(*) as comment_count from posts_and_comments group by post_id) c
  where p.post_id is null 
  and p.id = c.post_id;