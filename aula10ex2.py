class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    
class Mouse(Produto):  
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo

    def get_descricao(self):
        return self.descricao, self.tipo


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor
    
    def get_descricao(self):
        return self.descricao, self.autor


xxp = Mouse("xxp", 100, "um mouse grande", "gamer")
grat = Mouse("grat", 50, "um mouse pequeno", "escritorio")

l1 = Livro("Amore", 20, "amor romantico para sempre", "bruna")
l2 = Livro("odio", 10, "um odio para sempre", "pablo")

carrinho = [xxp, grat, l1, l2]

for i in carrinho:
    print(i.get_descricao())
