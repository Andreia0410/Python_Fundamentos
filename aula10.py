##################################Trabalhando e convertendo datas#########################
from datetime import date, time, datetime, timedelta


def trabalhando_date():
    data_atual = date.today()
    print(type(data_atual))
    # print(data_atual.strftime('%d/%m/%Y'))
    # print(data_atual.strftime('%A/%B/%Y')) # Nome do mÊs, ano com 4 digitos
    data_atual_str = data_atual.strftime('%A/%B/%Y')
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()]) 
    data_criada = datetime(2020, 6, 4, 15, 30, 20)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=20)
    print(nova_data) 
    

if __name__=='__main__':
    # trabalhando_time()
    trabalhando_datetime()
    