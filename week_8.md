class: center, middle

# MPCS 52553: Web Development
## Week 8: React Classes and Database Migrations \[WIP\]

---

class: agenda

# Database Migrations

- Configuration as Code
- Migrating Safely
- Lab: Posts and Comments

# React Classes

- Thinking in React
- Conditional Rendering
- Lab: Login and Post
- Type Checking
- Lab: Login and Post

---

# Database Migrations

A database is a critical part of most modern web applications, and the way that
database is structured is a critical part of their design. And as database
software has gotten more mature, larger and larger teams have moved away from
having dedicated database administrators (DBAs) and towards putting the database
under the control of web application engineers.

(There are more DBAs then ever
[BLS Statistics](https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm#tab-1),
but they tend to work on bigger databases, which are of course now bigger then
ever)

---

# Database Migrations

Rather than defining tables or modifying their structure by hand, the best
practice is to write code that performs the transformations and check it into
version control. This code is commonly called a **database migration**.

Writing the transformations out and committing them to version control has a
number of advantages:

- It's easy to discover what the state of the database is or should be
- The application code and database configuration are all in one place, making
  it easier to be sure they stay in sync
- It's easier to restore a damaged database, or make a new copy for staging or
  development work, because you have the code that created it
- It's easier to do collaborative review of database changes, through the
  regular code review process

https://martinfowler.com/articles/evodb.html

---

# Migrating Safely

Application code that tries to reference tables that aren't there will throw an
error.

Database tables that aren't referenced by any application code sit there
harmlessly.

So for **creating** a table, you have to make the database changes first, then
the application code changes.

For **dropping** a table, you have to make the application code changes first.

We preface our migrations with an
[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) date and time so that their
lexical order is the same as the order they are meant to be run in.

---

# Migrating Safely

Sometimes you'll be able to make these changes all at once. You'll schedule a
downtime window, make the changes to the database and the application code
together, restart the servers and be on your way.

But sometimes, especially in web development, you may not be able to schedule
downtime. You may have to carefully sequence your changes so that they can be
deployed without needing to turn the servers off. So to change the way a table
is structured you might need to:

1. Create the new table structure
1. Deploy a change to the application code to write to the new **and** the old
   tables
1. Copy over the historical data from the old table to the new one
1. Change the application code to read from the new table and stop writing to
   the old one
1. Drop the old table

## https://firstround.com/review/shims-jigs-and-other-woodworking-concepts-to-conquer-technical-debt/

---

# Lab: Posts and Comments

In the `/examples` directory we have SQL migrations to create the posts and
comments tables from Exercise 3, and to insert some sample data. Let's say we
want to add a new feature where users (with some `user_id`) can `like` posts and
comments.

--

So we know we'll need a `likes` table. We could let it link to posts and
comments separately with `post_id` and `comment_id` columns. But maybe thinking
about likes makes us realize the posts and comments have lots of behaviors in
common, and should really be modeled as one table.

--

## How would we do that migration?

---

# React Classes

https://beta.reactjs.org/learn/sharing-state-between-components

https://beta.reactjs.org/learn/thinking-in-react

## https://beta.reactjs.org/learn/conditional-rendering

---

# Lab: Login and Post

In the `/examples` directory we have a simple single-page application that is
doing a lot of showing and hiding of page elements manually, and has the
application state spread over several components. Let's lift the state up to the
top component and use conditional formatting to let React manage the display for
us.

---

# Type Checking

https://reactjs.org/docs/typechecking-with-proptypes.html

https://www.npmjs.com/package/prop-types

## https://www.typescriptlang.org/

# Lab: Login and Post

The Journal app already has some rudimentary type checking for the Posts
component, let's expand it to check that every Post has an id, a title, and a
post body.
