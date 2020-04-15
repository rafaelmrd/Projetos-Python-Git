

class Funcionarios():
    def contar_salario(self, horas_trabalhadas): # horas_trabalhadas - é um atributo pois enta dentro de uma classe.
        self.valor_por_hora_trab = 50
        self.h_t = horas_trabalhadas
        self.salario = self.valor_por_hora_trab*self.h_t
        return self.salario

# Usando self para fazer com que minhas variaveis locais h_t, ..., do método contar_salario
# estejam associadas ao meu objeto funcinario_1.
# self.h_t = funcinario_1.h_t.

funcinario_1 = Funcionarios()
sal = funcinario_1.contar_salario(2)

# print('Valor por hora trabalhada: {}'.format(funcinario_1.valor_por_hora_trab))
print('Valor por hora trabalhada: {}'.format(50))

print('Horas trabalhadas: {}'.format(funcinario_1.h_t))

print('Salário = {}*{}: {}'.format(funcinario_1.valor_por_hora_trab, funcinario_1.h_t, sal))


