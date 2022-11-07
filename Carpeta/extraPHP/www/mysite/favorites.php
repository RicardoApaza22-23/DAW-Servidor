<head>

    <link href="main.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Rock+Salt' rel='stylesheet' type='text/css'>

</head>
<?php
session_start();
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('FAIL');
$usuario = $_SESSION['user_id'];
$query = "select tFavoritos.idUsuario,tUsuarios.id,tJuegos.nombre,tJuegos.url_image,tJuegos.categoria,tJuegos.PEGI from tUsuarios inner join tFavoritos on tUsuarios.id=tFavoritos.idUsuario inner join tJuegos on tJuegos.id=tFavoritos.idJuego";
$resultado = mysqli_query($db, $query) or die("fallo");
?>
<table border="1">
    <tr>
        <th>IDUsuario</th>
        <th>Juego</th>
        <th>Foto</th>
        <th>Categoria</th>
        <th>PEGI</th>
    </tr>

    <?php
    while ($row = mysqli_fetch_array($resultado)) {
        echo "<tr>";
        echo ("<td>" . $row[1] . "</td>");
        echo ("<td>" . $row[2] . "</td>");
        echo "<td><img width='70' height='70' src='" . $row[3] . "'</td>";
        echo ("<td>" . $row[4] . "</td>");
        echo ("<td>" . $row[5] . "</td>");
        echo "</tr>";
    }

    ?>