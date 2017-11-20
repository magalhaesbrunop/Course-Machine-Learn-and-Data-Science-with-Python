class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimirNome(self):
        print(self.nome)
p = Pessoa('Bruno', 30)
p.imprimirNome()

"""
m = Pessoa('Bruno', 30)
print(type(m),'\n')

print('',m.nome, '\n', m.idade)

w = Pessoa('Galya', 21)
print('', w.nome, '\n', w.idade)
"""

class Conta:
    def __init__(self, cliente, numero):
        self.cliente = cliente
        self.numero = numero

class ContaEspecial(Conta):
    def __init__(self, cliente, numero, limite=0):
        Conta.__init__(self, cliente, numero)
        self.limite = limite

conta = ContaEspecial('Bruno', '1234', 100)
print(conta.limite)
print(conta.numero)


