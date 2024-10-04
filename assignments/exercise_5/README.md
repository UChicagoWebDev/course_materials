# Exercise #5: Watch Party

10 points

**DUE: Friday, April 26 by 5:00pm**

### Instructions

For this exercise, we will build a group chat web application with asynchronous
Javascript and a REST API written in Python with Flask. Watch Party is a public
group chat program. You have here a skeleton of the app, including signup, login,
and logout flows. Take the Watch Party UI here and serve it using server-side code
written in the [latest stable version of Python](https://www.python.org/downloads/)
and the [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/) web
application framework. You may want to read the
[Flask Quickstart Guide](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

Launch the app by running `flask run` on the command line from your Exercise 5
directory. I recommend running `flask run --reload --debug`, which will make the server
automatically load changes to your files.

Your task will be to implement a REST API for some of the Watch Party's functions,
and client-side Javascript code that consumes that API. Though the exercise is
designed to only require changes to `script.js` and `app.py`, you may make any
adjustments to any other files you feel would be helpful.

Remember to include in your submission any classmates you collaborated with and
any materials you consulted. Watch Party (though it has somewhat different
requirements) is inspired by [yap.chat](https://yap.chat/).

### Rubric

- `room.html` currently has a number of dummy messages to demonstrate styling.
  Implement an API endpoint that accepts and returns JSON and that returns all the
  messages in a chat room. [1 point]
- API endpoints require a valid API key in the request header. They do not use
  username/password, and they do not send the API key in the request body. [1 point]
- Write Javascript code that uses `fetch` to retrieve that list of messages. [1 point]
- When a chat room page first loads, clear any sample messages out of the chat
  histoy. [1 point]
- Create HTML elements for the messages retreived from the API using
  `document.createElement`. Do not write HTML strings. [1 point]
- While in a room, check the messages endpoint every 100 ms and add any new messages
  to the chat history. [1 point]
- Implement an API endpoint to allow users to post messages in a chat room. On all
  queries, pass variable parts to the SQL statement by using a question mark in the
  statement and pass in the arguments as a list,
  [as described in the Flask docs](https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/#:~:text=To%20pass%20variable%20parts%20to%20the%20SQL%20statement%2C%20use%20a%20question%20mark%20in%20the%20statement%20and%20pass%20in%20the%20arguments%20as%20a%20list.%20Never%20directly%20add%20them%20to%20the%20SQL%20statement%20with%20string%20formatting%20because%20this%20makes%20it%20possible%20to%20attack%20the%20application%20using%20SQL%20Injections.)
  [1 point]
- Default usernames, passwords, and room names are set automatically. Implement
  three API endpoints that accept and return JSON and that allow a user to change their
  username, their password, and the name of the room they are in. [1 point]
- Javascript code that uses `fetch` to allow a user to update their username or
  password without reloading the page. [1 point]
- Javascript code to show/hide the room name edit UI and uses `fetch` to allow a user
  to update the name of a room without reloading the page. [1 point]
