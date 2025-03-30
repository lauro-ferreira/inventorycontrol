def delete_product(conexao, id_produto):
    from main import conexao
    cursor = conexao.cursor()
    try:
        cursor.execute(f"DELETE FROM estoque_produtos WHERE id = {id_produto}")
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Produto {id_produto} deletado com sucesso.")
        else:
            print(f"Nenhum produto foi encontrado com ID {id_produto}")
    except Exception as es:
        print(f"Erro ao deletar {es}")
    finally:
        cursor.close()

