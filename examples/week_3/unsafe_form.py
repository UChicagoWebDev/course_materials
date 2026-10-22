# unsafe_form.py
# THIS IS BAD: a tiny server that echoes form input back into the page without
# escaping it. Run it, open http://localhost:8000, and try posting:
#
#   <div style="position: absolute;top: 0;left: 0;width: 500;background-color: red;height: 1000;">Hahahaha!</div>
#
# Then fix it by wrapping the user's input in html.escape() (see TODO below).
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse
from enum import Enum

class Method(Enum):
    GET = 1
    POST = 2

# Every message anyone has posted, kept in memory until the server stops.
# Because everyone sees the same list, one bad post breaks the page for everybody.
messages = []

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET")
        self.path_handler(Method.GET)

    def do_POST(self):
        print("POST")
        self.path_handler(Method.POST)

    def path_handler(self, method: Method):
        parsedUrl = urlparse(self.path)

        if parsedUrl.path == '/':
            self.form_handler(method)
        else:
            self.not_found_handler()

    def form_handler(self, method: Method):
        if method == Method.POST:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = dict(parse_qsl(post_data))
            print("Form Data:", form_data)
            messages.append(form_data.get('message', ''))

        # THIS IS BAD: user input goes straight into the HTML.
        # TODO: fix it with html.escape(message)
        message_list = "\n".join(f"        <li>{message}</li>" for message in messages)

        # No <!DOCTYPE html>, so the browser renders in quirks mode and accepts
        # the unitless "width: 500" and "height: 1000" in the attack above.
        body = f"""<html>
<head>
    <title>Unsafe Form by Tiny Server</title>
</head>
<body>
    <h1>Leave a message</h1>
    <form method="POST" action="/">
        <input type="text" name="message" size="80">
        <button type="submit">Post</button>
    </form>
    <h2>Messages</h2>
    <ul>
{message_list}
    </ul>
</body>
</html>"""

        self.wfile.write(
f"""HTTP/1.0 200 OK\r
Content-Type: text/html; charset=utf-8\r
\r
{body}""".encode("utf-8"))

    def not_found_handler(self):
        self.wfile.write("HTTP/1.0 404 FILE NOT FOUND\r\n".encode("utf-8"))

if __name__ == "__main__":
    print("Starting web server at http://localhost:8000")
    print("Press Control-C to stop")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
