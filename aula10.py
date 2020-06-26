from datetime import date, time, datetime, timedelta


def trabalando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))

    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)

    print(type(data_atual))
    print(type(data_atual_str))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.year)
    print(data_atual.date())
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2020, 6, 7, 18, 40, 55)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '20/01/2019 12:30:25'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

    # from datetime import datetime, time
    data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data, hora))


if __name__ == '__main__':
    # trabalando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()
