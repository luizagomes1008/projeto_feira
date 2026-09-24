<?php

$conexao = mysqli_connect(
    "localhost",
    "root",
    "",
    "rede_apoio"
);

if (!$conexao) {
    die("Erro na conexão com o banco de dados: " . mysqli_connect_error());
}

mysqli_set_charset($conexao, "utf8mb4");

?>