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


// ==========================================
// CONTROLES DO MAPA
// ==========================================

mapa.addControl(
    new maplibregl.NavigationControl(),
    'top-right'
);


// ==========================================
// LOCAIS
// ==========================================

const locais = [

    {
        nome: "ONG Exemplo",
        categoria: "ONG",
        endereco: "Rua Exemplo, 100",
        cidade: "São Paulo - SP",
        telefone: "(11) 00000-0000",
        servicos: "Apoio social, orientação e acolhimento.",
        latitude: -23.5505,
        longitude: -46.6333
    },

    {
        nome: "Centro de Assistência Exemplo",
        categoria: "Assistência Social",
        endereco: "Rua Exemplo, 200",
        cidade: "São Paulo - SP",
        telefone: "(11) 00000-0000",
        servicos: "Atendimento e orientação social.",
        latitude: -23.5605,
        longitude: -46.6433
    },

    {
        nome: "Serviço de Saúde Exemplo",
        categoria: "Saúde",
        endereco: "Rua Exemplo, 300",
        cidade: "São Paulo - SP",
        telefone: "(11) 00000-0000",
        servicos: "Atendimento e encaminhamento de saúde.",
        latitude: -23.5705,
        longitude: -46.6533
    },

    {
        nome: "Atendimento Jurídico Exemplo",
        categoria: "Jurídico",
        endereco: "Rua Exemplo, 400",
        cidade: "São Paulo - SP",
        telefone: "(11) 00000-0000",
        servicos: "Orientação e assistência jurídica.",
        latitude: -23.5805,
        longitude: -46.6633
    },

    {
        nome: "Projeto de Capacitação Exemplo",
        categoria: "Emprego",
        endereco: "Rua Exemplo, 500",
        cidade: "São Paulo - SP",
        telefone: "(11) 00000-0000",
        servicos: "Cursos e orientação profissional.",
        latitude: -23.5905,
        longitude: -46.6733
    }

];


// ==========================================
// MARCADORES
// ==========================================

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

            const marcador = criarMarcador(local);

            marcadores.push(marcador);

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

mapa.on('load', () => {

    mostrarLocais();

});