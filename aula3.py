# a = int(input('Valor 1: '))
# b = int(input('Valor 2: '))
# c = int(input('Valor 3: '))
#
# if a > b and a > c:
#     print('o maior numero é {}' .format(a))
# elif b > a and b > c:
#     print('o maior numero é {}' .format((b)))
# else:
#     print('o maior numero é {}' . format(c))
# print('Fim')

a = int(input('Valor: '))
resto = a % 2

if resto == 0:
    print('numero par')
else:
    print('numero é impar')