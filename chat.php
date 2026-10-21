<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Acolhe — Assistente Virtual</title>

    <style>
        :root {
            color-scheme: light;

            --cor-roxa: #8a4baf;
            --cor-roxa-hover: #733c94;

            --fundo-pagina: #f6f2f8;
            --balao-bot: #ffffff;
            --balao-user: #9b59b6;

            --texto-principal: #2b2b2b;
            --texto-secundario: #733c94;

            --borda: #e1d5e7;
            --fundo-rodape: #ffffff;
            --fundo-input: #fdfbfd;
            --fundo-apoio: #ffffff;
            --fundo-pergunta: #f3ebf7;
            --fundo-botao-secundario: #f0e6f5;
        }

        /* =========================
       TEMA ESCURO
    ========================= */

        [data-tema="escuro"] {
            color-scheme: dark;

            --cor-roxa: #c5a0df;
            --cor-roxa-hover: #d8bbed;

            --fundo-pagina: #201a25;
            --balao-bot: #302737;
            --balao-user: #79558f;

            --texto-principal: #f5eff8;
            --texto-secundario: #dfc4f2;

            --borda: #493b50;
            --fundo-rodape: #28212e;
            --fundo-input: #332a3a;
            --fundo-apoio: #302737;
            --fundo-pergunta: #3b2e43;
            --fundo-botao-secundario: #403348;
        }

        /* =========================
       CONFIGURAÇÕES GERAIS
    ========================= */

        * {
            box-sizing: border-box;
        }

        html,
        body {
            height: 100%;
            margin: 0;
            padding: 0;
            background-color: var(--fundo-pagina);
            color: var(--texto-principal);
            font-family: system-ui, -apple-system, sans-serif;
            transition: background-color 0.25s, color 0.25s;
        }

        .chat-layout {
            display: flex;
            flex-direction: column;
            height: 100vh;
            height: 100dvh;
            width: 100%;
            background-color: var(--fundo-pagina);
        }

        /* =========================
       CABEÇALHO
    ========================= */

        .chat-header-amplo {
            background-color: var(--cor-roxa);
            color: white;
            padding: 16px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            transition: background-color 0.25s;
        }

        .chat-header-amplo h2 {
            margin: 0;
            font-size: 22px;
            font-weight: 600;
        }

        .chat-header-amplo small {
            display: inline-block;
            margin-top: 4px;
        }

        [data-tema="escuro"] .chat-header-amplo {
            background-color: #302339;
        }

        .acoes-header {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }

        /* Botão de alternar tema */

        .btn-tema {
            width: 42px;
            height: 42px;
            padding: 0;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.35);
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.14);
            color: white;
            cursor: pointer;
            font-size: 19px;
            transition: background 0.2s, transform 0.2s;
        }

        .btn-tema:hover {
            background: rgba(255, 255, 255, 0.27);
            transform: scale(1.06);
        }

        .btn-tema:focus-visible,
        .btn-voltar-site:focus-visible {
            outline: 2px solid white;
            outline-offset: 3px;
        }

        #texto-tema {
            display: none;
        }

        /* Botão voltar para o site */

        .btn-voltar-site {
            color: white;
            text-decoration: none;
            background: rgba(255, 255, 255, 0.2);
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 14px;
            white-space: nowrap;
            transition: background 0.2s;
        }

        .btn-voltar-site:hover {
            background: rgba(255, 255, 255, 0.3);
            color: white;
        }

        /* =========================
       ÁREA DAS MENSAGENS
    ========================= */

        .chat-body-amplo {
            flex: 1;
            min-height: 0;
            padding: 30px 12%;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 20px;
            background-color: var(--fundo-pagina);
            transition: background-color 0.25s;
        }

        .msg {
            padding: 18px 24px;
            border-radius: 18px;
            font-size: 15.5px;
            max-width: 80%;
            line-height: 1.6;
            overflow-wrap: anywhere;
        }

        .msg-bot {
            background: var(--balao-bot);
            color: var(--texto-principal);
            align-self: flex-start;
            border: 1px solid var(--borda);
            border-bottom-left-radius: 4px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            transition: background-color 0.25s, color 0.25s;
        }

        .msg-user {
            background: var(--balao-user);
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 4px;
        }

        /* =========================
       CARTÕES DE APOIO
    ========================= */

        .bloco-apoio {
            background: var(--fundo-apoio);
            color: var(--texto-principal);
            border-left: 5px solid var(--cor-roxa);
            border-radius: 10px;
            padding: 16px 20px;
            margin-top: 14px;
            border-top: 1px solid var(--borda);
            border-right: 1px solid var(--borda);
            border-bottom: 1px solid var(--borda);
            transition: background-color 0.25s, color 0.25s;
        }

        .bloco-apoio h5 {
            margin: 0 0 8px 0;
            color: var(--cor-roxa);
            font-weight: bold;
            font-size: 18px;
        }

        .bloco-apoio p {
            color: var(--texto-principal);
        }

        .botoes-acao {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-top: 12px;
        }

        /* Botão para abrir o mapa */

        .btn-acao-mapa {
            background-color: var(--cor-roxa);
            color: white !important;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13.5px;
            font-weight: 500;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: background-color 0.2s;
        }

        .btn-acao-mapa:hover {
            background-color: var(--cor-roxa-hover);
        }

        /* Botão para abrir o site do serviço */

        .btn-acao-site {
            background-color: var(--fundo-botao-secundario);
            color: var(--texto-secundario) !important;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13.5px;
            font-weight: 500;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: background-color 0.2s;
        }

        .btn-acao-site:hover {
            background-color: #e2d1eb;
        }

        [data-tema="escuro"] .btn-acao-site:hover {
            background-color: #51405b;
        }

        /* Caixa da pergunta de acompanhamento */

        .pergunta-chat {
            background: var(--fundo-pergunta);
            color: var(--texto-principal);
            padding: 12px 16px;
            border-radius: 10px;
            margin-top: 10px;
            transition: background-color 0.25s, color 0.25s;
        }

        /* =========================
       RODAPÉ E CAMPO DE DIGITAÇÃO
    ========================= */

        .chat-footer-amplo {
            padding: 20px 12%;
            background: var(--fundo-rodape);
            border-top: 1px solid var(--borda);
            display: flex;
            align-items: center;
            transition: background-color 0.25s;
        }

        .chat-footer-amplo input {
            flex: 1;
            min-width: 0;
            border: 1px solid var(--borda);
            border-radius: 30px;
            padding: 14px 24px;
            font-size: 16px;
            outline: none;
            background: var(--fundo-input);
            color: var(--texto-principal);
            transition: background-color 0.25s, border-color 0.2s;
        }

        .chat-footer-amplo input::placeholder {
            color: #8c8291;
        }

        [data-tema="escuro"] .chat-footer-amplo input::placeholder {
            color: #c5b6cc;
        }

        .chat-footer-amplo input:focus {
            border-color: var(--cor-roxa);
        }

        .chat-footer-amplo button {
            background: var(--cor-roxa);
            color: white;
            border: none;
            border-radius: 50%;
            width: 52px;
            height: 52px;
            margin-left: 14px;
            flex-shrink: 0;
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background-color 0.2s;
        }

        .chat-footer-amplo button:hover {
            background: var(--cor-roxa-hover);
        }

        /* =========================
       AJUSTES PARA CELULAR
    ========================= */

        @media (max-width: 700px) {
            .chat-header-amplo {
                padding: 14px 16px;
                gap: 10px;
            }

            .chat-header-amplo h2 {
                font-size: 18px;
            }

            .chat-header-amplo small {
                font-size: 11px;
            }

            .acoes-header {
                gap: 8px;
            }

            .btn-tema {
                width: 38px;
                height: 38px;
                font-size: 17px;
            }

            .btn-voltar-site {
                padding: 8px 11px;
                font-size: 12px;
            }

            .chat-body-amplo {
                padding: 20px 16px;
                gap: 16px;
            }

            .msg {
                max-width: 92%;
                padding: 14px 16px;
                font-size: 14.5px;
            }

            .bloco-apoio {
                padding: 14px;
            }

            .chat-footer-amplo {
                padding: 14px 16px;
            }

            .chat-footer-amplo input {
                padding: 12px 16px;
                font-size: 14px;
            }

            .chat-footer-amplo button {
                width: 44px;
                height: 44px;
                margin-left: 8px;
            }
        }

        @media (max-width: 400px) {
            .chat-header-amplo {
                padding: 12px;
            }

            .chat-header-amplo h2 {
                font-size: 16px;
            }

            .btn-voltar-site {
                padding: 7px 9px;
                font-size: 11px;
            }
        }
    </style>


