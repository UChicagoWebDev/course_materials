import http_headers
from http_headers import Method

SECRET_PASSWORD = "phil"

def create_post_handler(request, method: Method, db_connection):
    message = ""

    if method == Method.POST:
        # TODO: get the title, body, and password out of the form data
        # password = form_data.get("password")

        # If the password doesn't match the secret password on our server,
        # return the page with an error message:
        # message = "rejected"

        # TODO: otherwise, the password matches, so we need to update the database
        # with our new post, remembering to sanitize your inputs
        # message = "success"
        pass

    response = http_headers.write_headers()
    response += http_headers.write_blank_line()
    response += write_html(message)

    request.wfile.write(response.encode("utf-8"))

def write_html(message=""):
  # TODO: Update the h1 with your name
  html = f"""<html>
<head>
  <title>Create a Post</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
  <h1>&lt;yourname&gt;'s Web Journal</h1>
  <div class="create-post">
    <h2>Create a Post</h2>"""
  
  if message == "rejected":
    html += """
    <h3 class="error">Oops, wrong password!</h3>"""
  elif message == "success":
    html += """
    <h3 class="success">Post created! See it <a href="/">here</a>."""
  html += """
    <form method="post">
      <label for="title">Title</label>
      <input name="title"></input>
      <label for="body">Post Body</label>
      <textarea name="body"></textarea>
      <label for="password">Secret Password</label>
      <input type="password" name="password"></input>
      <input type="submit" name="submit" value="Create Post"></input>
    </form>
  </div>
  <a href="/">Home</a>
</body>
</html>"""
  return html