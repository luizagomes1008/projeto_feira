<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#8a4baf">
    <title>Acolhe — Assistente Virtual</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        :root {
            color-scheme: light;
            --cor-roxa: #8a4baf;
            --cor-roxa-hover: #733c94;
            --cor-roxa-clara: #f0e6f7;
            --fundo-pagina: #f8f5fa;
            --balao-bot: #fff;
            --balao-user: #8a4baf;
            --texto-principal: #302936;
            --texto-secundario: #76538a;
            --borda: #e7ddec;
            --fundo-rodape: #fff;
            --fundo-input: #fdfbfd;
            --fundo-apoio: #fff;
            --fundo-pergunta: #f3ebf7;
            --fundo-botao-secundario: #f0e6f5;
            --sombra: 0 4px 18px rgba(65,35,80,.06);
        }

        [data-tema="escuro"] {
            color-scheme: dark;
            --cor-roxa: #b995d4;
            --cor-roxa-hover: #c9a9df;
            --cor-roxa-clara: #403047;
            --fundo-pagina: #211a26;
            --balao-bot: #302637;
            --balao-user: #76518d;
            --texto-principal: #f5edf8;
            --texto-secundario: #dfc5f0;
            --borda: #49394f;
            --fundo-rodape: #28202e;
            --fundo-input: #342a3b;
            --fundo-apoio: #302637;
            --fundo-pergunta: #3c2e45;
            --fundo-botao-secundario: #403047;
            --sombra: 0 4px 18px rgba(0,0,0,.15);
        }

        * { box-sizing: border-box; }
        html, body { width:100%; height:100%; margin:0; padding:0; font-family:system-ui,-apple-system,BlinkMacSystemFont,sans-serif; background:var(--fundo-pagina); color:var(--texto-principal); }
        body { overflow:hidden; transition:background-color .25s,color .25s; }
        a { overflow-wrap:anywhere; }
        button, input { font:inherit; }
        .chat-layout { display:flex; flex-direction:column; height:100vh; height:100dvh; width:100%; background:var(--fundo-pagina); }
        .chat-header-amplo { background:var(--cor-roxa); color:#fff; padding:16px 32px; display:flex; justify-content:space-between; align-items:center; gap:16px; box-shadow:0 3px 12px rgba(0,0,0,.08); flex-shrink:0; }
        [data-tema="escuro"] .chat-header-amplo { background:#302339; }
        .identidade-acolhe { display:flex; align-items:center; gap:12px; min-width:0; }
        .icone-acolhe { width:46px; height:46px; display:flex; align-items:center; justify-content:center; flex-shrink:0; border-radius:50%; background:rgba(255,255,255,.16); font-size:23px; }
        .chat-header-amplo h2 { margin:0; font-size:21px; font-weight:700; }
        .chat-header-amplo small { display:block; margin-top:4px; opacity:.9; font-size:12px; }
        .acoes-header { display:flex; align-items:center; gap:10px; flex-shrink:0; }
        .btn-tema { width:42px; height:42px; display:inline-flex; align-items:center; justify-content:center; border:1px solid rgba(255,255,255,.3); border-radius:50%; background:rgba(255,255,255,.13); color:#fff; cursor:pointer; font-size:19px; transition:background .2s,transform .2s; }
        .btn-tema:hover { background:rgba(255,255,255,.25); transform:rotate(-8deg); }
        .btn-voltar-site { color:#fff; text-decoration:none; background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.2); padding:9px 15px; border-radius:22px; font-size:13px; white-space:nowrap; }
        .btn-voltar-site:hover { background:rgba(255,255,255,.27); color:#fff; }
        .btn-tema:focus-visible,.btn-voltar-site:focus-visible { outline:2px solid white; outline-offset:3px; }
        .chat-body-amplo { flex:1; min-height:0; padding:28px max(6%,calc((100% - 950px)/2)); overflow-y:auto; display:flex; flex-direction:column; gap:17px; background:var(--fundo-pagina); scroll-behavior:smooth; }
        .msg { max-width:84%; padding:16px 20px; border-radius:18px; font-size:14.5px; line-height:1.75; overflow-wrap:anywhere; animation:aparecer .22s ease-out; }
        @keyframes aparecer { from {opacity:0;transform:translateY(6px)} to {opacity:1;transform:translateY(0)} }
        .msg-bot { align-self:flex-start; background:var(--balao-bot); color:var(--texto-principal); border:1px solid var(--borda); border-bottom-left-radius:5px; box-shadow:var(--sombra); }
        .msg-user { align-self:flex-end; background:var(--balao-user); color:#fff; border-bottom-right-radius:5px; white-space:pre-wrap; }
        .mensagem-boas-vindas { border-left:4px solid var(--cor-roxa); }
        .msg a:not(.btn-acao-mapa):not(.btn-acao-site) { color:var(--texto-secundario); }
        .bloco-apoio { background:var(--fundo-apoio); color:var(--texto-principal); border:1px solid var(--borda); border-left:4px solid var(--cor-roxa); border-radius:12px; padding:17px; margin-top:15px; box-shadow:var(--sombra); }
        .bloco-apoio h5 { color:var(--cor-roxa); font-weight:700; font-size:16px; line-height:1.5; margin:0 0 8px; }
        .bloco-apoio small { display:block; color:var(--texto-secundario); margin-bottom:8px; }
        .bloco-apoio p { margin:7px 0; color:var(--texto-principal); font-size:13.5px; line-height:1.7; }
        .botoes-acao { display:flex; flex-wrap:wrap; gap:9px; margin-top:14px; }
        .btn-acao-mapa,.btn-acao-site { display:inline-flex; align-items:center; justify-content:center; gap:6px; padding:9px 13px; border-radius:22px; font-size:12.5px; font-weight:600; line-height:1.4; text-decoration:none; transition:background-color .2s,transform .2s; cursor:pointer; }
        .btn-acao-mapa { background:var(--cor-roxa); color:#fff!important; }
        .btn-acao-mapa:hover { background:var(--cor-roxa-hover); color:#fff!important; transform:translateY(-2px); }
        .btn-acao-site { background:var(--fundo-botao-secundario); color:var(--texto-secundario)!important; border:1px solid var(--borda); }
        .btn-acao-site:hover { background:var(--cor-roxa-clara); transform:translateY(-2px); }
        .pergunta-chat { background:var(--fundo-pergunta); color:var(--texto-principal); border-radius:11px; padding:13px 15px; margin-top:16px; border:1px solid var(--borda); font-size:13.5px; }
        .tela-inicial-acolhe { width:100%; max-width:680px; margin:auto; padding:10px 0; }
        .tela-inicial-acolhe h3 { color:var(--cor-roxa); font-size:23px; font-weight:700; margin-bottom:12px; }
        .tela-inicial-acolhe p { color:var(--texto-principal); font-size:14px; line-height:1.8; }
        .opcoes-acolhe { display:grid; grid-template-columns:1fr; gap:12px; margin-top:24px; }
        .btn-opcao-acolhe { display:flex; align-items:center; gap:14px; width:100%; padding:17px; text-align:left; color:var(--texto-principal); background:var(--balao-bot); border:1px solid var(--borda); border-radius:16px; cursor:pointer; transition:border-color .2s,transform .2s,background-color .2s; }
        .btn-opcao-acolhe:hover { border-color:var(--cor-roxa); background:var(--cor-roxa-clara); transform:translateY(-2px); }
        .btn-opcao-acolhe:focus-visible { outline:2px solid var(--cor-roxa); outline-offset:3px; }
        .icone-opcao-acolhe { display:flex; align-items:center; justify-content:center; flex-shrink:0; width:46px; height:46px; border-radius:14px; background:var(--cor-roxa-clara); font-size:23px; }
        .texto-opcao-acolhe strong { display:block; color:var(--cor-roxa); font-size:14px; margin-bottom:4px; }
        .texto-opcao-acolhe small { display:block; color:var(--texto-secundario); font-size:12px; line-height:1.6; }
        .chat-footer-amplo { padding:17px max(6%,calc((100% - 950px)/2)); background:var(--fundo-rodape); border-top:1px solid var(--borda); display:flex; align-items:center; gap:11px; flex-shrink:0; }
        .chat-footer-amplo input { flex:1; min-width:0; border:1px solid var(--borda); border-radius:28px; padding:13px 19px; font-size:14px; outline:none; background:var(--fundo-input); color:var(--texto-principal); }
        .chat-footer-amplo input::placeholder { color:#93869a; }
        [data-tema="escuro"] .chat-footer-amplo input::placeholder { color:#c2b1ca; }
        .chat-footer-amplo input:focus { border-color:var(--cor-roxa); box-shadow:0 0 0 3px rgba(138,75,175,.12); }
        .chat-footer-amplo button { width:47px; height:47px; flex-shrink:0; display:flex; align-items:center; justify-content:center; background:var(--cor-roxa); color:#fff; border:0; border-radius:50%; cursor:pointer; font-size:20px; }
        .chat-footer-amplo button:hover { background:var(--cor-roxa-hover); }
        .chat-footer-amplo button:disabled { opacity:.6; cursor:wait; }
        .aviso-chat { padding:0 16px 12px; text-align:center; color:var(--texto-secundario); background:var(--fundo-rodape); font-size:10.5px; flex-shrink:0; }
        @media(max-width:650px) {
            .chat-header-amplo { padding:13px 14px; gap:8px; }
            .identidade-acolhe { gap:8px; }
            .icone-acolhe { width:37px; height:37px; font-size:19px; }
            .chat-header-amplo h2 { font-size:16px; }
            .chat-header-amplo small { font-size:10px; }
            .acoes-header { gap:7px; }
            .btn-tema { width:36px; height:36px; font-size:16px; }
            .btn-voltar-site { padding:8px 9px; font-size:10px; }
            .chat-body-amplo { padding:18px 12px; gap:13px; }
            .msg { max-width:96%; padding:13px 14px; font-size:13.5px; }
            .bloco-apoio { padding:13px; }
            .botoes-acao { gap:7px; }
            .btn-acao-mapa,.btn-acao-site { padding:8px 10px; font-size:11px; }
            .chat-footer-amplo { padding:12px; gap:8px; }
            .chat-footer-amplo input { padding:12px 14px; font-size:13px; }
            .chat-footer-amplo button { width:43px; height:43px; }
            .tela-inicial-acolhe h3 { font-size:20px; }
            .btn-opcao-acolhe { padding:13px; gap:11px; }
            .icone-opcao-acolhe { width:40px; height:40px; font-size:20px; }
        }
        @media(prefers-reduced-motion:reduce) {
            *,*::before,*::after { animation-duration:.01ms!important; transition-duration:.01ms!important; scroll-behavior:auto!important; }
        }
    </style>
</head>
<body>
<div class="chat-layout">
    <header class="chat-header-amplo">
        <div class="identidade-acolhe">
            <div class="icone-acolhe" aria-hidden="true">💜</div>
            <div>
                <h2>Assistente Acolhe</h2>
                <small>Um espaço de escuta, orientação e apoio</small>
            </div>
        </div>
        <div class="acoes-header">
            <button type="button" id="btn-tema" class="btn-tema" aria-label="Ativar tema escuro" aria-pressed="false" title="Alternar tema">
                <span id="icone-tema" aria-hidden="true">🌙</span>
            </button>
            <a href="index.html" class="btn-voltar-site">← Voltar ao site</a>
        </div>
    </header>

    <main id="chat-body" class="chat-body-amplo" aria-live="polite">
        <div id="inicio-acolhe" class="tela-inicial-acolhe">
            <h3>Olá, seja muito bem-vinda! 💜</h3>
            <p>Eu sou a <strong>Acolhe</strong>, uma assistente virtual criada para ouvir você e ajudar a encontrar caminhos de apoio.</p>
            <p>Você não precisa saber exatamente o que dizer. Podemos começar do seu jeito, sem pressa. 🌷</p>
            <div class="opcoes-acolhe">
                <button type="button" class="btn-opcao-acolhe" data-modo="desabafar">
                    <span class="icone-opcao-acolhe">💜</span>
                    <span class="texto-opcao-acolhe"><strong>Quero desabafar</strong><small>Quero falar sobre o que estou sentindo.</small></span>
                </button>
                <button type="button" class="btn-opcao-acolhe" data-modo="ajuda">
                    <span class="icone-opcao-acolhe">🤝</span>
                    <span class="texto-opcao-acolhe"><strong>Preciso de ajuda</strong><small>Quero encontrar cursos, emprego ou serviços.</small></span>
                </button>
                <button type="button" class="btn-opcao-acolhe" data-modo="conversar">
                    <span class="icone-opcao-acolhe">🌷</span>
                    <span class="texto-opcao-acolhe"><strong>Só quero conversar</strong><small>Quero começar com calma, sem um assunto definido.</small></span>
                </button>
            </div>
            <p style="margin-top:20px;font-size:12px;">Se preferir, escreva sua mensagem diretamente no campo abaixo.</p>
        </div>
    </main>

    <form id="chat-form" class="chat-footer-amplo">
        <input type="text" id="chat-input" placeholder="Pode me contar o que você precisa..." autocomplete="off" maxlength="1500" aria-label="Digite sua mensagem" required>
        <button type="submit" id="btn-enviar" aria-label="Enviar mensagem">➤</button>
    </form>
    <div class="aviso-chat">O Acolhe é uma assistente virtual e pode cometer erros. Em situações urgentes, procure os serviços oficiais de emergência.</div>
</div>

<script>
'use strict';

const chatBody = document.getElementById('chat-body');
const form = document.getElementById('chat-form');
const input = document.getElementById('chat-input');
const botaoEnviar = document.getElementById('btn-enviar');
const botaoTema = document.getElementById('btn-tema');
const iconeTema = document.getElementById('icone-tema');

let modoConversa = null;
let enviando = false;

const opcoesConversa = {
    desabafar: {
        mensagem: 'Pode falar no seu tempo. 💜 Não precisa organizar tudo nem contar nada que não queira. O que está passando pela sua cabeça hoje?',
        placeholder: 'Pode desabafar comigo...'
    },
    ajuda: {
        mensagem: 'Claro! 💜 Vou ajudar você a encontrar caminhos e serviços. Você procura emprego, cursos, renda, saúde, assistência social ou outro tipo de apoio?',
        placeholder: 'Conte de que tipo de ajuda precisa...'
    },
    conversar: {
        mensagem: 'Claro! 🌷 Podemos conversar com calma, sem precisar falar sobre problemas. Como foi seu dia?',
        placeholder: 'Vamos conversar...'
    }
};

/* Tema: usa os mesmos IDs e o mesmo atributo do CSS. */
function aplicarTema(tema) {
    const escuro = tema === 'escuro';
    document.documentElement.setAttribute('data-tema', escuro ? 'escuro' : 'claro');
    iconeTema.textContent = escuro ? '☀️' : '🌙';
    botaoTema.setAttribute('aria-label', escuro ? 'Ativar tema claro' : 'Ativar tema escuro');
    botaoTema.setAttribute('aria-pressed', String(escuro));
    localStorage.setItem('tema-acolhe', tema);
}
aplicarTema(localStorage.getItem('tema-acolhe') || 'claro');
botaoTema.addEventListener('click', () => {
    const atual = document.documentElement.getAttribute('data-tema');
    aplicarTema(atual === 'escuro' ? 'claro' : 'escuro');
});

function escaparHTML(texto) {
    return String(texto ?? '').replace(/[&<>"']/g, c => ({
        '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#039;'
    })[c]);
}
function normalizarTexto(texto) {
    return String(texto ?? '').toLowerCase().normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '').trim();
}
function rolarChat() {
    chatBody.scrollTop = chatBody.scrollHeight;
}
function adicionarMensagem(texto, tipo = 'bot') {
    const elemento = document.createElement('div');
    elemento.className = tipo === 'user' ? 'msg msg-user' : 'msg msg-bot';
    elemento.textContent = String(texto ?? '');
    chatBody.appendChild(elemento);
    rolarChat();
}
function adicionarHTMLSeguro(html) {
    const elemento = document.createElement('div');
    elemento.className = 'msg msg-bot';
    elemento.innerHTML = html;
    chatBody.appendChild(elemento);
    rolarChat();
}
function iniciarConversa(modo) {
    if (!opcoesConversa[modo]) return;
    modoConversa = modo;
    document.getElementById('inicio-acolhe')?.remove();
    document.getElementById('botao-voltar-modos')?.remove();
    adicionarMensagem(opcoesConversa[modo].mensagem);
    input.placeholder = opcoesConversa[modo].placeholder;
    input.focus();
    mostrarBotaoVoltar();
}
function mostrarOpcoes() {
    modoConversa = null;
    document.getElementById('inicio-acolhe')?.remove();
    document.getElementById('botao-voltar-modos')?.remove();

    const tela = document.createElement('div');
    tela.id = 'inicio-acolhe';
    tela.className = 'tela-inicial-acolhe';
    tela.innerHTML = `
        <h3>Como você gostaria de continuar? 💜</h3>
        <p>Escolha o tipo de conversa que faz mais sentido para você.</p>
        <div class="opcoes-acolhe">
            <button type="button" class="btn-opcao-acolhe" data-modo="desabafar"><span class="icone-opcao-acolhe">💜</span><span class="texto-opcao-acolhe"><strong>Quero desabafar</strong><small>Quero falar sobre o que estou sentindo.</small></span></button>
            <button type="button" class="btn-opcao-acolhe" data-modo="ajuda"><span class="icone-opcao-acolhe">🤝</span><span class="texto-opcao-acolhe"><strong>Preciso de ajuda</strong><small>Quero encontrar cursos, emprego ou serviços.</small></span></button>
            <button type="button" class="btn-opcao-acolhe" data-modo="conversar"><span class="icone-opcao-acolhe">🌷</span><span class="texto-opcao-acolhe"><strong>Só quero conversar</strong><small>Quero conversar sem um assunto definido.</small></span></button>
        </div>`;
    chatBody.appendChild(tela);
    input.placeholder = 'Escolha uma opção ou escreva sua mensagem...';
    rolarChat();
}
function mostrarBotaoVoltar() {
    document.getElementById('botao-voltar-modos')?.remove();
    const area = document.createElement('div');
    area.id = 'botao-voltar-modos';
    area.className = 'botoes-acao';
    const botao = document.createElement('button');
    botao.type = 'button';
    botao.className = 'btn-acao-site';
    botao.textContent = '🌷 Voltar às opções';
    botao.addEventListener('click', mostrarOpcoes);
    area.appendChild(botao);
    chatBody.appendChild(area);
    rolarChat();
}

/* Delegação permite que os botões continuem funcionando após voltar. */
chatBody.addEventListener('click', evento => {
    const botao = evento.target.closest('[data-modo]');
    if (botao) iniciarConversa(botao.dataset.modo);
});

const respostasConversa = {
    saudacao: [
        'Oi! 💜 Que bom conversar com você. Como você está hoje?',
        'Oii! 🌷 Como foi seu dia?',
        'Olá! Pode ficar à vontade. O que gostaria de me contar?'
    ],
    tristeza: [
        'Sinto muito que você esteja se sentindo assim. 💜 Quer me contar um pouco mais?',
        'Imagino que não esteja sendo fácil. O que mais está pesando para você?',
        'Obrigada por compartilhar isso comigo. Como você tem lidado com essa situação?'
    ],
    cansaco: [
        'Parece que você está carregando muita coisa ao mesmo tempo. Você tem conseguido descansar?',
        'Você também merece um tempo para si. O que tem deixado seus dias tão cansativos?',
        'Imagino que esteja sendo puxado. Quer me contar o que está acontecendo?'
    ],
    ansiedade: [
        'Vamos com calma, uma coisa de cada vez. 💜 O que está preocupando você?',
        'Deve ser difícil lidar com tantos pensamentos. Quer me contar mais?',
        'O que está deixando você mais apreensiva neste momento?'
    ],
    felicidade: [
        'Que notícia boa! 💗 Me conta mais!',
        'Aaa, que bom! O que aconteceu?',
        'Fico feliz que você queira compartilhar isso. O que deixou seu dia melhor?'
    ],
    agradecimento: [
        'Você não precisa agradecer. 💜 Podemos continuar conversando.',
        'Fico feliz em poder conversar com você. 🌷',
        'Por nada! Como você está se sentindo agora?'
    ],
    geral: [
        'Entendi. 💜 Quer me contar um pouco mais?',
        'E como você se sentiu nessa situação?',
        'Pode continuar, estou aqui para conversar com você. 🌷',
        'O que você acha que mais precisa neste momento?',
        'O que aconteceu depois?',
        'Quero entender melhor. Pode me explicar um pouquinho mais?'
    ]
};
function escolherResposta(lista) {
    return lista[Math.floor(Math.random() * lista.length)];
}
function identificarConversa(mensagem) {
    const texto = normalizarTexto(mensagem);
    if (/\b(oi|ola|bom dia|boa tarde|boa noite|eai|e ai)\b/.test(texto)) return 'saudacao';
    if (/\b(obrigada|obrigado|valeu|agradeco|agradecida|agradecido)\b/.test(texto)) return 'agradecimento';
    if (/\b(feliz|felicidade|contente|consegui|conquista|deu certo)\b/.test(texto)) return 'felicidade';
    if (/\b(ansiosa|ansioso|ansiedade|preocupada|preocupado|nervosa|nervoso|medo|aflita|aflito)\b/.test(texto)) return 'ansiedade';
    if (/\b(cansada|cansado|exausta|exausto|esgotada|esgotado|sobrecarregada|sobrecarregado|sem energia)\b/.test(texto)) return 'cansaco';
    if (/\b(triste|tristeza|sozinha|sozinho|chorar|chorei|desanimada|desanimado|dificil|machucada|machucado)\b/.test(texto)) return 'tristeza';
    return 'geral';
}
function identificarSituacaoUrgente(mensagem) {
    const texto = normalizarTexto(mensagem);
    return /\b(violencia|agressao|me bateu|me ameacou|estou em perigo|quero me matar|vou me matar|nao quero mais viver|quero morrer|me machucar|me ferir)\b/.test(texto);
}
function responderConversa(mensagem) {
    if (identificarSituacaoUrgente(mensagem)) {
        return 'Sinto muito que você esteja passando por isso. 💜 Sua segurança importa. Se houver perigo imediato, procure um lugar seguro e ligue para o 190. Se estiver pensando em se machucar, procure alguém de confiança que possa ficar com você e ajudar. Você está em segurança neste momento?';
    }
    return escolherResposta(respostasConversa[identificarConversa(mensagem)]);
}

/* Gera um cartão com os campos que o PHP retornar. */
function criarCartaoApoio(item) {
    const nome = escaparHTML(item.nome || item.titulo || 'Serviço de apoio');
    const categoria = escaparHTML(item.categoria || 'Rede de apoio');
    const descricao = escaparHTML(item.descricao || item.descricao_servico || '');
    const enderecoOriginal = String(item.endereco || item.endereco_completo || item.localizacao || '');
    const endereco = escaparHTML(enderecoOriginal);
    const telefone = escaparHTML(item.telefone || '');
    const linkOriginal = String(item.link || item.site || item.url || '');
    const latitude = Number(item.latitude ?? item.lat);
    const longitude = Number(item.longitude ?? item.lng ?? item.lon);

    let rota = '';
    if (enderecoOriginal.trim()) {
        if ((item.latitude != null || item.lat != null) &&
            Number.isFinite(latitude) && Number.isFinite(longitude) &&
            Math.abs(latitude) <= 90 && Math.abs(longitude) <= 180) {
            rota = `https://www.google.com/maps/dir/?api=1&destination=${latitude},${longitude}`;
        } else {
            rota = `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(enderecoOriginal)}`;
        }
    }

    let html = `<div class="bloco-apoio">
        <h5>${nome}</h5><small>${categoria}</small>
        ${descricao ? `<p>${descricao}</p>` : ''}
        ${endereco ? `<p>📍 ${endereco}</p>` : ''}
        ${telefone ? `<p>☎️ ${telefone}</p>` : ''}
        <div class="botoes-acao">`;

    if (rota) {
        html += `<a class="btn-acao-mapa" href="${rota}" target="_blank" rel="noopener noreferrer">📍 Como chegar</a>`;
    }
    if (/^https?:\/\//i.test(linkOriginal)) {
        // O link precisa ser HTTP(S); o texto do link é escapado.
        html += `<a class="btn-acao-site" href="${escaparHTML(linkOriginal)}" target="_blank" rel="noopener noreferrer">🔗 Acessar serviço</a>`;
    }

    // Este botão aparece em cada cartão e leva à rede de apoio do site.
    html += `<a class="btn-acao-site" href="index.html#rede-apoio">🔍 Ver mais locais no site</a>`;
    html += '</div></div>';
    return html;
}

/* Os dois botões de navegação aparecem mesmo quando há resultados. */
function mostrarBotoesApoio(mensagem) {
    const consulta = encodeURIComponent(mensagem + ' serviço de apoio à mulher Brasil');
    adicionarHTMLSeguro(`
        <div class="botoes-acao">
            <a href="auxilio.html" class="btn-acao-site">💜 Ver rede de apoio</a>
            <a href="https://www.google.com/search?q=${consulta}" target="_blank" rel="noopener noreferrer" class="btn-acao-site">🌐 Pesquisar na internet</a>
        </div>
    `);
}

/* Envio de mensagens. */
form.addEventListener('submit', async evento => {
    evento.preventDefault();
    if (enviando) return;

    const mensagem = input.value.trim();
    if (!mensagem) return;

    // Se a pessoa digitar sem escolher um modo, inicia a conversa livre.
    if (!modoConversa) {
        document.getElementById('inicio-acolhe')?.remove();
        modoConversa = 'conversar';
    }

    adicionarMensagem(mensagem, 'user');
    input.value = '';
    enviando = true;
    input.disabled = true;
    botaoEnviar.disabled = true;

    try {
        if (modoConversa === 'desabafar' || modoConversa === 'conversar') {
            await new Promise(resolve => setTimeout(resolve, 350));
            adicionarMensagem(responderConversa(mensagem), 'bot');
            return;
        }

        if (modoConversa === 'ajuda') {
            const respostaPHP = await fetch('conexao_chat.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({mensagem})
            });

            if (!respostaPHP.ok) throw new Error('Falha ao consultar os serviços.');

            const dados = await respostaPHP.json();

            if (dados.status === 'mensagem_especial') {
                adicionarMensagem(dados.resposta || 'Estou aqui para ajudar você. 💜');
                mostrarBotoesApoio(mensagem);
                return;
            }

            if (dados.status !== 'sucesso') {
                adicionarMensagem('Não consegui consultar os serviços agora. Tente novamente em alguns instantes. 💜');
                mostrarBotoesApoio(mensagem);
                return;
            }

            if (dados.acolhimento) adicionarMensagem(dados.acolhimento);

            const lista = Array.isArray(dados.dados) ? dados.dados : [];

            if (lista.length > 0) {
                adicionarHTMLSeguro(`
                    <p>💜 Encontrei ${lista.length} ${lista.length === 1 ? 'opção' : 'opções'} que podem ajudar você:</p>
                    ${lista.map(criarCartaoApoio).join('')}
                `);
            } else {
                adicionarHTMLSeguro(`
                    <div class="pergunta-chat">
                        <strong>🌷 Vamos tentar outro caminho?</strong>
                        <p>Não encontrei um serviço correspondente na nossa base de dados desta vez. Isso não significa que não exista ajuda disponível.</p>
                    </div>
                `);
            }

            mostrarBotoesApoio(mensagem);

            if (dados.pergunta_seguinte) adicionarMensagem(dados.pergunta_seguinte);
        }
    } catch (erro) {
        console.error('Erro na conversa:', erro);
        adicionarMensagem(
            modoConversa === 'ajuda'
                ? 'Tive um problema ao procurar os serviços. Confira se o XAMPP está ligado e tente novamente. 💜'
                : 'Desculpe, não consegui responder agora. Pode tentar escrever novamente?',
            'bot'
        );
        if (modoConversa === 'ajuda') mostrarBotoesApoio(mensagem);
    } finally {
        enviando = false;
        input.disabled = false;
        botaoEnviar.disabled = false;
        input.focus();
    }
});
</script>
</body>
</html>
