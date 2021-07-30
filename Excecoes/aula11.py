#############################Exceções e encadeamento de exceções############################
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética.')
except IndexError:
    print('Erro ao acessar índice inválido da lista.')
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção.')
finally:
    print('Sempre executa.')
    print('Fechando arquivo.')
    arquivo.close()
