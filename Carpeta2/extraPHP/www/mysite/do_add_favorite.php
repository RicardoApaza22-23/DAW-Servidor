<?php
session_start();
$usuario = $_SESSION['user_id'];
$idjuego=$_POST['favorito'];
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('FAIL');
if(isset($_SESSION['user_id'])){
$query="insert into tFavoritos(idUsuario,idJuego) values('".$usuario."','".$idjuego."')";
$result = mysqli_query($db,$query) or die('Error');
echo "añadido a favoritos";
}else{
header('Location: login.html');
}

?>
