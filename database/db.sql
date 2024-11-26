CREATE DATABASE cadastro;

USE cadastro;

CREATE TABLE IF NOT EXISTS usuario(
    cod INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome CHAR(50) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR (100) NOT NULL,
    cidade VARCHAR (20) NOT NULL
);

CREATE TABLE IF NOT EXISTS fotos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome_foto VARCHAR(255),
    foto LONGBLOB,
    data_captura DATETIME,
    usuario_id INT UNSIGNED,
    FOREIGN KEY (usuario_id) REFERENCES usuario(cod)
);