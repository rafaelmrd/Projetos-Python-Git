from math import ceil

class Funcionarios():
    def contar_salario(self, horas_trabalhadas, valor_por_hora_trab):
        v_p_h_t = valor_por_hora_trab
        h_t = horas_trabalhadas
        salario = v_p_h_t * h_t
        return salario

# Instanciando a class no meu objeto funcinario_1.
funcinario_1 = Funcionarios()
sal = funcinario_1.contar_salario(2, 50)

print('Valor por hora trabalhada: {}'.format(50))
print('Horas trabalhadas: {}'.format(ceil(sal/50) )) # Sem o self. Passando dois atributos.
print('Salário = {}'.format(sal)) # Sem o self

# Parametros dentro de uma classe = atributos.
# Sem o self eu nao consigo ter acesso as váriaveis v_p_h_t e h_t locais.

# https://www.youtube.com/watch?v=RhtsCbKyYoA
# Aulão Python sobre Classes, Objetos, Métodos, Herança, Construtor

