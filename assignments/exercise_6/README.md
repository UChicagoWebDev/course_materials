# Exercise #6: Watch Party 2: The Single Page Experience

10 points

**DUE: Friday, May 3 by 5:00pm**

### Instructions

For this exercise, we will build a _single-page_ group chat web application with
asynchronous Javascript and a REST API written in Python with Flask.

Like the original, Watch Party 2 lets users start group chats and invite their
friends. This time, however, we serve a single static HTML page and never
redirect or reload. Instead, the page interacts purely with the JSON API.

Starting with the files included in this directory, implement the UI for Watch
Party in HTML, CSS, and Javascript, and serve it using server-side code written
in the
[latest stable version of Python](https://www.python.org/downloads/release/python-3112/)
([3.11.2](https://www.python.org/downloads/release/python-3112/)) and
[Flask](https://flask.palletsprojects.com/en/2.2.x/installation/). Routes to
serve the static content are provided, so you will only need to implement the
API endpoints in `app.py` and the javascript in `script.js`. You are however
free to modify any other file if it makes development more convenient.

You may re-use any code from your Exercise 5. Remember to include in the README
of your submission any classmates you collaborated with and any materials you 
consulted.

### Rubric

One point each for:

- One-click signup creates a new user in the database and returns an API key for
  that user. Store the API key in the user's browser, so that it is available
  across tabs and if the browser window is closed and reopened. A javascript
  logout function removes the API key from where it is stored on the user's
  browser and reloads the page.
- Login API endpoint that accepts a username and password (either in the headers
  or request body, but **not** in the URL) and returns the API key for that
  user. All other API endpoints require a valid API key.
- Make all HTTP requests after the page load with `fetch` calls to API endpoints
  that return JSON. Prefix API routes with `/api`.
- Users can update their name and password, create and rename rooms, and post
  messages. Replace every double curly brace `{{}}` in `index.html` with values 
  set by your `script.js`. HINT: For curly braces inside a block of text, it may 
  be helpful to wrap them in a `<span>` first.
- Visiting a screen pushes its URL to the navigation bar and the browser
  history. Rooms have their own unique URLs.
- Opening `/`, `/login`, or `/profile` in a new browser window opens the app to
  those screens.
- Opening the url for a room opens the app to that room. You may choose to
  encode the room id in whichever part of the URL makes the most sense to you.
- Opening a url while logged out loads the login page, and then returns the user
  to that url after they log in.
- Users can use the browser Back and Forward buttons to navigate the app.
- While in a room, poll the API every 0.5 seconds for new messages. Stop polling
  after the user leaves a room.
