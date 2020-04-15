
# __init__ - método construtor, ele vai construir/definir os valores iniciais dos nossos atributos
# Parametros dentro de uma classe = atributos.
class Funcionarios:
    def __init__(self, valor: int):
        self.valor = valor
    def funci1(self):
        self.valor = self.valor * 2

# Passando os atributos para a classe, pq o metodo construtor init
# faz com que esses atributos estejam relacionados com a class.
a = Funcionarios(1)
a.funci1()
a.valor

b = Funcionarios(2)
b.funci1()
b.valor

# c = a.funci1(2)

print('a.valor - Valor: {} '.format(a.valor))
print('b.valor - Valor: {} '.format(b.valor))

# print('c - Valor {}: '.format(c))




















