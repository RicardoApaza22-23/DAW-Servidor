<html>
<?php
		$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
 		?>
<head>
	<title>Conexión a base de datos</title>
</head>
	<body>
        <?php
            $juegos_id = $_POST['juegos_id'];
            $comentario = $_POST['new_comment'];
            $query = "insert into tComentarios(comentarios,usuario_id,'usuario_id') values ('".$comentario."',". $juegos_id ."','null')";
            mysqli_query($db,$query) or die('Error');
            echo "<p>Nuevo Comentario";
            echo mysqli_insert_id($db);
            echo " añadido</p>";
            echo "<a href='detail.php?juegos_id=" . $juegos_id . "'>Volver</a>";
            mysqli_close($db);
        ?>
	</body>
</html>