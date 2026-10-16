# lab-3

We have a tiny web server built on Python's low-level HTTP library. Run it with:

`python tiny_server.py`

## 3-1: Writing HTTP Responses

1. Update `index_handler` in `tiny_server.py` to add HTML for an index page to the response body

2. Add handling for requests to `/mystery` to return a redirect to https://en.wikipedia.org/wiki/Mystery_Spot

## 3-2: Serving Static Assets

3. Update the tiny server to serve files out of the `files` directory

## 3-3: Forms

4. Update `form.html` to allow users to submit a name

5. Receive a name submitted via POST and display it on form.html

6. Escape user-entered data before writing it on the page

## 3-4 Cookies

7. Store the user's name in a cookie and display it on `form.html`

8. Implement a "Log Out" button that appears only to users who have a cookie. Clicking the button deletes the cookie.

## 3-4: Data-Driven Applications

9. Let logged-in users post on wall.html

10. Save posts in wall.db, sanitizing inputs