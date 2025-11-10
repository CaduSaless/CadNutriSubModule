-- Tabela: Pessoa
-- Armazena informações pessoais básicas
CREATE TABLE IF NOT EXISTS Pessoa (
    id_Pessoa SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    raca TEXT NOT NULL,
    sexo TEXT NOT NULL,
    escolaridade TEXT NOT NULL,
    email TEXT NOT NULL,
    data_nascimento DATE NOT NULL
);

-- Tabela: Etnia
-- Armazena diferentes etnias
CREATE TABLE IF NOT EXISTS Etnia (
    id_Etnia SERIAL PRIMARY KEY,
    nome_Etnia TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL
);

-- Tabela: Etnia_Pessoa
-- Tabela de relacionamento N:M (muitos para muitos) entre Pessoa e Etnia
-- Nota: O esquema original do SQLite tinha uma PK e FK em id_Pessoa e uma FK em id_Etnia com UNIQUE.
-- Para refletir uma relação N:M mais flexível, usarei uma chave composta (id_Pessoa, id_Etnia).
CREATE TABLE IF NOT EXISTS Etnia_Pessoa (
    id_Pessoa INTEGER NOT NULL REFERENCES Pessoa (id_Pessoa) ON DELETE CASCADE ON UPDATE CASCADE,
    id_Etnia INTEGER NOT NULL REFERENCES Etnia (id_Etnia) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (id_Pessoa, id_Etnia)
);

-- Tabela: Consumo
-- Armazena dados de consumo alimentar
CREATE TABLE IF NOT EXISTS Consumo (
    id_Pessoa INTEGER PRIMARY KEY REFERENCES Pessoa (id_Pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION,
    come_Com_TV BOOLEAN NOT NULL,
    quais_Refeicoes TEXT NOT NULL,
    feijao BOOLEAN NOT NULL,
    frutas BOOLEAN NOT NULL,
    verduras_Legumes BOOLEAN NOT NULL,
    embutidos BOOLEAN NOT NULL,
    bebidas_Acocadas BOOLEAN NOT NULL,
    insdustrializados_Salgados BOOLEAN NOT NULL,
    industrializados_Doces BOOLEAN NOT NULL,
    data_Resposta TEXT NOT NULL
);

-- Tabela: Medidas_Antropomorficas
-- Armazena medidas físicas
CREATE TABLE IF NOT EXISTS Medidas_Antropomorficas (
    id_Medidas SERIAL PRIMARY KEY,
    id_Pessoa INTEGER NOT NULL REFERENCES Pessoa (id_Pessoa) ON DELETE CASCADE ON UPDATE CASCADE,
    peso_kg NUMERIC (5) NOT NULL,
    altura_cm INTEGER (4) NOT NULL,
    tipo_Cabelo TEXT NOT NULL,
    cor_Cabelo TEXT NOT NULL,
    imagem BYTEA UNIQUE,
    data_Medida DATE NOT NULL
);

-- Tabela: Questio_Socioeconomico (Tabela original com chave de data UNIQUE)
-- Armazena respostas a questionário socioeconômico (versão original)
CREATE TABLE IF NOT EXISTS Questio_Socioeconomico (
    id_Socio SERIAL PRIMARY KEY,
    id_Pessoa INTEGER NOT NULL REFERENCES Pessoa (id_Pessoa) ON DELETE CASCADE ON UPDATE CASCADE,
    data DATE UNIQUE NOT NULL,
    preocupacao_Conseguir_Comida BOOLEAN NOT NULL,
    comeu_Saudavel_sempre BOOLEAN NOT NULL,
    comeu_Todo_Dia BOOLEAN NOT NULL,
    ficou_Dia_Sem_Comer BOOLEAN NOT NULL,
    comeu_Menos_Pelos_Outros BOOLEAN NOT NULL,
    criancas_Comeram_Pouco BOOLEAN NOT NULL,
    criancas_Dormiram_Com_Fome BOOLEAN NOT NULL
);
