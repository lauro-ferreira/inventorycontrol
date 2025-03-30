def adicionar_produtos(conexao, produto, quantidade, preco, categoria, fornecedor):
    from main import conexao
    cursor = conexao.cursor()

    query = """
    INSERT INTO estoque_produtos (produto, quantidade, preco, categoria, fornecedor)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (produto, quantidade, preco, categoria, fornecedor)

    try:
        cursor.execute(query, values)
        conexao.commit()
        print(f"Produto {produto} adicionado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cursor.close()


