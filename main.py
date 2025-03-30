import mysql.connector
import pandas as pd
from add_product import adicionar_produtos
from edit_product import editar_produto
from delete_product import delete_product
from consultation import consultar_produto


# Função para conectar ao banco de dados
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="neto",
            password="neto",
            database="estoque"
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None  # Retorna None se a conexão falhar


# Criar conexão
conexao = conectar()


if conexao is None:
    print("Não foi possível conectar ao banco. Verifique as credenciais.")
else:
    try:
        while True:
            print("\n------ Menu ------")
            print("1. Adicionar Produto")
            print("2. Editar Produto")
            print("3. Deletar Produto")
            print("4. Consultar Produto")
            print("5. Sair")

            escolha = input("Digite uma alternativa: ").strip()  # Remover espaços extras

            if escolha == "1":
                produto = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                categoria = input("Categoria: ")
                fornecedor = input("Fornecedor: ")
                adicionar_produtos(conexao, produto, quantidade, preco, categoria, fornecedor)

            elif escolha == "2":
                id_produto = int(input("ID do produto: "))
                produto = input("Nome do produto (ou Enter para manter): ")
                quantidade = input("Nova quantidade (ou Enter para manter): ")
                preco = input("Novo preço (ou Enter para manter): ")
                categoria = input("Nova categoria (ou Enter para manter): ")
                fornecedor = input("Novo fornecedor (ou Enter para manter): ")

                quantidade = int(quantidade) if quantidade else None
                preco = float(preco) if preco else None

                editar_produto(conexao, id_produto, produto, quantidade, preco, categoria, fornecedor)

            elif escolha == "3":
                id_produto = int(input("ID do produto a ser deletado: "))
                delete_product(conexao, id_produto)

            elif escolha == "4":
                produto = input("Nome do produto para consulta: ")
                id_produto = input("ID do produto para consulta (ou Enter para ignorar): ")
                id_produto = int(id_produto) if id_produto else None
                consultar_produto(conexao, produto, id_produto)

            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida! Digite um número de 1 a 5.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
        conexao.close()  # Garante que a conexão será fechada
