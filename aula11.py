
lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não possível dividir por zero')
except IndexError:
    print('Indice invalido')
except Exception as ex:
    print('Erro: {}' .format(ex))
else:
    print('Não houve erros')
finally:
    print('Finalizado')