from math import ceil

class Funcionarios():
    def contar_salario(self, horas_trabalhadas):
        valor_por_hora_trab = 50
        h_t = horas_trabalhadas
        salario = valor_por_hora_trab*h_t
        return salario

funcinario_1 = Funcionarios()
sal = funcinario_1.contar_salario(2)

print('Valor por hora trabalhada: {}'.format(50))

print('Horas trabalhadas: {}'.format(ceil(sal/50) ))

# Valor por hora trabalhada, horas trabalhadas, salario
print('Salário = {}*{}: {}'.format(50, 2, sal ))

# Tem os mesmos valores
# v_p_h_t = Funcionarios().contar_salario(2)
# sal = funcinario_1.contar_salario(2)

# Se eu tiro o self das variaveis dentro do método, contar_salario iria da esse erro:
# Erro linha 13, in <module>
#
#  print('Horas trabalhadas: {}'.format(funcinario_1.h_t))
# AttributeError: 'Funcionarios' object has no attribute 'h_t'
# o objeto 'Funcionarios' não tem atributo 'h_t'

# https://www.youtube.com/watch?v=RhtsCbKyYoA
# Aulão Python sobre Classes, Objetos, Métodos, Herança, Construtor
