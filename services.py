from model import Autor, Livro,  Emprestimo, Leitor

autores = []

def cadastrar_autor(nome, nacionalidade, data_nascimento, idade):
    id = len(autores) + 1
    autor = Autor(id, nome, nacionalidade, data_nascimento, idade)
    autores.append(autor)
    return autor

def listar_autores():
    return autores

def buscar_autor_por_id(id):
    for autor in autores:
        if autor.id == id:
            return autor
    return None

def atualizar_autor(id, nome, nacionalidade, data_nascimento, idade):
    for autor in autores:
        if autor.id == id:
            autor.nome = nome
            autor.nacionalidade = nacionalidade
            autor.data_nascimento = data_nascimento
            autor.idade = idade
            return autor
    return None
        
def deletar_autor(id):
    for autor in autores:
        if autor.id == id:
            autores.remove(autor)
            return True
    return False
   

