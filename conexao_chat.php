<?php
// Garante que a resposta seja sempre um JSON limpo
header('Content-Type: application/json; charset=utf-8');
error_reporting(0); // Oculta avisos do PHP para não quebrar o JSON

$host = "localhost";
$user = "root";
$pass = "";
$dbname = "rede_apoio";

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo json_encode([
        'status' => 'sucesso',
        'acolhimento' => "Estou com um pequeno problema técnico para acessar o banco de dados agora, mas estou aqui com você! 💜",
        'pergunta_seguinte' => "Tente atualizar a página ou me perguntar novamente em instantes.",
        'quantidade' => 0,
        'dados' => []
    ]);
    exit;
}

$dados = json_decode(file_get_contents('php://input'), true);
$mensagem = isset($dados['mensagem']) ? trim(mb_strtolower($dados['mensagem'], 'UTF-8')) : '';

if (empty($mensagem)) {
    echo json_encode([
        'status' => 'sucesso',
        'acolhimento' => "Estou te ouvindo com toda a atenção. Pode me contar o que você precisa. 🌸",
        'pergunta_seguinte' => "Como posso te ajudar hoje?",
        'quantidade' => 0,
        'dados' => []
    ]);
    exit;
}

// 1. AGRADECIMENTOS E DESPEDIDAS
if (preg_match('/(^obrigada|^valeu|^muito obrigada|^brigadu|tchau|ate mais|agradeco)/u', $mensagem)) {
    $respostas = [
        "Imagina! Fico muito feliz de poder ajudar de alguma forma. Cuide bem de você e lembre-se de que estou sempre por aqui. 💜",
        "Por nada! Meu maior objetivo é que você se sinta segura e apoiada. Conte comigo sempre que precisar. ✨",
        "Estou aqui exatamente para isso. Vá no seu ritmo, você é muito forte. Se precisar de mais alguma informação, é só chamar! 🌸"
    ];
    echo json_encode([
        'status' => 'mensagem_especial',
        'resposta' => $respostas[array_rand($respostas)]
    ]);
    exit;
}

// 2. EMERGÊNCIA / VIOLÊNCIA
if (preg_match('/(agredida|apanhando|violencia|agressao|agressor|bater|ameaca|perigo|socorro|medo|180|190|briga|abus|apanhei)/u', $mensagem)) {
    $stmtUrgente = $pdo->query("SELECT * FROM apoios WHERE categoria LIKE '%Jurídico%' OR categoria LIKE '%Segurança%' OR tipo LIKE '%Delegacia%' OR nome LIKE '%DDM%' LIMIT 3");
    $locaisUrgentes = $stmtUrgente->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode([
        'status' => 'sucesso',
        'acolhimento' => "🚨 <strong>Sua vida e segurança são prioridade absoluta.</strong><br>Sinto muito que você esteja passando por isso, mas quero te lembrar que <strong>a culpa nunca é sua</strong>.<br><br>• <strong>Ligue 190</strong> para emergências da Polícia Militar.<br>• <strong>Ligue 180</strong> para orientação segura e sigilosa 24h.",
        'pergunta_seguinte' => "Você está em um local seguro? Posso te mostrar a Delegacia da Mulher (DDM) mais próxima.",
        'quantidade' => count($locaisUrgentes),
        'dados' => $locaisUrgentes
    ]);
    exit;
}

// 3. DEFINIÇÃO DE CATEGORIA E ACOLHIMENTO
$categoria_busca = "";
$cidade_busca = "";
$acolhimento = "";
$pergunta_seguinte = "";

if (strpos($mensagem, 'maua') !== false || strpos($mensagem, 'mauá') !== false) {
    $cidade_busca = "Mauá";
} elseif (strpos($mensagem, 'ribeirao') !== false || strpos($mensagem, 'ribeirão') !== false) {
    $cidade_busca = "Ribeirão Pires";
}

