<html>
<?php
		$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
 		?>
<head>
	<title>Conexión a base de datos</title>
</head>
	<body>
        <?php
        if (!isset($_GET['juegos_id'])){
            die('NO SE HA ESPECIFIDADO UN JUEGO');
        }
        $juegos_id = $_GET['juegos_id'];
        $query = "Select * from tJuegos where id=".$juegos_id;
        $result = mysqli_query($db,$query) or die('Query error');
        $only_row = mysqli_fetch_array($result);
        echo '<h1>'.$only_row['nombre'].'</h1>';
        echo '<h2>'.$only_row['categoria'].'</h2>';
        ?>
        <h3>COMENTARIOS:</h3>
        <ul>
        <?php
            $query2 = "select * from tComentarios where juegos_id = ". $juegos_id ; 
            $result2 = mysqli_query($db,$query2) or die('Query error');
            while($row = mysqli_fetch_array($result2)){
                echo "<li>". $row['comentarios']. "</li>";
            }
            mysqli_close($db);
        ?>
        </ul>
	</body>
</html>
