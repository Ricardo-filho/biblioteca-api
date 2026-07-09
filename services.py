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

livros = []

def cadastrar_livro(titulo, ISBN, ano_de_publicacao, quantidade_total_de_livros, autores_do_livro):
    id = len(livros) + 1
    quantidade_disponivel = quantidade_total_de_livros
    livro = Livro(id, titulo, ISBN, ano_de_publicacao, quantidade_total_de_livros, quantidade_disponivel, autores_do_livro)
    livros.append(livro)
    return livro


def listar_livros():
    return livros

def buscar_livro_por_id(id):
    for livro in livros:
        if livro.id == id:
            return livro
    return None


def atualizar_livro(id,titulo, ISBN, ano_de_publicacao, quantidade_total_de_livros, autores_do_livro):
    for livro in livros:
        if livro.id == id:
            livro.titulo = titulo
            livro.ISBN = ISBN
            livro.ano_de_publicacao = ano_de_publicacao
            livro.quantidade_total_de_livros = quantidade_total_de_livros
            livro.autores_do_livro = autores_do_livro
            return livro
    return None


def deletar_livro(id):
    for livro in livros:
        if livro.id == id:
            livros.remove(livro)
            return True
        return False
    


def listar_livros_por_filtro(termo):
    resultado = []
    for livro in livros:
        if termo.lower() in livro.titulo.lower():
            resultado.append(livro)
        else:
            for autor in livro.autores_do_livro:
                if termo.lower() in autor.lower():
                    resultado.append(livro)
                    break 
    return resultado


Leitores =  []

def cadastrar_leitores(nome ,email,telefone):
    id = len(Leitores)+1
    leitor = Leitor(id,nome ,email,telefone)
    Leitores.append(leitor)
    return leitor


def listar_leitor():
    return Leitores

def buscar_leitor_id(id):
    for leitor in Leitores :
        if leitor.id == id:
            return leitor
    return None



def atualizar_leitor(id,nome ,email,telefone):
    for leitor in Leitores:
        if leitor.id == id:
            leitor.nome = nome
            leitor.email = email
            leitor.telefone = leitor
            return leitor
        return None
    

def deletar_leitor(id):
    for leitor in Leitores:
        if leitor.id == id:
            Leitores.remove(leitor)
            return True
        return False