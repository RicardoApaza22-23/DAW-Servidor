<?php
session_start();
$usuario = $_SESSION['nombre'];
$idjuego=$_POST['favorito'];
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('FAIL');

var_dump($_POST);
//$query="insert into tFavoritos(idUsuario,idJuego) values('".$."')"

?>