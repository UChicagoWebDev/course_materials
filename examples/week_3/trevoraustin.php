<html>
<head>
  <title>POST Handling Example</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <style> hr { margin: 20px 20px 20px 20px; } </style>
</head>
<body>
  <h1>Post Code</h1>
  <hr/>
  <?php $x = 5 ?>
  <div class="post-place">
      <?php if (isset($_POST['submit'])) { ?>
        <?php echo htmlspecialchars($_POST['freeform']) ?>
      <?php } else { ?>
          Welcome! That was a GET request!
      <?php } ?>
  </div>
  <hr/>
  <div>
    <form action="trevoraustin.php" method="post">
      <label for="freeform">Any old text</label>
      <textarea name="freeform"></textarea>
      <input type="submit" name="submit" value="Submit"></input>
    </form>
    <?php echo $x ?>
  </div>
</body>
