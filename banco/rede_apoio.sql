-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24/09/2026 às 17:25
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
(23, 'Casa do Trabalhador SINE Mauá', 'Emprego', 'Órgão Público', 'Serviço público voltado ao atendimento de trabalhadores e empregadores.', 'Vagas de emprego, intermediação de mão de obra, orientação profissional, Carteira de Trabalho e Seguro-Desemprego.', 'Pessoas em busca de emprego e trabalhadores.', 'Segunda a sexta, das 8h às 17h', 'Rua Jundiaí, 63 - Matriz', 'Mauá - SP', '(11) 4514-6141 / 4512-7779', -23.6680000, -46.4605000, NULL),
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
(37, 'CEREST - Centro de Referência em Saúde do Trabalhador', 'Saúde', 'Saúde Pública', 'Centro de Referência especializado em saúde do trabalhador.', 'Orientação e atendimento relacionado à saúde e às condições de trabalho.', 'Trabalhadores.', 'Segunda a sexta, das 8h às 17h', 'Avenida Capitão João, 2301 - Vila Vitória', 'Mauá - SP', '(11) 4512-7784', -23.6800000, -46.4650000, NULL),
(38, 'CRAM Zaíra', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento de mulheres em situação de violência.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Avenida Presidente Castelo Branco, 2982 - Jardim Zaíra', 'Mauá - SP', '4514-4265', -23.6500000, -46.4360000, NULL),
(39, 'CRAM Macuco', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Rua Remo Luiz Corradini, 115 - Macuco', 'Mauá - SP', '4518-2666', -23.6486450, -46.4446640, NULL),
(40, 'CRAM Oratório', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Rua Salvador, 266 - Jardim Oratório', 'Mauá - SP', '4514-5411', -23.6740000, -46.4205000, NULL),
(41, 'CRAM Parque das Américas', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Rua Estados Unidos, 84 - Parque das Américas', 'Mauá - SP', '4541-1484', -23.6892000, -46.4426000, NULL),
(42, 'CRAM São João', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Avenida Barão de Mauá, 4050 - Vila São João', 'Mauá - SP', '4518-4535', -23.6748000, -46.4315000, NULL),
(43, 'CRAM Feital', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Avenida Benedita Franco da Veiga, 1085 - Jardim Feital', 'Mauá - SP', '4512-7726', -23.6755000, -46.4245000, NULL),
(44, 'CRAM Vila Mercedes', 'Assistência Social', 'Serviço Público', 'Centro de Referência de Atendimento à Mulher.', 'Acolhimento, orientação e encaminhamento para a rede de proteção.', 'Mulheres em situação de violência.', 'Segunda a sexta, das 8h às 17h', 'Rua Cícero Rodrigues da Silva, 443 - Vila Mercedes', 'Mauá - SP', '4513-6465', -23.6785000, -46.4515000, NULL),
(45, 'Central de Cadastro Único de Mauá', 'Assistência Social', 'Órgão Público', 'Unidade responsável pelo atendimento relacionado ao Cadastro Único.', 'Cadastro Único e orientações sobre benefícios e programas sociais.', 'Famílias e pessoas que podem participar de programas e benefícios sociais.', 'Segunda a sexta, das 8h às 17h', 'Rua Almirante Tamandaré, 589 - Vila Bocaina', 'Mauá - SP', '4545-3269 / 4512-7717', -23.6685000, -46.4585000, NULL),
(46, 'Centro POP Mauá', 'Assistência Social', 'Órgão Público', 'Centro de Referência Especializado para População em Situação de Rua.', 'Atendimento social, orientação e fortalecimento de vínculos.', 'Pessoas em situação de rua.', 'Segunda a sexta, das 8h às 17h', 'Avenida Washington Luiz, 625 - Jardim Cerqueira Leite', 'Mauá - SP', '4547-1061', -23.6765000, -46.4495000, NULL),
(47, 'Centro de Convivência Bombeiro Mirim', 'Assistência Social', 'Serviço Público', 'Serviço socioeducativo voltado a crianças e adolescentes.', 'Atividades socioeducativas, cidadania e fortalecimento de vínculos.', 'Crianças e adolescentes de 9 a 14 anos.', 'Segunda a quinta-feira, no contraturno escolar', 'Avenida Papa João XXIII, 255 - Vila Noemia', 'Mauá - SP', '4546-3418 / 93725-5877', -23.6775000, -46.4615000, NULL),
(48, 'CRAS Centro Alto - Ribeirão Pires', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social.', 'Acolhimento, orientação, Cadastro Único e encaminhamento para benefícios e serviços sociais.', 'Famílias e pessoas em situação de vulnerabilidade social.', 'Segunda a sexta, das 8h às 17h', 'Rua Jorge Tibiriçá, 140 - Centro Alto', 'Ribeirão Pires - SP', NULL, -23.7327000, -46.3721000, NULL),
(49, 'SAPIS / CREAS Ribeirão Pires', 'Assistência Social', 'Órgão Público', 'Serviço especializado de assistência social.', 'Atendimento especializado, orientação e encaminhamento em situações de violação de direitos.', 'Pessoas e famílias em situação de vulnerabilidade ou violação de direitos.', 'Segunda a sexta, das 8h às 17h', 'Rua Conde de Sarzedas, 333 - Pastoril', 'Ribeirão Pires - SP', NULL, -23.7185000, -46.4115000, NULL),
(50, 'OAB Ribeirão Pires - Assistência Judiciária', 'Jurídico', 'Serviço Jurídico', 'Atendimento jurídico e assistência judiciária para pessoas que não podem pagar advogado.', 'Orientação jurídica e encaminhamento para assistência judiciária.', 'Pessoas sem condições financeiras para contratar advogado.', 'Segunda a sexta, das 9h às 18h', 'Rua Presidente Kennedy, 133 - Vila Ugliengo', 'Ribeirão Pires - SP', '(11) 4824-4336 / 4823-7466', -23.7105000, -46.4135000, NULL),
(51, 'Delegacia de Polícia de Ribeirão Pires', 'Jurídico', 'Órgão Público', 'Unidade policial para registro de ocorrências e encaminhamentos.', 'Registro de ocorrências e encaminhamento de medidas protetivas.', 'Pessoas que necessitam de atendimento policial.', '24 horas', 'Avenida Prefeito Valdírio Prisco, 245 - Centro', 'Ribeirão Pires - SP', '(11) 4828-1166', -23.7100000, -46.4130000, NULL),
(52, 'Atende Fácil / PAT Ribeirão Pires', 'Emprego', 'Órgão Público', 'Central de atendimento aos trabalhadores e serviços de emprego.', 'Intermediação de mão de obra, vagas de emprego e Seguro-Desemprego.', 'Pessoas em busca de emprego e trabalhadores.', 'Segunda a sexta, das 8h às 16h30', 'Rua Capitão José Galo, 55 - Centro', 'Ribeirão Pires - SP', '(11) 4824-4282', -23.7105000, -46.4135000, NULL),
(53, 'Central de Cadastro Único de Ribeirão Pires', 'Assistência Social', 'Órgão Público', 'Unidade responsável pelo atendimento do Cadastro Único.', 'Cadastro Único e orientações sobre programas e benefícios sociais.', 'Famílias e pessoas que podem ter direito a programas sociais.', 'Segunda a sexta, das 8h às 17h', 'Rua Capitão José Gallo, s/n - Centro', 'Ribeirão Pires - SP', '(11) 4825-6465 / 4824-4282', -23.7105000, -46.4135000, NULL),
(54, 'Defensoria Pública de Santo André', 'Jurídico', 'Órgão Público', 'Unidade da Defensoria Pública do Estado de São Paulo.', 'Orientação e assistência jurídica gratuita.', 'Pessoas que necessitam de assistência jurídica e não possuem condições de contratar advogado.', 'Segunda a sexta, das 8h às 17h', 'Rua Primeiro de Maio, 178 - Centro', 'Santo André - SP', NULL, -23.6565000, -46.5315000, NULL),
(55, 'Vara da Violência Doméstica e Familiar contra a Mulher de Santo André', 'Jurídico', 'Órgão Público', 'Vara especializada em processos relacionados à violência doméstica e familiar contra a mulher.', 'Processos judiciais e medidas protetivas.', 'Mulheres envolvidas em situações de violência doméstica e familiar.', 'Horário do Fórum', 'Praça IV Centenário, 03 - Centro', 'Santo André - SP', NULL, -23.6580000, -46.5320000, NULL),
(56, 'Delegacia de Defesa da Mulher - DDM Santo André', 'Jurídico', 'Órgão Público', 'Delegacia especializada no atendimento de mulheres.', 'Registro de ocorrências e atendimento especializado.', 'Mulheres vítimas de violência.', 'Consultar unidade', 'Rua Laura, 452 - Centro', 'Santo André - SP', NULL, -23.6575000, -46.5295000, NULL),
(57, 'CPETR / Poupatempo Santo André', 'Emprego', 'Órgão Público', 'Centro Público de Emprego, Trabalho e Renda.', 'Vagas de emprego, Seguro-Desemprego e serviços relacionados ao trabalho.', 'Pessoas em busca de emprego e trabalhadores.', 'Segunda a sexta, das 9h às 17h; sábado, das 9h às 13h', 'Rua Giovanni Battista Pirelli, 155 - Vila Homero Thon', 'Santo André - SP', NULL, -23.6638450, -46.5070570, NULL),
(58, 'CRAS Centro de Santo André', 'Assistência Social', 'Órgão Público', 'Centro de Referência de Assistência Social.', 'Cadastro Único, orientação e encaminhamento para benefícios e serviços sociais.', 'Famílias e pessoas em situação de vulnerabilidade social.', 'Segunda a sexta, das 8h às 17h', 'Rua Xavier de Toledo, 350 - Centro', 'Santo André - SP', '(11) 4433-4550', -23.6606000, -46.5244000, NULL),
(59, 'ONG Viva Melhor', 'ONG', 'ONG', 'Organização voltada ao acolhimento e apoio de mulheres que enfrentam o câncer de mama, incluindo mulheres mastectomizadas.', 'Acolhimento; apoio emocional; grupos de autoajuda', 'Mulheres que enfrentam ou enfrentaram o câncer de mama', 'Consultar diretamente a organização', 'Rua Antônio Cardoso Franco, 167 - Casa Branca', 'Santo André - SP', '', -23.6635000, -46.5305000, 'https://www.instagram.com/ongvivamelhor/'),
(60, 'Casa da Mulher Paulista - Ficar de Bem', 'ONG', 'ONG', 'Serviço voltado ao atendimento de mulheres em situação de violência e vulnerabilidade social.', 'Atendimento psicossocial; atividades de empoderamento; orientação sobre direitos; acompanhamento especializado', 'Mulheres cis e trans em situação de violência doméstica e familiar', 'Segunda a sexta, das 8h às 17h', 'Rua Senador Ricardo Batista, 300 - Bairro Assunção', 'São Bernardo do Campo - SP', '(11) 99324-1685', -23.6945000, -46.5575000, 'https://ficardebem.org.br/centro-de-referencia-e-apoio-a-mulher/'),
(61, 'Mapa do Acolhimento', 'ONG', 'Atendimento online', 'Rede nacional que conecta mulheres em situação de violência a profissionais voluntárias.', 'Apoio psicológico; orientação jurídica; informações sobre serviços públicos e rede de proteção', 'Mulheres em situação de violência e vulnerabilidade', 'Atendimento e cadastro pela plataforma online', 'Atendimento online - sede no Rio de Janeiro', 'Rio de Janeiro - RJ', '(21) 7201-8787', -22.9645000, -43.2245000, 'https://www.mapadoacolhimento.org/'),
(62, 'Instituto Rede Mulher Empreendedora - IRME', 'ONG', 'Atendimento online', 'Instituição voltada à inclusão econômica de mulheres em situação de vulnerabilidade e ao fortalecimento da autonomia financeira.', 'Capacitação; empreendedorismo; geração de renda; mentoria', 'Mulheres em situação de vulnerabilidade e empreendedoras', 'Consultar programas disponíveis no site', 'Av. Jabaquara, 1909 - Mirandópolis', 'São Paulo - SP', '(11) 2619-9190', -23.6165000, -46.6415000, 'https://rme.net.br/'),
(63, 'Cruzando Histórias', 'ONG', 'Atendimento online', 'Organização sem fins lucrativos que promove acolhimento, valorização profissional e empregabilidade entre mulheres.', 'Orientação de carreira; empregabilidade; geração de renda; acolhimento; saúde emocional', 'Mulheres em situação de vulnerabilidade social e desemprego', 'Atendimento presencial e programação online - consultar site', 'Rua Barão de Itapetininga, 255, conjunto 209 - República', 'São Paulo - SP', '', -23.5465000, -46.6435000, 'https://www.cruzandohistorias.org/'),
(64, 'Vem Maria - Santo André', 'Assistência Social', 'Serviço público especializado', 'Serviço de atendimento e acompanhamento de mulheres em situação de violência de gênero.', 'Acolhimento; acompanhamento psicossocial; orientação; encaminhamento para a rede de proteção', 'Mulheres cis e trans em situação de violência', 'Segunda a sexta, das 8h às 20h', 'Alameda Gaspar Nogueira, 31 - Jardim', 'Santo André - SP', '4992-2936', -23.6555000, -46.5350000, ''),
(65, 'ONG Mulheres em Ação de Mauá', 'ONG', 'ONG', 'Organização que atua no enfrentamento da violência contra a mulher, acolhimento e garantia de direitos.', 'Apoio jurídico; apoio psicológico; assistência social; orientação e encaminhamento', 'Mulheres em situação de violência e vulnerabilidade', 'Consultar diretamente a organização', 'Rua Guatemala, 273 - Parque das Américas', 'Mauá - SP', '(11) 95054-9291', -23.6892000, -46.4426000, ''),
(66, 'Viva Maria - Centro de Referência no Atendimento à Mulher', 'Assistência Social', 'Serviço público especializado', 'Centro público especializado no atendimento e acompanhamento de mulheres em situação de violência.', 'Acolhimento; apoio psicológico; assistência social; orientação jurídica; acompanhamento e encaminhamento', 'Mulheres em situação de violência', 'Segunda a sexta, das 8h às 17h', 'Rua Santa Cecília, 489 - Matriz', 'Mauá - SP', '(11) 4512-7615', -23.6680000, -46.4595000, ''),
(67, 'Movimento Mãe Onça', 'ONG', 'ONG', 'Organização voltada ao acolhimento de mães atípicas, mulheres e famílias em situação de vulnerabilidade social.', 'Acolhimento; apoio emocional; orientação; atividades de inclusão; autocuidado; apoio a mães atípicas', 'Mães atípicas, mulheres e famílias em situação de vulnerabilidade', 'Consultar diretamente a organização', 'Avenida Ernesto Menato, 7 - Centro Alto', 'Ribeirão Pires - SP', '', -23.7320000, -46.3720000, ''),
(68, 'Projeto Resgatando Vidas', 'ONG', 'ONG', 'Organização social voltada à promoção da dignidade humana e apoio a pessoas e famílias em situação de vulnerabilidade socioeconômica.', 'Distribuição de alimentos; ações de cidadania; bazar beneficente; apoio social', 'Mulheres, famílias e pessoas em situação de vulnerabilidade socioeconômica', 'Consultar diretamente a organização', 'Rua Capitão José Gallo, 348 - Centro', 'Ribeirão Pires - SP', '', -23.7105000, -46.4135000, '');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
