<?php

header('Content-Type: application/json; charset=utf-8');

require_once 'conexao.php';

$sql = "SELECT
            id,
            nome,
            categoria,
            tipo,
            descricao,
            servicos,
            publico,
            horario,
            endereco,
            cidade,
            telefone,
            latitude,
            longitude,
            site
        FROM apoios";

$resultado = mysqli_query($conexao, $sql);

if (!$resultado) {
    echo json_encode([
        "erro" => "Erro ao buscar os apoios.",
        "detalhes" => mysqli_error($conexao)
    ], JSON_UNESCAPED_UNICODE);

    exit;
}

$locais = [];

while ($linha = mysqli_fetch_assoc($resultado)) {
    $locais[] = $linha;
}

echo json_encode(
    $locais,
    JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);

mysqli_close($conexao);

?>