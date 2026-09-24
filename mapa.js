// ==========================================
// MAPA DE REDE DE APOIO
// ==========================================

// Criando o mapa
const mapa = new maplibregl.Map({
    container: 'mapa',

    // Estilo do mapa
    style: 'https://tiles.openfreemap.org/styles/liberty',

    // Centro inicial
    center: [-46.4133, -23.7104],

    // Zoom inicial
    zoom: 11
});


let locais = [];

// ==========================================
// CONTROLES DO MAPA
// ==========================================

mapa.addControl(
    new maplibregl.NavigationControl(),
    'top-right'
);

// ==========================================
// MARCADORES
// ==========================================

let marcadores = [];

async function carregarLocais() {

    try {

        const resposta = await fetch('buscar_apoios.php');

        if (!resposta.ok) {
            throw new Error('Erro ao buscar os apoios.');
        }

        locais = await resposta.json();

        console.log('Locais carregados:', locais);

    } catch (erro) {

        console.error('Erro:', erro);

    }

}

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
// CRIAR MARCADOR
// ==========================================

function criarMarcador(local) {

    // Criando o botão do marcador
    const elemento = document.createElement('button');

    elemento.className = 'marcador-mapa';

    elemento.type = 'button';

    elemento.innerHTML = `
        <span>${icones[local.categoria] || "•"}</span>
    `;


    // ==========================================
    // POPUP
    // ==========================================

    const popup = new maplibregl.Popup({
        offset: 20,
        closeButton: true,
        closeOnClick: true,
        maxWidth: '320px'
    })
        .setHTML(`

        <div class="popup-apoio">

            <span class="popup-categoria">
                ${local.categoria}
            </span>

            <h3>
                ${local.nome}
            </h3>

            <p>
                <strong>📍 Endereço</strong><br>
                ${local.endereco}<br>
                ${local.cidade}
            </p>

            <p>
                <strong>📞 Telefone</strong><br>
                ${local.telefone}
            </p>

            <p>
                <strong>♡ Serviços</strong><br>
                ${local.servicos}
            </p>

            <a
                class="botao-rota"
                href="https://www.google.com/maps/dir/?api=1&destination=${local.latitude},${local.longitude}"
                target="_blank"
                rel="noopener noreferrer"
            >
                Como chegar →
            </a>

        </div>

    `);


    // ==========================================
    // CRIANDO O MARCADOR
    // ==========================================

    const marcador = new maplibregl.Marker({
        element: elemento,
        anchor: 'bottom'
    })
        .setLngLat([
            local.longitude,
            local.latitude
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


    // Adiciona os locais
    locais.forEach(local => {

        if (
            categoria === "todos" ||
            local.categoria === categoria
        ) {

            // Só cria marcador se tiver coordenadas
            if (
                local.latitude !== null &&
                local.longitude !== null
            ) {

                const marcador = criarMarcador(local);

                marcadores.push(marcador);

            }

        }

    });

}


// ==========================================
// FILTROS
// ==========================================

const botoes = document.querySelectorAll('.filtro');


botoes.forEach(botao => {

    botao.addEventListener('click', () => {

        // Remove o ativo dos outros
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

    await carregarLocais();

    mostrarLocais();

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

        modal.classList.remove('aberta');

        document.body.style.overflow = '';

    });

});


// ==========================================
// FECHAR CLICANDO FORA
// ==========================================

modais.forEach(modal => {

    modal.addEventListener('click', (evento) => {

        if (evento.target === modal) {

            modal.classList.remove('aberta');

            document.body.style.overflow = '';

        }

    });

});


// ==========================================
// FECHAR COM ESC
// ==========================================

document.addEventListener('keydown', (evento) => {

    if (evento.key === 'Escape') {

        modais.forEach(modal => {
            modal.classList.remove('aberta');
        });

        document.body.style.overflow = '';
    }

});