lista = [1,3,5,7,9]
listAnimal = ['cachorro', 'coelho', 'gato', 'cavalo', 'iena', 'zebra', 'cabra', 'papagaio']

print(lista)
print(listAnimal[1])

for x in listAnimal:
    print(x)

soma=0
for x in lista:
    print(x)
    soma += x
print(soma)

print(sum(lista))
print(max(lista))
print(min(lista))

if 'gato' in listAnimal:
    print('existe')

listAnimal.append('lobo')
print(listAnimal)
listAnimal.pop() #remover ultimo
listAnimal.pop(1) #remover posição
listAnimal.remove('gato')
print(listAnimal)
listAnimal.sort() # ordenar
print(listAnimal)
listAnimal.reverse()
print(listAnimal)

# Tupla não permite alterar valor
tupla = (1,10,12,14,16) # criado entre parenteses
print(tupla)
print(len(tupla))

tuplaAnimal = tuple(listAnimal)
print(type(tuplaAnimal))

lista1 = [3, 5, 7, 10, 11]
resultado = []
for x in lista1:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)
