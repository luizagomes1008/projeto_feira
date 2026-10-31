// ==========================================
// MAPA DE REDE DE APOIO
// ==========================================

// Criando o mapa
const mapa = new maplibregl.Map({
    container: 'mapa',

    // Estilo do mapa
    style: 'https://tiles.openfreemap.org/styles/liberty',

    // Centro inicial - Ribeirão Pires
    center: [-46.4133, -23.7104],

    // Zoom inicial
    zoom: 11
});


// ==========================================
// CONTROLES DO MAPA
// ==========================================

mapa.addControl(
    new maplibregl.NavigationControl(),
    'top-right'
);


// ==========================================
// VARIÁVEIS
// ==========================================

let locais = [];
let marcadores = [];


// ==========================================
// ÍCONES DAS CATEGORIAS
// ==========================================

const icones = {
    "ONG": "♡",
    "Assistência Social": "✦",
    "Saúde": "+",
    "Jurídico": "§",
    "Emprego": "↗"
};


// ==========================================
// CARREGAR LOCAIS DO BANCO DE DADOS
// ==========================================

async function carregarLocais() {

    try {

        const resposta = await fetch('buscar_apoios.php');

        if (!resposta.ok) {
            throw new Error('Erro ao buscar os apoios.');
        }

        locais = await resposta.json();

        console.log('Locais carregados:', locais);

    } catch (erro) {

        console.error('Erro ao carregar os locais:', erro);

    }

}


// ==========================================
// CRIAR MARCADOR
// ==========================================

function criarMarcador(local) {

    let botaoAcao = '';


    // ======================================
    // ATENDIMENTO ONLINE
    // ======================================

    if (
        local.tipo === 'Atendimento online' ||
        local.tipo === 'Atuação online'
    ) {

        if (local.site) {

            botaoAcao = `
                <a
                    class="botao-rota"
                    href="${local.site}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Acessar site →
                </a>
            `;

        }

    }


    // ======================================
    // ATENDIMENTO HÍBRIDO
    // ======================================

    else if (
        local.tipo === 'Atendimento híbrido' ||
        local.tipo === 'Atendimento hibrido'
    ) {

        botaoAcao = `
            <div class="botoes-popup">

                ${
                    local.site
                    ? `
                        <a
                            class="botao-rota"
                            href="${local.site}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Acessar site →
                        </a>
                    `
                    : ''
                }

                ${
                    local.latitude !== null &&
                    local.longitude !== null
                    ? `
                        <a
                            class="botao-rota"
                            href="https://www.google.com/maps/dir/?api=1&destination=${local.latitude},${local.longitude}"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Como chegar →
                        </a>
                    `
                    : ''
                }

            </div>
        `;

    }


    // ======================================
    // ATENDIMENTO PRESENCIAL
    // ======================================

    else {

        if (
            local.latitude !== null &&
            local.longitude !== null
        ) {

            botaoAcao = `
                <a
                    class="botao-rota"
                    href="https://www.google.com/maps/dir/?api=1&destination=${local.latitude},${local.longitude}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Como chegar →
                </a>
            `;

        }

    }


    // ======================================
    // BOTÃO DO MARCADOR
    // ======================================

    const elemento = document.createElement('button');

    elemento.className = 'marcador-mapa';

    elemento.type = 'button';

    elemento.innerHTML = `
        <span>
            ${icones[local.categoria] || "•"}
        </span>
    `;


    // ======================================
    // POPUP
    // ======================================

    const popup = new maplibregl.Popup({

        offset: 20,

        closeButton: true,

        closeOnClick: true,

        maxWidth: '320px'

    }).setHTML(`

        <div class="popup-apoio">

            <span class="popup-categoria">
                ${local.categoria || 'Apoio'}
            </span>


            <h3>
                ${local.nome || ''}
            </h3>


            ${
                local.tipo
                ? `
                    <p>
                        <strong>Tipo:</strong><br>
                        ${local.tipo}
                    </p>
                `
                : ''
            }


            ${
                local.endereco
                ? `
                    <p>
                        <strong>📍 Endereço</strong><br>
                        ${local.endereco}<br>
                        ${local.cidade || ''}
                    </p>
                `
                : ''
            }


            ${
                local.telefone
                ? `
                    <p>
                        <strong>📞 Telefone</strong><br>
                        ${local.telefone}
                    </p>
                `
                : ''
            }


            ${
                local.servicos
                ? `
                    <p>
                        <strong>♡ Serviços</strong><br>
                        ${local.servicos}
                    </p>
                `
                : ''
            }


            ${botaoAcao}

        </div>

    `);


    // ======================================
    // COLOCAR MARCADOR NO MAPA
    // ======================================

    const marcador = new maplibregl.Marker({

        element: elemento,

        anchor: 'bottom'

    })
        .setLngLat([
            Number(local.longitude),
            Number(local.latitude)
        ])

        .setPopup(popup)

        .addTo(mapa);


    return marcador;

}


