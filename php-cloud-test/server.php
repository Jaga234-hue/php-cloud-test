<?php
// server.php
header('Content-Type: application/json');

$response = [
    "message" => "Hello from Google Cloud!",
    "time" => date("Y-m-d H:i:s")
];

echo json_encode($response);
?>
