def editar_produto(conexao, id_produto, produto=None, quantidade=None, preco=None, categoria=None, fornecedor=None):
    from main import conexao
    cursor = conexao.cursor()

    # Criar uma lista dinâmica de colunas para atualizar
    updates = []
    values = []

    if produto is not None:
        updates.append("produto = %s")
        values.append(produto)
    if quantidade is not None:
        updates.append("quantidade = %s")
        values.append(quantidade)
    if preco is not None:
        updates.append("preco = %s")
        values.append(preco)
    if categoria is not None:
        updates.append("categoria = %s")
        values.append(categoria)
    if fornecedor is not None:
        updates.append("fornecedor = %s")
        values.append(fornecedor)

    # Se não houver nada para atualizar, sai da função
    if not updates:
        print("Nenhum dado foi passado para atualização.")
        return

    # Criar query dinâmica
    query = f"UPDATE estoque_produtos SET {', '.join(updates)} WHERE id = %s"
    values.append(id_produto)  # Adicionar ID no final da tupla de valores

    try:
        cursor.execute(query, tuple(values))  # Passando os valores corretamente
        conexao.commit()
        print(f"Produto {id_produto} atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
    finally:
        cursor.close()