// ==========================================
// MOSTRAR LOCAIS
// ==========================================

function mostrarLocais(categoria = "todos") {

    // Remove os marcadores antigos
    marcadores.forEach(marcador => {

        marcador.remove();

    });

    marcadores = [];


    // Percorre todos os locais
    locais.forEach(local => {

        // Verifica a categoria
        if (
            categoria === "todos" ||
            local.categoria === categoria
        ) {

            // Verifica se possui coordenadas
            if (
                local.latitude !== null &&
                local.longitude !== null &&
                local.latitude !== '' &&
                local.longitude !== ''
            ) {

                const marcador = criarMarcador(local);

                marcadores.push(marcador);

            }

        }

    });

}


// ==========================================
// MOSTRAR ATENDIMENTOS ONLINE
// ==========================================

function mostrarAtendimentosOnline() {

    const lista = document.getElementById('lista-online');

    // Se não existir a lista, não faz nada
    if (!lista) {

        console.log('Lista de atendimentos online não encontrada.');

        return;

    }


    lista.innerHTML = '';


    // Procura serviços online ou híbridos
    const online = locais.filter(local => {

        const tipo = (local.tipo || '')
            .trim()
            .toLowerCase();

        return (
            tipo.includes('online') ||
            tipo.includes('híbrido') ||
            tipo.includes('hibrido')
        );

    });


    console.log(
        'Atendimentos online/híbridos:',
        online
    );


    // Cria os cards
    online.forEach(local => {

        const card = document.createElement('article');

        card.className = 'card-online';


        card.innerHTML = `

            <span class="categoria-online">
                ${local.categoria || 'Apoio'}
            </span>


            <h4>
                ${local.nome || 'Serviço de apoio'}
            </h4>


            <p>
                ${
                    local.descricao ||
                    'Serviço de orientação, apoio ou capacitação disponível pela internet.'
                }
            </p>


            ${
                local.tipo
                ? `
                    <small>
                        ${local.tipo}
                    </small>
                `
                : ''
            }


            ${
                local.site
                ? `
                    <br><br>

                    <a
                        class="botao-online"
                        href="${local.site}"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Acessar site →
                    </a>
                `
                : ''
            }

        `;


        lista.appendChild(card);

    });

}


// ==========================================
// FILTROS DO MAPA
// ==========================================

const botoes = document.querySelectorAll('.filtro');


botoes.forEach(botao => {

    botao.addEventListener('click', () => {

        // Remove o ativo de todos
        botoes.forEach(outro => {

            outro.classList.remove('ativo');

        });


        // Ativa o botão clicado
        botao.classList.add('ativo');


        // Pega a categoria
        const categoria = botao.dataset.categoria;


        // Mostra os locais
        mostrarLocais(categoria);

    });

});


// ==========================================
// MAPA CARREGADO
// ==========================================

mapa.on('load', async () => {

    console.log('Mapa carregado!');


    await carregarLocais();


    // Mostra os marcadores
    mostrarLocais();


    // Mostra os atendimentos online
    mostrarAtendimentosOnline();

});


// ==========================================
// MODAIS DOS AUXÍLIOS
// ==========================================

const botoesModal = document.querySelectorAll('.botao-modal');

const modais = document.querySelectorAll('.modal-apoio');


// ==========================================
// ABRIR MODAL
// ==========================================

botoesModal.forEach(botao => {

    botao.addEventListener('click', () => {

        const idModal = botao.dataset.modal;

        const modal = document.getElementById(idModal);


        if (!modal) {

            console.error(
                'Modal não encontrado:',
                idModal
            );

            return;

        }


        modal.classList.add('aberta');

        document.body.style.overflow = 'hidden';

    });

});


// ==========================================
// FECHAR NO X
// ==========================================

const botoesFechar = document.querySelectorAll('.fechar-modal');


botoesFechar.forEach(botao => {

    botao.addEventListener('click', () => {

        const modal = botao.closest('.modal-apoio');


        if (modal) {

            modal.classList.remove('aberta');

        }


        document.body.style.overflow = '';

    });

});


// ==========================================
// FECHAR CLICANDO FORA
// ==========================================

modais.forEach(modal => {

    modal.addEventListener('click', evento => {

        if (evento.target === modal) {

            modal.classList.remove('aberta');

            document.body.style.overflow = '';

        }

    });

});


// ==========================================
// FECHAR COM ESC
// ==========================================

document.addEventListener('keydown', evento => {

    if (evento.key === 'Escape') {

        modais.forEach(modal => {

            modal.classList.remove('aberta');

        });


        document.body.style.overflow = '';

    }

});