# Exercise 3: A Weblog

10 points

**DUE: Friday, April 12 by 5:00pm**

### Instructions

One very common kind database-driven web application is a Content Management
System, or CMS. A CMS provides an interface for users to write content—posts,
articles, whole web pages—that is stored in a database, and then creates web
pages from those entries, without the author needing to know any HTML.

We're going to make our own very simple CMS for a web journal, with posts and
comments. The assignment this week is to modify the `.py` files in `exercise_3`
to make the pages display posts and comments that are stored in a database, and
to enable users to create new posts and leave new comments.

The LAMP stack is still free and still powerful, but it can be harder to get running on your laptops than some alternatives. Instead we're going to use Python as our server-side language. It's widely used both in application development and in scientific computing, and it has some things we'll need already built-in. So first, install the latest stable version of Python from https://www.python.org/.

From the root our your exercise directory (ie this one), start your server with:

`python3 weblog.py`

You should be able to see your pages at e.g. http://localhost:8000/

From there:
1. You can connect to the SQLite3 database in `db/weblog.sqlite3`. It has
  already been set up to have tables for posts and comments by running the
  commands in `create_tables.sql`.
1. Modify `weblog.py` to fetch posts and their associated comments from the
    database and display them to visitors, and modify index_page.py to render the 
    posts and comments retreived from the database
    - Use no more than two queries to get the existing posts and their comments
      (note: it is possible to do this in one query).
    - Display posts in reverse chronological order. That is, with the newest
      (highest id) posts at the top. Display Comments in chronological order from
      lowest id to highest.
    - Put the `id` of posts in the appropriate HTML attributes to enable
      linking to individual posts on the page and to comment pages for each post.
    - When displaying user-entered information like titles, posts, or usernames, use
      the [html.escape](https://docs.python.org/3/library/html.html#html.escape)
      function to make sure special characters like < and > render correctly in HTML.
    - Replace `<yourname>` with your name.
1. Modify `weblog.py` to insert a new row in the `posts` table in response to an 
    appropriate POST message.
    - Be sure to add a secret password in the your code, and only add a row if the
      password the user entered matches! For ease in grading, use the password `phil`
    - Make the id of each post in the database the `id` attribute on your
      `<post>` elements, like in 
      https://github.com/UChicagoWebDev/private_exercise_3/blob/main/index_page.py#L23.
      Update the anchor tag in the h2 of the post to link to the 
      [fragment dentifier](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#anchor),
      like in https://github.com/UChicagoWebDev/private_exercise_3/blob/main/index_page.py#L26. 
      That makes it so opening the link in a post's h2 opens the page to the index and
      scrolls to that post. For example, https://uchicagowebdev.com/examples/week_3/weblog.html#1 
      opens the page scrolled down to "Sonnet 2."
    - Because we're accepting content from users, be sure to
      [sanitize your inputs](https://xkcd.com/327/) using placeholders to form the insert
      statements rather than creating queries with string concatenation.
      https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries.
1. Modify `weblog.py` to enable users to leave comments on posts, and modify 
  `leave_comment.py` to display the post the user is commenting on and any previous comments.
    - We'll get a `post_id` as a query param. Fetch the post and any existing
      comments from the database in a single query (you'll have to use a `JOIN`).
    - We'll let any users post comments without authentication. It's become clear
      that's a bad idea on the real internet, but it's fine for this exercise.
    - When a user posts a new comment, add a new row to the `comments` table,
      sanitizing as before.

Don't worry about mobile layouts for this exercise, about or about features like
previewing or editing.

Remember to include in your submission any classmates you collaborated with and
any materials you consulted.

### Rubric

One point each for:
- Replace `<yourname>` with your name in the index, post, and comment pages
- Uses one SELECT query with a JOIN to fetch a post and any of its
  comments for the leave_comment page.
- Uses no more than two queries to fetch all the posts and all their comments
  for the main page each time it is loaded. (It's possible to do this in one 
  query, though it does make looping over the results more complicated).
- Server-side rendering: Correctly builds main page from fetched data: loops to
  write Post and Comment divs. Displays newest Posts at the top, and Comments in
  chronological order, oldest at the top and newest at the bottom. Posts have
  links in their h2 that scroll to that post.
- Correctly builds the comment page, displaying the text of the post,
  and other comments posted so far in the thread.
- Form submission: Correctly handles POSTing new posts and comments and parses
  them out of the form data.
- INSERT: Correctly inserts posted comments and posts to the database. Comments
  have the correct relationship to posts.
- Escaping: Correctly uses `html.escape` when rendering the content of posts
  and comments, which are usedr-generated.
- Correctly sanitizes user-provided data for posts by binding values to prepared 
  placeholders.
- Correctly sanitized user-provided data for comments by binding values to prepared 
  placeholders.
