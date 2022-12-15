
<?php
    require('../../fpdf.php');
    ?>
    <?php
    $nombre = $_POST['name'];
    $apellidos = $_POST['surname'];
    $fecha = date("F j, Y, g:i a");


    $pdf = new FPDF();
    //crear pagina
    $pdf->AddPage();

    //elegimos fuente para los títulos
    $pdf->SetFont('Arial', 'B', 14);
    $pdf->SetFillColor(255, 218, 185);
    $pdf->cell(40, 10, 'CURSO', 1, 0, 'c',true);
    //seleccionar fuente para los datos
  
    $pdf->SetFont('Times', 'u', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->cell(120, 10, 'DESARROLLO DE APLICACION WEB', 1, 0, 'C');
    $pdf->SetTextColor('');
    $pdf->ln();


    $pdf->SetFont('Arial', 'B', 14);
    $pdf->cell(40, 10, 'CENTRO', 1, 0, 'c',true);
    $pdf->SetFont('Times', 'u', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->Cell(120, 10, 'AFUNDACION', 1, 0, 'C');
    $pdf->SetTextColor('');
    $pdf->ln();

    $pdf->SetFont('Arial', 'B', 14);
    $pdf->cell(40, 10, 'FECHA', 1, 0, 'c',true);
    $pdf->SetFont('Times', '', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->Cell(120, 10, '2022/2023', 1, 0, 'C');
    $pdf->SetTextColor('');
    $pdf->ln();

    $pdf->SetFont('Arial', 'B', 14);
    $pdf->cell(40, 10, 'NOMBRE', 1, 0, 'c',true);
    $pdf->SetFont('Times', 'u', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->Cell(120, 10, $nombre, 1, 0, 'C');
    $pdf->SetTextColor('');
    $pdf->ln();

    $pdf->SetFont('Arial', 'B', 14);
    $pdf->cell(40, 10, 'APELLIDOS', 1, 0, 'c',true);
    $pdf->SetFont('Times', 'u', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->Cell(120, 10, $apellidos, 1, 0, 'C');
    $pdf->SetTextColor('');
    $pdf->ln();

    $pdf->SetFont('Arial', 'B', 14);
    $pdf->cell(60, 10, 'FECHA DE DIPLOMA', 1, 0, 'c',true);
    $pdf->SetFont('Times', '', 10);
    $pdf->SetTextColor(189, 183, 107);
    $pdf->Cell(100, 10, $fecha, 1, 0, 'C');
    $pdf->SetTextColor('');

    $pdf->line(190,33,33,33);

    $pdf->Output();

    ?>

