<?php
session_start();

$valid_user = "Nosled";
$valid_pass = "1234";
$error = "";

if($_SERVER["REQUEST_METHOD"] == "POST") {

  $user = $_POST["username"];
  $pass = $_POST["password"];

  if($user === $valid_user && $pass === $valid_pass) {

    $_SESSION["user"] = $user;

    header("Location: main.php"); 
    exit();

  } else {
    $error = "Invalid Login!";
  }
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Retro Login</title>

<style>

  @font-face {
  font-family: 'Press Start 2P';
  src: url('fonts/PressStart2P-Regular.ttf') format('truetype');
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: #111;
  font-family: 'Inter', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}


.logwindow {
  width: 500px;
  background: #f5f5f5;
  border: 3px solid #000;
}


.logwindow-bar {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border-bottom: 3px solid #000;
  font-family: 'Press Start 2P', cursive;
  font-size: 10px;
  background: #e0e0e0;
}

.logbuttons div {
  width: 12px;
  height: 12px;
  border: 2px solid #000;
  display: inline-block;
  margin-left: 5px;
}


.logtitle {
  text-align: center;
  padding: 25px;
  font-family: 'Press Start 2P', cursive;
  font-size: 14px;
}


.form-box {
  padding: 25px 40px;
}

label {
  font-family: 'Press Start 2P', cursive;
  font-size: 10px;
}

input{
  width: 100%;
  padding: 10px;
  margin: 10px 0 20px;
  border: 2px solid #000;
  background: #fff;
}


button {
  width: 100%;
  padding: 12px;
  border: 3px solid #000;
  background: #000;
  color: #fff;
  font-family: 'Press Start 2P', cursive;
  cursor: pointer;
}

button:hover {
  background: #fff;
  color: #000;
}


.error {
  color: red;
  font-size: 12px;
  margin-bottom: 15px;
  text-align: center;
}


.footer {
  text-align: center;
  padding: 12px;
  border-top: 3px solid #000;
  font-size: 11px;
}

</style>
</head>
<body>

<div class="logwindow">

 
  <div class="logwindow-bar">
    <p>RetroWebSite — Login</p>
  </div>


  <div class="logtitle">
    :: SYSTEM LOGIN ::
  </div>

  
  <div class="form-box">

    <?php if($error != "") { ?>
      <div class="error"><?php echo $error; ?></div>
    <?php } ?>

    <form method="POST">

      <label>USERNAME</label>
      <input type="text" name="username" required>

      <label>PASSWORD</label>
      <input type="password" name="password" required>

      <button type="submit">LOGIN</button>

    </form>

  </div>

  <div class="footer">
    © 2026 RetroWebSite
  </div>

</div>

</body>
</html>

