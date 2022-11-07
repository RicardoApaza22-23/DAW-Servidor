<?php
$db = mysqli_connect('localhost','root','1234','mysitedb') or die('FAIL');
$email = $_POST['email'];
$contraseña = $_POST['password'];

$query = "Select id,email,contraseña from tUsuarios where email='" . $email . "'";
$result = mysqli_query($db,$query) or die('Query error');


if((mysqli_num_rows($result) > 0)){
    $only_row = mysqli_fetch_array($result);
    if(hash_equals(crypt($contraseña,'$2a$07$usesomesillystringforsalt$'),$only_row[2])){
       
        session_start();
        $_SESSION['user_id']=$only_row[0];
        $_SESSION['email']=$only_row[1];
        header("Location: main.php");
    }else{
        echo "<p style='color:red'> Contraseña incorrecta</p>";
    }
}else{
    echo "<p style='color:red'>Usuario no encontrado con ese email</p>";
}


?>
