from enum import Enum

class Method(Enum):
    GET = 1
    POST = 2

def write_headers():
    return  "" \
f"""HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
"""
def write_blank_line():
    return "" \
"""
"""
def redirect_to(location):
    return f"""HTTP/1.0 302 Found
Location: {location}
"""
def write_404():
    return f"""HTTP/1.0 404 FILE NOT FOUND
"""