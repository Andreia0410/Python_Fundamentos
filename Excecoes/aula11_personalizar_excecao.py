#############################Exceções com messagens personalizadas############################
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
        
while True:    
    try:
        x = int(input('Entre com uma nota de o a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior do que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor do que 0.')
        break
    except ValueError:
        print('Valor inválido, digite apenas números.')
    except InputError as ex:
        print(ex)
        