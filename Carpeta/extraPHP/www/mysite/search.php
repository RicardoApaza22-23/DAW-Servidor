<head>
    <link href="main.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Rock+Salt' rel='stylesheet' type='text/css'>
</head>
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('FAIL');
// echo "Asdasd";
// var_dump($_POST);

$parametro = $_POST['search'];
$query = "select * from tJuegos where nombre like '%" . $parametro . "%' or categoria like '%" . $parametro . "%' or PEGI like '%" . $parametro . "%' ";
$resultado = mysqli_query($db, $query) or die("Query error");
?>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Juego</th>
        <th>Foto</th>
        <th>Categoria</th>
        <th>PEGI</th>
        <th>AÑADIR A FAVORITOS</th>

    </tr>
    <?php

    while ($row = mysqli_fetch_array($resultado)) {
        
        echo "<tr>";
        echo "<td><a src='detail.php?juegos_id=".$row[0]."'>$row[0]</a> </td>";

        echo "<td>" . $row[1] . "</td>";
        echo "<td><img width='70' height='70' src='" . $row[2] . "'</td>";
        echo "<td>" . $row[3] . "</td>";
        echo "<td>" . $row[4] . "</td>";
        
        ?>
<form action="do_add_favorite.php" method="post" id="formulario">
<input name="favorito" type="hidden" id="favorito" value="<?php echo $row[0] ?>"><br>
<td><input type="submit" value="favorito"></td>
</form>
        <?php
        echo "</tr>";
    }

    ?>
</table>
<br>
<a href="/main.php">Volver a pagina principal</a>