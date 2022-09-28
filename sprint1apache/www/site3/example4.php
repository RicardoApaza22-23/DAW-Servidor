<html>
	<body>
		<h1>Example 4</h1>
		<?php
		function edad_en_5_anos($edad){
			return $edad + 5;

}
		function mensaje($age){
		if(edad_en_5_anos($age) > 65){
			return "En 5 años tendrás edad de jubilación";
		}else{
			return "Disfruta tu tiempo";
}
		}
?>
<table>
<tr>
<th>EDAD</th>
<th>INFO</th>
</tr>
<?php 
$edades = array(20,58,59,60,63,68);
foreach ($edades as $valor){
	echo "<tr>";
	echo "<td>".$valor."</td>";
	echo "<td>".mensaje($valor)."</td>";
	echo "</tr>";
}
 		?>
</table>
	</body>
</html>

