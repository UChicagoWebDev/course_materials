# weblog.py
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse
import sqlite3

import http_headers, index_page, leave_comment, create_post
from http_headers import Method

# This is a simple extension on Python's built-in web server library
# See https://github.com/python/cpython/blob/3.12/Lib/http/server.py#L146C7-L146C29
class WebRequestHandler(BaseHTTPRequestHandler):
    # BaseHTTPRequestHandler will call this function for any GET request
    def do_GET(self):
        print("GET")
        self.path_handler(Method.GET)
 
    # BaseHTTPRequestHandler will call this function for any POST request
    def do_POST(self):
        print("POST")
        self.path_handler(Method.POST)

    def path_handler(self, method: Method):
        parsedUrl = urlparse(self.path)
        # This is a python dictionary containing any query parameters the user sent
        # See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web#query
        queryParams = dict(parse_qsl(parsedUrl.query))
        db_connection = sqlite3.connect("db/weblog.sqlite3")

        # Each page has its own handler function, which writes the whole
        # response (headers and body) to self.wfile
        if parsedUrl.path == "/":
            index_page.index_handler(self, method, db_connection)
        elif parsedUrl.path == "/comment":
            leave_comment.comment_handler(self, method, db_connection, queryParams)
        elif parsedUrl.path == "/post":
            create_post.create_post_handler(self, method, db_connection)
        elif parsedUrl.path == "/css/style.css":
            self.css_handler()
        else:
            self.not_found_handler()

        db_connection.close()

    def css_handler(self):
        with open("css/style.css") as style:
            response = "HTTP/1.0 200 OK\r\n" \
                "Content-Type: text/css; charset=utf-8\r\n" \
                "\r\n"
            response += style.read()

        self.wfile.write(response.encode("utf-8"))

    def not_found_handler(self):
        response = http_headers.write_404()
        self.wfile.write(response.encode("utf-8"))


if __name__ == "__main__":
    print("Starting web server at http://localhost:8000")
    print("Press Control-C to stop")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
