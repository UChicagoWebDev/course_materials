def write_html(post={}):
  # TODO: Update the h1 with your name
  # TODO: Display the post the user is commenting on, and the existing comments
  html = f"""<html>
<head>
  <title>Leave a Comment</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
  <h1>&lt;yourname&gt;'s Web Journal</h1>
  <div class="leave-comment">
    <h2>
      Leave a Comment on
      <a href="weblog.php#a_post_title">A Post Title</a>
    </h2>

    <div class="post-body">
Call me Ishmael. Some years ago&mdash;never mind how long precisely&mdash;having
little or no money in my purse, and nothing particular to interest me on shore,
I thought I would sail about a little and see the watery part of the world. It
is a way I have of driving off the spleen and regulating the circulation.
Whenever I find myself growing grim about the mouth; whenever it is a damp,
drizzly November in my soul; whenever I find myself involuntarily pausing before
coffin warehouses, and bringing up the rear of every funeral I meet; and
especially whenever my hypos get such an upper hand of me, that it requires a
strong moral principle to prevent me from deliberately stepping into the street,
and methodically knocking people's hats off&mdash;then, I account it high time
to get to sea as soon as I can. This is my substitute for pistol and ball. With
a philosophical flourish Cato throws himself upon his sword; I quietly take to
the ship. There is nothing surprising in this. If they but knew it, almost all
men in their degree, some time or other, cherish very nearly the same feelings
towards the ocean with me.
    </div>

    <h3>2 Comments</h3>
    <div class="comment-block">
      <div class="comment">
        <div class="comment-body">
          Yeah Izzy!
        </div>
        <div class="comment-author">
          Sydney Carton
        </div>
      </div>
      <div class="comment">
        <div class="comment-body">
          off to a great start!
        </div>
        <div class="comment-author">
          nick_carraway
        </div>
      </div>
    </div>

    <form method="post">
      <label for="body">Comment</label>
      <textarea name="body"></textarea>
      <label for="name">Your name</label>
      <input name="name"></input>
      <input type="hidden" name="post_id" value="1"></input>
      <input type="submit" name="submit" value="Leave Comment"></input>
    </form>
  </div>
  <a href="/">Home</a>
</body>
</html>"""
  return html