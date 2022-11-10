<?php
session_start();
$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
$contraseña = $_POST['password'];
$id = $_SESSION['user_id'];
$hashPass=crypt($contraseña, '$2a$07$usesomesillystringforsalt$');

$query = "update tUsuarios set contraseña='". $hashPass . "' where id= ' ".$id." ' ";

if($contraseña!=''){
    mysqli_query($db, $query) or die('Error');
    header("Location: /logout.php");
}else{
    echo "<p style='color:red'>Campo vacío</p>";
}
?>