// Saúde (Gravidez, médicos, remédios, psicológico)
if (preg_match('/(grávida|gravida|medico|médico|ubs|posto|hospital|ubs|saude|psicolog|depressao|ansiedade|terapia|chora|triste)/u', $mensagem)) {
    $categoria_busca = "Saúde";
    $acolhimento = "A saúde é um direito fundamental, especialmente em momentos tão importantes como a gestação ou o cuidado com o bem-estar. Você merece um atendimento humanizado e gratuito. 🩺💜";
    $pergunta_seguinte = "Gostaria de conferir os postos de saúde, UBS ou atendimento médico gratuito na sua cidade?";
} 
// Jurídico
elseif (preg_match('/(direito|advogad|juridic|defensoria|processo|divorcio|pensao|guarda|medida protetiva)/u', $mensagem)) {
    $categoria_busca = "Jurídico";
    $acolhimento = "Lidar com questões legais gera insegurança, mas você tem leis que protegem os seus direitos. ⚖️";
    $pergunta_seguinte = "Quer que eu busque os contatos de orientação jurídica gratuita na sua região?";
} 
// Assistência Social / Fome / CRAS
elseif (preg_match('/(cras|creas|beneficio|bolsa|auxilio|comida|fome|necessidade|cadastro unico)/u', $mensagem)) {
    $categoria_busca = "Assistência Social";
    $acolhimento = "A rede de assistência social existe exatamente para garantir dignidade e suporte para você e sua família. 🥣🤝";
    $pergunta_seguinte = "Você quer saber o endereço do CRAS mais próximo?";
} 
// Emprego / Renda
elseif (preg_match('/(emprego|trabalho|vaga|renda|servico|trabalhar|dinheiro|carteira assinada)/u', $mensagem)) {
    $categoria_busca = "Emprego";
    $acolhimento = "Ter a sua própria renda é um passo transformador rumo à autonomia. Vamos buscar juntas uma oportunidade! 💼✨";
    $pergunta_seguinte = "Você prefere procurar vagas no PAT/SINE ou cursos de capacitação?";
} 
// Cursos
elseif (preg_match('/(curso|capacita|estudar|qualifica|aprender|aula|estudo)/u', $mensagem)) {
    $categoria_busca = "Emprego";
    $acolhimento = "Investir em conhecimento abre horizontes e fortalece a nossa confiança. É lindo ver você buscando crescer! 📚🌟";
    $pergunta_seguinte = "Você procura por cursos profissionalizantes presenciais ou online?";
} 
// Mães / Filhos
elseif (preg_match('/(filho|filhos|mae|maternidade|mãe solo|crianca|creche)/u', $mensagem)) {
    $acolhimento = "A maternidade e a responsabilidade de criar os filhos exigem uma força extraordinária. Você faz um trabalho incrível! 💜🌸";
    $pergunta_seguinte = "Posso te ajudar a encontrar suporte social ou vagas de emprego com flexibilidade?";
} 
// Geral
else {
    $acolhimento = "Estou aqui com os ouvidos bem abertos para te escutar, seja sobre saúde, trabalho, direitos ou para o que precisar. 💜";
    $pergunta_seguinte = "Para te orientar melhor, qual é a sua principal necessidade neste momento?";
}

// 4. CONSULTA SQL
$where = [];
$params = [];

if (!empty($categoria_busca)) {
    $where[] = "categoria LIKE :cat";
    $params[':cat'] = "%" . $categoria_busca . "%";
}

if (!empty($cidade_busca)) {
    $where[] = "cidade LIKE :cid";
    $params[':cid'] = "%" . $cidade_busca . "%";
}

if (empty($where)) {
    $palavras = explode(' ', $mensagem);
    $conds = [];
    foreach ($palavras as $i => $palavra) {
        if (mb_strlen($palavra, 'UTF-8') > 3 && !in_array($palavra, ['para', 'tenho', 'preciso', 'anos', 'sobre', 'minha', 'com', 'estou', 'voce', 'que', 'onde'])) {
            $pName = ":p" . $i;
            $conds[] = "(nome LIKE $pName OR categoria LIKE $pName OR descricao LIKE $pName OR servicos LIKE $pName OR cidade LIKE $pName)";
            $params[$pName] = "%" . $palavra . "%";
        }
    }
    if (!empty($conds)) {
        $where[] = "(" . implode(' OR ', $conds) . ")";
    }
}

$sql = "SELECT * FROM apoios";
if (!empty($where)) {
    $sql .= " WHERE " . implode(' AND ', $where);
}
$sql .= " LIMIT 4";

$stmt = $pdo->prepare($sql);
foreach ($params as $k => $v) {
    $stmt->bindValue($k, $v, PDO::PARAM_STR);
}
$stmt->execute();
$resultados = $stmt->fetchAll(PDO::FETCH_ASSOC);

if (count($resultados) == 0 && !empty($cidade_busca)) {
    $sqlAlt = "SELECT * FROM apoios WHERE cidade LIKE :cid LIMIT 4";
    $stmtAlt = $pdo->prepare($sqlAlt);
    $stmtAlt->bindValue(':cid', "%" . $cidade_busca . "%", PDO::PARAM_STR);
    $stmtAlt->execute();
    $resultados = $stmtAlt->fetchAll(PDO::FETCH_ASSOC);
}

// 5. RETORNO
echo json_encode([
    'status' => 'sucesso',
    'acolhimento' => $acolhimento,
    'pergunta_seguinte' => $pergunta_seguinte,
    'quantidade' => count($resultados),
    'dados' => $resultados
]);
?>