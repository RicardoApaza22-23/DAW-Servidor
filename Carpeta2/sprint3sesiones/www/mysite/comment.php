<?php
session_start();
?>
<html>

<head>
	<title>Conexión a base de datos</title>
</head>

<body>
	<?php

	$db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('FAIL');
	
	//el programa solo acepta registros de la base de datos aunque le pase otros parámetros

	if (!empty($_SESSION['user_id'])) {
		$user = $_SESSION['user_id'];
	}
	
	$juegos_id = $_POST['juegos_id'];
	$comentario = $_POST['new_comment'];
	$fecha = date('Y-m-d H:i:s');
	if ($comentario != '') {
		$query = "insert into tComentarios(comentarios,usuario_id,juegos_id,fecha) values('" . $comentario . "','" . $user . "','".$juegos_id."','".$fecha."')";
		mysqli_query($db, $query) or die('Error');
		echo "<p>Nuevo Comentario";
		echo mysqli_insert_id($db);
		echo " añadido</p>";
		echo "<a href='detail.php?juegos_id=" . $juegos_id . "'>Volver</a>";
	} else {

		echo "<p style='color:red'> Introduzca un comentarios</p>";
		echo "<a href='detail.php?juegos_id=" . $juegos_id . "'>Vovler</a>";
	}




	mysqli_close($db);

	?>
</body>

</html>
