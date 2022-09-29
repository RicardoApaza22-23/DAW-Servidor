<html>
	<body>
		<h1>Conversor de longitudes</h1>
		<p>Convierte de la unidad especificada a metros</p>
<p>
		<?php
			if(isset($_POST['funidad'])){
				if($_POST['funidad']=='pulgada'){
				$v_pulgadas=$_POST['fcantidad'];
				$v_metros = $v_pulgadas * 0.0254;
				echo "<p style='color:green'>".$v_pulgadas." pulgada(s) = ".$v_metros." metro(s)</p>";
				}else{
					echo "<p style='color:red'>Unidad no soportada";
				}
}

		?>
</p>
<p>Realiza una nueva conversión: </p>
<form action="/conversor2.php" method="post">
	<label for="cantidad_input">Cantidad:</label><br>
	<input type="text" id="cantidad_input" name="fcantidad"><br>

	<input type="radio" id="pulgada_input" name="funidad" value="pulgada">
	<label for="pulgada_input">Pulgada(s)</label><br>
	<input type="radio" id="otro_input" name="funidad" value="otro">
	<label for="otro_input">Otros</label><br>
	<input type="submit" value="convertir">
</form>

	</body>
</html>

