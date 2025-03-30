def consultar_produto(conexao, nome=None, id_produto=None):
    from main import conexao
    from main import pd
    cursor = conexao.cursor(dictionary=True)

    if id_produto:
        query = f"SELECT * FROM estoque_produtos WHERE id = {id_produto}"
    elif nome:
        query = f"SELECT * FROM estoque_produtos WHERE nome LIKE '%{nome}%'"
    else:
        query = "SELECT * FROM estoque_produtos"

    cursor.execute(query)
    resultados = cursor.fetchall()

    if resultados:
        df = pd.DataFrame(resultados)
        print(df)
    else:
        print("Nenhum produto encontrado.")

    cursor.close()
