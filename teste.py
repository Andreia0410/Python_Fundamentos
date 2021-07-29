class Geladeira:
  def __init__(self):
    self.temperatura = -20
    self.minimo = -2
    self.maximo = 2

  def regularTemperatura(self):
    if self.temperatura > self.minimo:
      self.temperatura -= 1
    elif self.temperatura < self.minimo:
      self.temperatura += 1
  
  def mostrarTemperatura(self):
    print('Atual: {}.'.format(self.temperatura))

geladeira = Geladeira()
print('A temperatura da geladeira: {}'.format(geladeira.temperatura))
geladeira.regularTemperatura()
print('A nova temperatura é : {}'.format(geladeira.regularTemperatura()))

# class Carro:
#     def __init__(self):
#         self.motor = 'desligado'
#         self.movimento = False

#     def ligar(self):
#         self.motor = 'ligado'
    
#     def acelerar(self):
#         if self.motor == 'ligado':
#             self.movimento = True

#     def carro_em_movimento(self):
#         return self.movimento

# carro = Carro()
# carro.acelerar()
# carro_em_movimento = carro.carro_em_movimento()
# print(carro_em_movimento)

class Liquidificador:
  def __init__(self):
    self.velocidade = 0
    self.power = False

  def velocidade_A(self):
    #lacuna1
    if self.power:
      self.velocidade = 1
    
  def velocidade_B(self):
    #lacuna2
    if self.power:
      self.velocidade = 2

  def velocidade_Z(self):
    self.velocidade = 0  
    self.power = 0


# liquidificador = Liquidificador()

# class ArCondicionado:
#   def __init__(self):
#     self.temperatura = 20
  
#   def aumentarTemperatura(self):
#     if self.temperatura < 30:
#       self.temperatura += 1

#   def diminuirTemperatura(self):
#      if self.temperatura < 18:
#          self.temperatura -= 1

# def minha_funcao(numero):
#     if numero % 2 == 0:
#         return '{} é par'.format(numero)
#     else:
#         return '{} é ímpar'.format(numero)
#     return "zero é neutro"

# resultado = minha_funcao(0)
# print(resultado)
        