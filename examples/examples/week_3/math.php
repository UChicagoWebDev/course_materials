<html>
<head>
  <title>PHP Math Examples</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
  <h1> Let's do some math on the server!</h1>
  <p>2 + 2 = <?php echo 2+2 ?></p>
  <p>8 - 3 = <?php echo 8-3 ?></p>
  <p>6 * 7 = <?php echo 6*7 ?></p>
  <p>pi = <?php echo pi()?></p>
  <p>
    <?php echo getenv("HTTP_USER_AGENT") ?>
  </p>
</body>
