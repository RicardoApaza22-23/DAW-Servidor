<html>
<head>
	<title>Conexión a base de datos</title>
</head>
	<body>

		<?php
		$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
 		?>
		<h1>Conexión establecida</h1>
		<?php
		//lanzar un query
		$query = "Select * from tJuegos";
		$resultado = mysqli_query($db,$query) or die("Query error");
		//recorrer el resultadod
		while($row = mysqli_fetch_array($resultado)){
			echo $row[1]. " => " . $row[3]."<br>";
}
		mysqli_close($db);
		?>
	</body>
</html>