</head>

<body>

    <div class="chat-layout">
        <div class="chat-header-amplo">
            <div>
                <h2>💜 Assistente Acolhe</h2>
                <small style="opacity: 0.9;">Espaço de escuta, orientação e apoio</small>
            </div>

            <div class="acoes-header">
                <button type="button" id="btn-tema" class="btn-tema" aria-label="Ativar tema escuro"
                    aria-pressed="false">
                    <span id="icone-tema">🌙</span>
                    <span id="texto-tema">Tema escuro</span>
                </button>

                <a href="index.php" class="btn-voltar-site">
                    ← Voltar para o Site
                </a>
            </div>

        </div>

        <div id="chat-body" class="chat-body-amplo">
            <div class="msg msg-bot">
                Olá! Seja muito bem-vinda ao nosso espaço seguro. 💜<br>
                Eu sou a <strong>Acolhe</strong>. Estou aqui para te orientar sobre cursos, vagas de emprego,
                assistência social, saúde e apoio jurídico.<br><br>
                Pode me contar livremente o que você precisa no momento ou qual a sua cidade!
            </div>
        </div>

        <form id="chat-form" class="chat-footer-amplo">
            <input type="text" id="chat-input" placeholder="Escreva aqui a sua dúvida ou necessidade..."
                autocomplete="off" required>
            <button type="submit">➢</button>
        </form>
    </div>

    <script>
        const chatBody = document.getElementById('chat-body');
        const form = document.getElementById('chat-form');
        const input = document.getElementById('chat-input');


        const botaoTema = document.getElementById('btn-tema');
        const iconeTema = document.getElementById('icone-tema');
        const textoTema = document.getElementById('texto-tema');

        function aplicarTema(tema) {
            document.documentElement.setAttribute('data-tema', tema);

            const escuro = tema === 'escuro';

            iconeTema.textContent = escuro ? '🌙' : '☀️';
            textoTema.textContent = escuro ? 'Tema claro' : 'Tema escuro';

            botaoTema.setAttribute(
                'aria-label',
                escuro ? 'Ativar tema claro' : 'Ativar tema escuro'
            );

            botaoTema.setAttribute('aria-pressed', String(escuro));
        }

        const temaSalvo = localStorage.getItem('tema-acolhe');
        aplicarTema(temaSalvo === 'escuro' ? 'escuro' : 'claro');

        botaoTema.addEventListener('click', () => {
            const temaAtual =
                document.documentElement.getAttribute('data-tema');

            const novoTema = temaAtual === 'escuro' ? 'claro' : 'escuro';

            aplicarTema(novoTema);
            localStorage.setItem('tema-acolhe', novoTema);
        });


        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const mensagem = input.value.trim();
            if (!mensagem) return;

            adicionarMensagem(mensagem, 'user');
            input.value = '';

            const idTemp = 'loading-' + Date.now();
            adicionarMensagem("Acolhe está ouvindo e buscando as melhores opções para você...", 'bot', idTemp);

            try {
                const resposta = await fetch('conexao_chat.php', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ mensagem: mensagem })
                });

                const dados = await resposta.json();
                document.getElementById(idTemp)?.remove();

                if (dados.status === 'mensagem_especial') {
                    adicionarMensagem(dados.resposta, 'bot', null, true);
                }
                else if (dados.status === 'sucesso') {
                    let htmlResposta = `${dados.acolhimento}<br><br>Encontrei ${dados.quantidade} local(is) na nossa rede de apoio que correspondem ao que você procura:<br>`;

                    dados.dados.forEach(item => {
                        let linkMapa = "";
                        if (item.latitude && item.longitude) {
                            linkMapa = `https://www.google.com/maps/dir/?api=1&destination=${item.latitude},${item.longitude}`;
                        } else if (item.endereco) {
                            linkMapa = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(item.nome + ' ' + item.endereco + ' ' + item.cidade)}`;
                        }

                        htmlResposta += `
                            <div class="bloco-apoio">
                                <h5>${item.nome}</h5>
                                <strong>Categoria:</strong> ${item.categoria} ${item.tipo ? '(' + item.tipo + ')' : ''}<br>
                                ${item.servicos ? `<strong>O que oferece:</strong> ${item.servicos}<br>` : ''}
                                ${item.cidade ? `<strong>Cidade:</strong> ${item.cidade}<br>` : ''}
                                ${item.endereco ? `<strong>Endereço:</strong> ${item.endereco}<br>` : ''}
                                ${item.telefone ? `<strong>Telefone:</strong> ${item.telefone}<br>` : ''}

                                <div class="botoes-acao">
                                    ${linkMapa ? `<a href="${linkMapa}" target="_blank" class="btn-acao-mapa">📍 Como Chegar (Ver no Mapa)</a>` : ''}
                                    <a href="index.php#rede-apoio" class="btn-acao-site">🔍 Ver mais locais no site</a>
                                </div>
                            </div>
                        `;
                    });

                    if (dados.pergunta_seguinte) {
                        htmlResposta += `<br><div style="background: #f3ebf7; padding: 12px 16px; border-radius: 10px; margin-top: 10px;"><strong>💬 Pergunta:</strong> ${dados.pergunta_seguinte}</div>`;
                    }

                    adicionarMensagem(htmlResposta, 'bot', null, true);
                }
                else {
                    adicionarMensagem(dados.resposta, 'bot', null, true);
                }

            } catch (erro) {
                document.getElementById(idTemp)?.remove();
                adicionarMensagem("Tive um pequeno imprevisto de conexão. Pode tentar me mandar a mensagem novamente?", 'bot');
            }
        });

        function adicionarMensagem(texto, tipo, id = null, ehHtml = false) {
            const div = document.createElement('div');
            div.className = `msg msg-${tipo}`;
            if (id) div.id = id;

            if (ehHtml) {
                div.innerHTML = texto;
            } else {
                div.textContent = texto;
            }

            chatBody.appendChild(div);
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    </script>
</body>

</html>