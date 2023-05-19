-- sudo mysql -u root weblog < 20200304T184700-create_tables.sql

create table users (
  username VARCHAR(40) PRIMARY KEY,
  password BINARY(60) NOT NULL
);
