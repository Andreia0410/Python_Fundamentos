# Função é tudo que retorna um valor
# Método é o que não retorna.

class Calculadora:
    def __init__(self):
        pass
         
        def soma(self, valor_a, valor_b):
            return self.valor_a + self.valor_b

        def sub(self, valor_a, valor_b):
            return self.valor_a - self.valor_b

        def multiplcacao(self, valor_a, valor_b):
            return self.valor_a * self.valor_b

        def divisao(self, valor_a, valor_b):
            return self.valor_a / self.valor_b


calculadora = Calculadora()
print(calculadora.valor_a,'\n ',
calculadora.soma(),'\n',
calculadora.sub(),'\n',
calculadora.multiplcacao(),'\n',
calculadora.divisao())
