class Autor:
    def __init__(self,id,nome,nacionalidade,data_nascimento,idade):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.idade = idade


class Livro:
    def __init__(self,id,titulo,ISBN,ano_de_publicacao,quantidade_total_de_livros,quantidade_disponivel,autores ):
        self.id = id
        self.titulo = titulo
        self.ISBN = ISBN
        self.ano_de_publicacao = ano_de_publicacao
        self.quantidade_total_de_livros = quantidade_total_de_livros
        self.quantidade_disponivel = quantidade_disponivel
        self.autores = autores
        

class Emprestimo:
    def __init__(self, id, livro, usuario, data_de_retirada, data_prevista_devolucao, data_real_devolucao, status):
        self.id = id
        self.livro = livro
        self.usuario = usuario
        self.data_de_retirada = data_de_retirada
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_real_devolucao = data_real_devolucao
        self.status = status

class Leitor:
    def __init__(self,id,nome,email,telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
