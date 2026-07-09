from services import cadastrar_autor, listar_autores, buscar_autor_por_id, atualizar_autor, deletar_autor, cadastrar_livro, listar_livros, buscar_livro_por_id , cadastrar_leitores  , atualizar_leitor , deletar_leitor

while True:
    print("1 - Cadastrar usuario")
    print("2 - Gerenciar autores")
    print("3 - Gerenciar livros")
    print("0 - Sair")
    escolher = input("escolha uma opcao:")

    if escolher == "0":
        break

    if escolher == "2":


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



    elif escolher == "3":

        while True:
            print("1 - Cadastrar livro")
            print("2 - Listar livros")
            print("3 - Buscar livro por id")
            print("4 - Atualizar livro")
            print("5 - Deletar livro")
            print("6 Filtrar por titulo ou autor")
            print("0 - Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "0":
                break

            if opcao == "1":
                titulo = input("Digite o título do livro: ")
                ISBN = input("Digite o ISBN do livro: ")
                ano_de_publicacao = input("Digite o ano de publicação do livro: ")
                quantidade_total_de_livros = int(input("Digite a quantidade total de livros: "))
                autores_do_livro = input("Digite os autores do livro (separados por vírgula): ").split(",")
                cadastrar_livro(titulo, ISBN, ano_de_publicacao, quantidade_total_de_livros,  autores_do_livro)
                print("Livro cadastrado com sucesso!")

            if opcao == "2":
                from services import listar_livros
                livros = listar_livros()
                for livro in livros:
                    print(f"ID: {livro.id}, Título: {livro.titulo}, ISBN: {livro.ISBN}, Ano de Publicação: {livro.ano_de_publicacao}, Quantidade Total de Livros: {livro.quantidade_total_de_livros}, Quantidade Disponível: {livro.quantidade_disponivel}, Autores: {', '.join(livro.autores_do_livro)}")


            elif opcao == "3":
                from services import buscar_livro_por_id
                id_livro = int(input("Digite o id do livro "))
                livro = buscar_livro_por_id(id_livro)
                if livro:
                    print(f"ID: {livro.id}  , Titulo: {livro.titulo} ,ISBN {livro.ISBN} , Ano de publicação: {livro.ano_de_publicacao}, Quantidade Disponivel: {livro.quantidade_disponivel}, Autores {livro.autores_do_livro} ")

                else :
                    print("LIVRO NAO ENCONTRADO" \
                    "" \
                    "" \
                    '')

            elif opcao == "4":
                from services import atualizar_livro
                id = int(input("Digite o id do livro: "))
                titulo = input("Digite o título do livro: ")
                ISBN = input("Digite o ISBN do livro: ")
                ano_de_publicacao = input("Digite o ano de publicação do livro: ")
                quantidade_total_de_livros = int(input("Digite a quantidade total de livros: "))
                autores_do_livro = input("Digite os autores do livro (separados por vírgula): ").split(",")      
                atualizado_livro = atualizar_livro(id,titulo,ISBN,ano_de_publicacao,quantidade_total_de_livros,autores_do_livro)
                if atualizado_livro:
                    print("Livro atualizado")

                else :print("livro nao encontrado") 


            elif opcao == "5":
                from services import deletar_livro
                id = int(input("Digite o id do livro que queira deletar"))
                livro_deletado = deletar_livro(id)
                if livro_deletado:
                    print("livro deletado com sucesso")

                else:
                    print("Livro nao encontrado")

            elif opcao == "6":
                from services import listar_livros_por_filtro
                termo = input("Digite um título ou autor para buscar: ")
                encontrados = listar_livros_por_filtro(termo)
                if encontrados:
                    for livro in encontrados:
                        print(f"ID: {livro.id}, Título: {livro.titulo}, Autores: {', '.join(livro.autores_do_livro)}")
                else:   
                    print("Nenhum livro encontrado com esse filtro.")  




    elif escolher == "1":
        while True:
            print("1 - Cadastrar Leitor")
            print("2 - Consultar Leitores")
            print("3 - Buscar por id")
            print("4 - Atualizar Leitor")
            print("5 - Deletar leitor")
            print("0 - Sair")



            opcao = input("digite uma opção: ")

            if opcao == "0":
                break


            elif opcao == "1":
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                telefone = int(input("Digite seu telefone: "))
                cadastrar_leitores(nome , email , telefone  )
                print("Leitor cadastrado com sucesso")



            elif opcao == "2":
                from services import listar_leitor
                Leitores = listar_leitor ()
                for leitor in Leitores:
                     print(f"ID: {leitor.id } , nome: {leitor.nome}, telefone {leitor.telefone} email: {leitor.email}" )



            elif opcao == "3":
                from services import buscar_leitor_id
                id_leitor = int(input("Digite o ID do leitor: "))
                id_leitor = buscar_leitor_id (id_leitor)
                if id_leitor:
                    print(f"nome: {leitor.nome}, telefone {leitor.telefone} email: {leitor.email}")

                else:
                    print("leitor  nao encontrado")






            elif opcao == "4":
                from services import atualizar_leitor
                id = int(input("digite o id do leitor:"))
                nome = input("Digite  o nome: ")
                email = input("Digite o email: ")
                telefone = int(input("Digite o telefone: "))
                leitor_atualizado = atualizar_leitor(id,nome,email,telefone)
                if leitor_atualizado:
                    print("leitor atualizado com sucesso")

                else:
                    print("Leitor nao encontrado")


            elif opcao == "5":
                from services import deletar_leitor
                id = int(input("Difgite o id do Leitor que queira deletar"))
                leitor_deletado = deletar_leitor(id)
                if leitor_deletado:
                    print("Leitor deletado com sucesso")
                else:
                    print("Leitor nao encontrado")






            