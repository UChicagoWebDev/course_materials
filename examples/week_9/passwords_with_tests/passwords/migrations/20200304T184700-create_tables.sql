drop table if exists users;

create table users (
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL
);
