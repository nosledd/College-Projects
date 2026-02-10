<?php
session_start();

if(!isset($_SESSION['user'])) {
  echo "<p style='text-align:center;'>Please Log In</p>";
  exit();
}
?>


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
    <p class="window-title">RetroWeb</p>
  </div>

  <nav class="home">
    <a href="main.php"> Home </a>
    <a href="about"> About </a>
    <a href="contact"> Contact </a>
  </nav>



  <h1 class="title">:: RETRO GAME BOY ::</h1>

  <div class="content">

    <div class="left">
      <img src="images\gameboy.png" alt="GameBoy">
    </div>
   
    <div class="right">

      <div class="panel">
        <h3>POWER ON</h3>
        <p>
          Play classic games on the go with the iconic Game Boy.
          Relive the days of monochrome screens and 8-bit adventures.
        </p>
      </div>

      <div class="panel">
        <h3>GAME LIST</h3>
        <ul>
          <li>Tetris</li>
          <li>Super Mario Land</li>
          <li>Pokémon Red & Blue</li>
          <li>Donkey Kong</li>
          <li>Metroid II</li>
        </ul>
      </div>

    </div>

  </div>

 
  <div class="description">
    <h3>Portable Nostalgia</h3>
    <p>
      Born in 1989, the Game Boy brought portable gaming to the masses
      with its monochrome screen and classic D-pad controls. It became
      the best-selling handheld of its time, selling over 118 million units worldwide.
    </p>
  </div>

  

  
  <div class="rights">
    © 2026 RetroWebSite. All rights reserved.
  </div>

</div>

</body>
</html>