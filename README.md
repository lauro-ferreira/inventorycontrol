# 📊 Projeto Controle de Estoque
Um projeto simples com python e mySQL para controle de estoque. Ele permite adicionar produtos, editar produtos, remover e fazer consultas em produtos cadastrados.

## Tecnologias Usadas
- Python (MySQL Connector, Pandas)   
- MySQL (Banco de dados relacional)

## 📂 Estrutura
### Configuração do Banco de Dados
O primeiro passo é criar o banco de dados e a tabela:

CREATE DATABASE estoque;
USE estoque;

CREATE TABLE estoque_produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    categoria VARCHAR(50),
    data_de_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_de_venda TIMESTAMP NULL DEFAULT NULL,
    data_ultima_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    fornecedor VARCHAR(50)
);
