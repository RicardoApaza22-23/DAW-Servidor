<?php
session_start();
$usuario = $_SESSION['user_id'];
$idjuego=$_POST['favorito'];
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('FAIL');

$query="insert into tFavoritos(idUsuario,idJuego) values('".$usuario."', '".$idjuego."')";


mysqli_query($db,$query) or die("FALLO EN BD");
mysqli_close($db);
header("Location: /favorito_added.php");

?>