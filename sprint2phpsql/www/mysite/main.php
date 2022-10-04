<html>
<head>
	<title>Conexión a base de datos</title>
</head>
	<body>

		<?php
		$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
 		?>
		<h1>Conexión establecida</h1>
	</body>
</html>

