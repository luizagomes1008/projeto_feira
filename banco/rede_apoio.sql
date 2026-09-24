-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/09/2026 às 15:59
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `rede_apoio`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `apoios`
--

CREATE TABLE `apoios` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `categoria` varchar(100) NOT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `servicos` text DEFAULT NULL,
  `publico` text DEFAULT NULL,
  `horario` varchar(200) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `telefone` varchar(50) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `longitude` decimal(10,7) DEFAULT NULL,
  `site` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `apoios`
--

INSERT INTO `apoios` (`id`, `nome`, `categoria`, `tipo`, `descricao`, `servicos`, `publico`, `horario`, `endereco`, `cidade`, `telefone`, `latitude`, `longitude`, `site`) VALUES
(1, 'Caminho da Capacitação - Fundo Social de Ribeirão Pires', 'Emprego', 'Capacitação', 'Cursos gratuitos de capacitação profissional.', 'Assistente de Cabeleireiro, Manicure e Design de Sobrancelha. 60 vagas.', 'Pessoas interessadas em capacitação profissional', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, 'http://caminhodacapacitacao.sp.gov.br'),
(2, 'Programa Senac de Gratuidade (PSG)', 'Emprego', 'Capacitação', 'Programa de cursos gratuitos do Senac.', 'Cursos gratuitos para pessoas com renda de até 2 salários mínimos.', 'Pessoas com renda de até 2 salários mínimos', NULL, NULL, NULL, NULL, NULL, NULL, 'http://ead.senac.br/gratuito'),
(3, 'Sebrae Delas - Elas Acontecem', 'Emprego', 'Capacitação', 'Programa voltado ao empreendedorismo feminino.', 'Mulheres interessadas em empreendedorismo', 'Cursos e mentoria', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'Qualifica SP / SP Por Todas', 'Emprego', 'Capacitação', 'Programas de qualificação profissional.', 'Mulheres interessadas em qualificação e empreendedorismo', 'Assistente Administrativo, Excel, Marketing Digital e Carreta do Empreendedorismo', NULL, NULL, NULL, NULL, NULL, NULL, 'http://qualificasp.sp.gov.br'),
(5, 'CRAS e CREAS de Ribeirão Pires', 'Assistência Social', 'Órgão Público', 'Serviços de assistência social e encaminhamento.', 'Cadastro Único, benefícios e encaminhamento para cursos.', 'Pessoas em situação de vulnerabilidade', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(6, 'PAT - Posto de Atendimento ao Trabalhador de Ribeirão Pires', 'Emprego', 'Órgão Público', 'Serviço público voltado ao atendimento de trabalhadores.', 'Vagas de emprego formal.', 'Pessoas em busca de emprego', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(7, 'Casa da Mulher Paulista / Centro de Referência da Mulher do ABC', 'Assistência Social', 'Órgão Público', 'Serviço de apoio e atendimento às mulheres.', 'Atendimento e orientação para mulheres.', 'Mulheres', NULL, NULL, 'ABC Paulista', NULL, NULL, NULL, NULL),
(8, 'DDM - Delegacia da Mulher', 'Jurídico', 'Órgão Público', 'Delegacia especializada no atendimento de mulheres.', 'Atendimento policial especializado.', 'Mulheres', '24 horas', NULL, 'Estado de São Paulo', NULL, NULL, NULL, NULL),
(9, 'Rede Mulher Empreendedora', 'Emprego', 'ONG', 'Rede de apoio ao empreendedorismo feminino.', 'Apoio para mulheres que querem começar um negócio.', 'Mulheres empreendedoras', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 'Associação Fala Mulher', 'Assistência Social', 'ONG', 'Organização de acolhimento para mulheres em situação de vulnerabilidade.', 'Acolhimento e apoio.', 'Mulheres em situação de vulnerabilidade', NULL, NULL, 'Diadema / ABC', NULL, NULL, NULL, NULL),
(11, 'TransEmpregos', 'Emprego', 'ONG', 'Iniciativa voltada à empregabilidade de pessoas trans.', 'Vagas e apoio para empregabilidade.', 'Pessoas trans', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, 'ANTRA', 'Emprego', 'ONG', 'Organização voltada à população trans.', 'Apoio relacionado à empregabilidade de pessoas trans.', 'Pessoas trans', NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, 'Fundo Social de Solidariedade de Ribeirão Pires', 'Assistência Social', 'Órgão Público', 'Serviço relacionado à assistência social do município.', 'Apoio e iniciativas de assistência social.', 'Pessoas em situação de vulnerabilidade', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(14, 'Defensoria Pública do Estado de SP - Núcleo da Mulher', 'Jurídico', 'Órgão Público', 'Serviço de assistência jurídica gratuita.', 'Atendimento jurídico gratuito.', 'Mulheres', NULL, NULL, 'São Paulo - SP', NULL, NULL, NULL, NULL),
(15, 'Ministério Público de SP - Promotoria da Mulher', 'Jurídico', 'Órgão Público', 'Serviço relacionado à proteção de direitos das mulheres.', 'Atendimento e orientação.', 'Mulheres', NULL, NULL, 'São Paulo - SP', NULL, NULL, NULL, NULL),
(16, 'OAB por Elas', 'Jurídico', 'Serviço Jurídico', 'Iniciativa de apoio jurídico às mulheres.', 'Atendimento jurídico gratuito.', 'Mulheres', NULL, NULL, 'ABC Paulista', NULL, NULL, NULL, NULL),
(17, 'UBS do município', 'Saúde', 'Saúde Pública', 'Unidades Básicas de Saúde.', 'Atendimento básico de saúde.', 'População em geral', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(18, 'CAPS Ribeirão Pires', 'Saúde', 'Saúde Pública', 'Serviço de atenção à saúde mental.', 'Atendimento em saúde mental.', 'População em geral', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(19, 'Hospital e Maternidade São Lucas / Mário Covas', 'Saúde', 'Saúde Pública', 'Serviços hospitalares e de maternidade.', 'Atendimento hospitalar e maternidade.', 'População em geral', NULL, NULL, 'ABC Paulista', NULL, NULL, NULL, NULL),
(20, 'CTA - Centro de Testagem e Aconselhamento', 'Saúde', 'Saúde Pública', 'Serviço de testagem e aconselhamento.', 'Testagem e aconselhamento.', 'População em geral', NULL, NULL, 'Ribeirão Pires', NULL, NULL, NULL, NULL),
(21, 'SP Mulher Segura', 'Saúde', 'Serviço Público', 'Aplicativo voltado à proteção e segurança das mulheres.', 'Botão de pânico e ligação direta para a polícia.', 'Mulheres', NULL, NULL, 'Estado de São Paulo', NULL, NULL, NULL, NULL),
(22, 'CRAS Parque das Américas', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Estados Unidos, 84 - Parque das Américas', 'Mauá - SP', '(11) 4541-1484', -23.6892000, -46.4426000, NULL),
(23, 'Casa do Trabalhador SINE Mauá', 'Emprego', 'Órgão Público', 'Serviço público voltado ao atendimento de trabalhadores e empregadores.', 'Vagas de emprego, intermediação de mão de obra, orientação profissional, Carteira de Trabalho e Seguro-Desemprego.', 'Pessoas em busca de emprego e trabalhadores.', 'Segunda a sexta, das 8h às 17h', 'Rua Jundiaí, 63 - Matriz', 'Mauá - SP', '(11) 4514-6141 / 4512-7779', NULL, NULL, NULL),
(24, 'Centro de Referência em Saúde da Mulher, Criança e Adolescente', 'Saúde', 'Saúde Pública', 'Centro de referência voltado ao atendimento especializado de mulheres, crianças e adolescentes.', 'Atendimento e acompanhamento em saúde da mulher, criança e adolescente.', 'Mulheres, crianças e adolescentes.', 'Segunda a sexta, das 7h às 17h', 'Rua Luís Lacava, 229 - Vila Bocaina', 'Mauá - SP', '(11) 4519-5000', -23.6686648, -46.4579699, NULL),
(25, 'CRAS Falchi', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Friedrich Gunter Meinen, 71 - Vila Falchi', 'Mauá - SP', '(11) 4512-7582', -23.6858000, -46.4710000, NULL),
(26, 'CRAS Feital', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Avenida Benedita Franco da Veiga, 1083 - Jardim Feital', 'Mauá - SP', '(11) 4512-7726 / 4555-2558', -23.6755000, -46.4245000, NULL),
(27, 'CRAS Macuco', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Remo Luiz Corradini, 115 - Jardim Zaira/Macuco', 'Mauá - SP', '(11) 4518-2666 / 4512-7727', -23.6486450, -46.4446640, NULL),
(28, 'CRAS Oratório', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Salvador, 266 - Jardim Oratório', 'Mauá - SP', '(11) 4514-5411 / 4512-7721', -23.6740000, -46.4205000, NULL),
(29, 'CRAS Parque das Américas', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Estados Unidos, 84 - Parque das Américas', 'Mauá - SP', '(11) 4541-1484 / 4512-7729', -23.6892000, -46.4426000, NULL),
(30, 'CRAS São João', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Avenida Barão de Mauá, 4050 - Vila São João', 'Mauá - SP', '(11) 4518-4535 / 4512-7730', -23.6748000, -46.4315000, NULL),
(31, 'CRAS Vila Mercedes', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Rua Cícero Rodrigues da Silva, 355 - Vila Mercedes', 'Mauá - SP', '(11) 4513-6465 / 4512-7722', -23.6785000, -46.4515000, NULL),
(32, 'CRAS Zaíra', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social de Mauá.', 'Acolhimento, orientação, encaminhamento para serviços e atendimento socioassistencial.', 'Famílias e pessoas que necessitam de assistência social.', 'Segunda a sexta, das 8h às 17h', 'Avenida Presidente Castelo Branco, 2982 - Jardim Zaíra', 'Mauá - SP', '(11) 4514-4265 / 4512-7723', -23.6500000, -46.4360000, NULL),
(33, 'CREAS Vila Bocaina', 'Assistência Social', 'Órgão Público', 'Centro de Referência Especializado de Assistência Social.', 'Atendimento especializado e encaminhamento para a rede de proteção social.', 'Pessoas e famílias em situação de vulnerabilidade ou violação de direitos.', 'Segunda a sexta, das 8h às 17h', 'Rua Álvares Machado, 18A - Vila Bocaina', 'Mauá - SP', '(11) 4513-6417', -23.6680000, -46.4620000, NULL),
(34, 'CREAS Matriz', 'Assistência Social', 'Órgão Público', 'Centro de Referência Especializado de Assistência Social.', 'Atendimento especializado, orientação e encaminhamento para serviços da rede de proteção.', 'Pessoas e famílias em situação de vulnerabilidade ou violação de direitos.', 'Segunda a sexta, das 8h às 17h', 'Rua Avaré, 62 - Matriz', 'Mauá - SP', '(11) 4512-7731 / 4512-9142', -23.6675000, -46.4595000, NULL),
(35, 'Casa do Trabalhador SINE Mauá', 'Emprego', 'Órgão Público', 'Serviço público de atendimento a trabalhadores e empregadores.', 'Vagas de emprego, intermediação de mão de obra, orientação profissional, Seguro-Desemprego e cursos profissionalizantes.', 'Pessoas em busca de emprego e trabalhadores.', 'Segunda a sexta, das 8h às 17h', 'Rua Jundiaí, 63 - Matriz', 'Mauá - SP', '(11) 4514-6141 / 4512-7779', -23.6680000, -46.4605000, NULL),
(36, 'CRSMCA - Centro de Referência em Saúde da Mulher, Criança e Adolescente', 'Saúde', 'Saúde Pública', 'Centro de referência em saúde da mulher, criança e adolescente.', 'Atendimento e acompanhamento especializado em saúde.', 'Mulheres, crianças e adolescentes.', 'Segunda a sexta, das 7h às 17h', 'Rua Luís Lacava, 229 - Vila Bocaina', 'Mauá - SP', '(11) 4519-5000', -23.6686648, -46.4579699, NULL),
(37, 'CEREST - Centro de Referência em Saúde do Trabalhador', 'Saúde', 'Saúde Pública', 'Centro de Referência especializado em saúde do trabalhador.', 'Orientação e atendimento relacionado à saúde e às condições de trabalho.', 'Trabalhadores.', 'Segunda a sexta, das 8h às 17h', 'Avenida Capitão João, 2301 - Vila Vitória', 'Mauá - SP', '(11) 4512-7784', -23.6800000, -46.4650000, NULL);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `apoios`
--
ALTER TABLE `apoios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `apoios`
--
ALTER TABLE `apoios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
