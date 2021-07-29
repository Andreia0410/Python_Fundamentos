# Função é tudo que retorna um valor
# Método é o que não retorna.

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
         
         
    def soma(self):
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def multiplcacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__=='__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a,'\n ',
    calculadora.soma(),'\n',
    calculadora.sub(),'\n',
    calculadora.multiplcacao(),'\n',
    calculadora.divisao())
