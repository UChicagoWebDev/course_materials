<html>
<head>
  <title>POST Handling Example</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <style> hr { margin: 20px 20px 20px 20px; } </style>
</head>
<body>
  <h1>Post Code (No Escaping)</h1>
  <hr/>
  <div class="post-place">
    <?php if (isset($_POST['submit'])) { ?>
      <?php echo $_POST['freeform'] ?>
    <?php } ?>
  </div>
  <hr/>
  <div>
    <form action="post_no_escape.php" method="post">
      <label for="freeform">Any old text</label>
      <textarea name="freeform"></textarea>
      <input type="submit" name="submit" value="Submit"></input>
    </form>
  </div>
</body>
