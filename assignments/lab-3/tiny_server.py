# weblog.py
from functools import cached_property
import html
from http.cookies import SimpleCookie
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse, unquote_plus
from enum import Enum
import os

class Method(Enum):
    GET = 1
    POST = 2

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

        if parsedUrl.path == '/':
            self.index_handler(method)
        elif parsedUrl.path == '/mystery':
            self.mystery_handler(method)
        elif parsedUrl.path.startswith('/files/'):
            self.files_handler(method, parsedUrl.path)
        elif parsedUrl.path == '/form':
            self.form_handler(method)
        else:
            self.not_found_handler()

    def not_found_handler(self):
        response = """HTTP/1.0 404 FILE NOT FOUND

            """
        self.wfile.write(response.encode("utf-8"))

    def index_handler(self, method: Method):
        # TODO: add the rest of the Response to return an index page
        response =  """HTTP/1.1 200 OK
Content-Type: text/html
Nonense-Header: foobar

<html>
<head>
    <title>Index Page</title>
</head>
<body>
    <h1>Welcome to the Index Page</h1>
    <p>This is a simple web server built using Python's http.server module.</p>
</body>
</html>
"""

        self.wfile.write(response.encode("utf-8"))

    def files_handler(self, method: Method, path):
        file_contents = None

        fs_path = os.getcwd() + unquote_plus(path)

        print(f"FS PATH: {fs_path}")

        if os.path.exists(fs_path):
            if os.path.isfile(fs_path):
                with open(fs_path, 'rb') as f:
                    file_contents = f.read()

        if file_contents is None:
            self.not_found_handler()
            return

        # TODO
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        
        response = response.encode("utf-8") + file_contents

        self.wfile.write(response)
        

    def mystery_handler(self, method: Method):
        #TODO https://en.wikipedia.org/wiki/Mystery_Spot
        response = """HTTP/1.1 302 Found
Location: https://en.wikipedia.org/wiki/Mystery_Spot
"""
        

        self.wfile.write(response.encode("utf-8"))

    def form_handler(self, method: Method):
        print("FORM")
        print(method)

        if method == Method.POST:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = dict(parse_qsl(post_data))
            print("Form Data:", form_data)

        with open('form.html', 'rb') as f:
            content = f.read()
            print(f"FILE CONTENT: {content}")

            page_template = content.decode('utf-8')

            if method == Method.POST:
                u = html.escape(form_data.get("username", ""))
                
                page_template = page_template.replace("{username}", u)

                # TODO: set a cookie with the username
                headers = "HTTP/1.0 200 OK\r\n" \
                    "content-type: text/html\r\n" \
                    "Set-Cookie: username={}\r\n".format(u) + \
                    "\r\n"
                
                response = (headers + page_template).encode("utf-8")
                self.wfile.write(response)
                
            else:
                username = None

                # TODO: get the username from the cookie if it exists
                cookie_header = self.headers.get('Cookie')
                if cookie_header:
                    cookie = SimpleCookie(cookie_header)
                    if 'username' in cookie:
                        username = cookie['username'].value
                
                if username:
                    page_template = page_template.replace("{username}", html.escape(username))
                
                headers = "HTTP/1.0 200 OK\r\n" \
                    "content-type: text/html\r\n" \
                    "\r\n"
                
                response = (headers + page_template).encode("utf-8")
                self.wfile.write(response)

if __name__ == "__main__":
    print("Starting web server at http://localhost:8000")
    print("Press Control-C to stop")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()