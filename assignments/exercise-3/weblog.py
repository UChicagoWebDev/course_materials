# weblog.py
from enum import Enum
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse
import http_headers, index_page, leave_comment, create_post
import sqlite3
SECRET_PASSWORD = "phil"

class Method(Enum):
    GET = 1
    POST = 2

# This is a simple extension on Python's built-in web server library
# See https://github.com/python/cpython/blob/3.12/Lib/http/server.py#L146C7-L146C29
class WebRequestHandler(BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call this function for any GET request
    def do_GET(self):
        print("GET")
        self.handler(Method.GET)
 
    # BaseHTTPRequestHandler will call this function for any POST request
    def do_POST(self):
        print("POST")
        self.handler(Method.POST)

    def handler(self, method: Method):
        parsedUrl = urlparse(self.path)
        # This is a python dictionary containing any query parameters the user sent
        # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web#query
        queryParams = dict(parse_qsl(parsedUrl.query))
        db_connection = sqlite3.connect("db/weblog.sqlite3")

        if parsedUrl.path == "/":
            # TODO: get posts and comments from the database
            # results = db_connection.execute("SELECT ...")
            # HINT: re-shape your data in Python so each post object has a list of its comments
            # e.g.  [
            #           {
            #               post_id: 1, 
            #               comments: [{...}, {...}, ...],
            #               ...
            #           }, 
            #           {
            #               post_id: 2,
            #               ...
            #           },
            #           ...
            #       ]
            posts_with_comments= []
            responseBody = index_page.write_html(posts_with_comments=[])

        elif parsedUrl.path == "/comment":
            # TODO: get the post we're commenting on and all the previous comments on it
            post = {}
            # SELECT * from POSTS where post_id = ...
            # SELECT * from COMMENTS where post_id = ...
            # post.comments = comments
            responseBody = leave_comment.write_html(post)
        elif parsedUrl.path == "/create":
            responseBody = create_post.write_html()
        elif parsedUrl.path == "/css/style.css":
            responseBody = ""
            with open("css/style.css") as style:
                responseBody += style.read()
        else:
            response = http_headers.write_404()
            self.wfile.write(response.encode("utf-8"))
            return
        
        response = http_headers.write_headers()
        response += http_headers.write_blank_line()
        response += responseBody

        self.wfile.write(response.encode("utf-8"))

    # TODO: add cases for any other paths that should receive a POST request
    #       update the database as appropriate, remembering to sanitize your inputs
    #       then render the appropriate page and send it as a response
    
    # in case  of POSTS:
        # get the password that the user entered into the form data
        # if it doesn't match the secret password on our server, return the page with
        # an error message. See create_post.py.

        # password = formData.get("password")
        # if password == SECRET_PASSWORD:
        # TODO: otherwise, the password matches, so we need to update the database with
        # our new post
        # do_some_stuff()
        # We redirect back to the index page, where our new post should be at the top


if __name__ == "__main__":
    print("Starting web server at http://localhost:8000")
    print("Press Control-C to stop")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()