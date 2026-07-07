from services import cadastrar_autor, listar_autores, buscar_autor_por_id


while True: 
    print("1 - Cadastrar autor")
    print("2 - Listar autores")
    print("3 - Buscar autor por id")
    print("4 - Atualizar autor")
    print("5 - Deletar autor")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "0":
        break

    if opcao == "1":
        nome = input("Digite o nome do autor: ")
        nacionalidade = input("Digite a nacionalidade do autor: ")
        data_nascimento = input("Digite a data de nascimento do autor (dd/mm/aaaa): ")
        idade = input("Digite a idade do autor: ")
        cadastrar_autor(nome, nacionalidade, data_nascimento, idade)
        print("Autor cadastrado com sucesso!")


    elif opcao == "2":
        from services import listar_autores
        autores = listar_autores()
        for autor in autores:
            print(f"ID: {autor.id}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}, Data de Nascimento: {autor.data_nascimento}, Idade: {autor.idade}")


    elif opcao == "3":
        from services import buscar_autor_por_id
        id_autor = int(input("Digite o ID do autor: "))
        autor = buscar_autor_por_id(id_autor)
        if autor:
            print(f"ID: {autor.id}, Nome: {autor.nome}, Nacionalidade: {autor.nacionalidade}, Data de Nascimento: {autor.data_nascimento}, Idade: {autor.idade}")
        else:
            print("Autor não encontrado.")

    elif opcao == "4":
        from services import atualizar_autor
        id = int(input("Digite o ID do autor que deseja atualizar: "))
        nome = input("Digite o novo nome do autor: ")
        nacionalidade = input("Digite a nova nacionalidade do autor: ")
        data_nascimento = input("Digite a nova data de nascimento do autor (dd/mm/aaaa): ")
        idade = input("Digite a nova idade do autor: ")
        autor_atualizado = atualizar_autor(id, nome, nacionalidade, data_nascimento, idade)
        if autor_atualizado:
            print("Autor atualizado com sucesso!")
        else:
            print("Autor não encontrado.")

    elif opcao == "5":
        from services import deletar_autor
        id = int(input("Digite o ID do autor que deseja deletar: "))
        autor_deletado = deletar_autor(id)
        if autor_deletado:
            print("Autor deletado com sucesso!")
        else:
            print("Autor não encontrado.")


    else:
        print("Opção inválida. Tente novamente.")


        