<?php session_start(); ?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RetroWebSite</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="window">

  <div class="window-bar">

    <p>RetroWeb</p>
  
   <?php if(isset($_SESSION['user'])) { ?>
    <p class="user">
      Welcome, <?php echo $_SESSION['user']; ?> 
    </p>
   <?php } ?>

  </div>


  <nav class="home">
    <a href=""> Home </a>
    <a href=""> About </a>
    <a href=""> Contact </a>

    <?php if(isset($_SESSION['user'])) { ?>
     <a href="logout.php"> Logout </a>
    <?php } ?>

  </nav>

  <section class="welcome">
    <h1> WELCOME TO THE INTERNET! </h1>
    <a href="login.php">
       <button class="enter"> :: LOGIN :: </button>
    </a>
  </section>

  <section class="about">
    <h2> Old is Gold </h2>
    <p> Bringing back the nostalgia</p>
  </section>

  <section class="box">
    <div class="design">
    <a href="gameboy.php">
      <button class="game">
        <img src="images\gameboy.png" width="120" class="img1">
        <h3> GameBoy Rome </h3>
      </button>
    </a>
    </div>

    <div class="design">
      <a href="gameboy.php">
       <button class="game">
         <img src="images\cassette_tape1.png" width="120" class="img1">
         <h3> Cassette Tape </h3>
       </button>
     </a>
    </div>

    <div class="design">
      <a href="gameboy.php">
       <button class="game">
         <img src="images\floppy_disk1.png" width="120" class="img1">
         <h3> Floppy Disk </h3>
       </button>
      </a>
    </div>
  </section>


  <section class="get">
    <button class="enter"> Get in Touch </button>
  </section> 

  <p class="rights">
    © 2026 RetroWebSite. All rights reserved. 
  </p>


</div>

</body>
</html>


<!-- PS E:\Git\College-Projects\Html_CSS\Webpage> php -S localhost:8000 -->
