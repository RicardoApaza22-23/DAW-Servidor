<?php
session_start();
?>
<html>
<head>
	<title>Conexión a base de datos</title>
	<link href="main.css" rel="stylesheet" type="text/css">
	<link href='https://fonts.googleapis.com/css?family=Rock+Salt' rel='stylesheet' type='text/css'>
</head>
	<body>

		<?php
		
		$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
 		?>
		<h1>Conexión establecida</h1>´
		<table border="1" id="tabla">
			<tr>
				<th>ID</th>
				<th>Juego</th>
				<th>Foto</th>
				<th>Categoria</th>
				<th>PEGI</th>
			</tr>
		<?php
			
		//lanzar un query
		$query = "Select * from tJuegos";
		$resultado = mysqli_query($db,$query) or die("Query error");
		//recorrer el resultadod
		while($row = mysqli_fetch_array($resultado)){
			echo "<tr>";
			echo "<td><a href='detail.php?juegos_id=".$row[0]."'>$row[0]</a> </td>";
			// echo $row[1]. " => " . $row[3]."<br>";
			echo "<td>".$row[1]."</td>";
			echo "<td>".$row[2]."</td>";
			echo "<td>".$row[3]."</td>";
			echo "<td>".$row[4]."</td>";
			echo "</tr>";
}

		mysqli_close($db);

		?>
		</table>
<br>
<a href ="/logout.php" > LogOut</a>

<?php
if(isset($_SESSION['user_id'])){
echo '<a href ="/cambiarContrasena.html" > Cambiar Contraseña</a>';
}

?>
	</body>
</html>

