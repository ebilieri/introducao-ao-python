#type set
#não repete elementos
conjunto = {1,2,3,4,4,5}
conjunto.add(6)
conjunto.discard(2)
print(type(conjunto))
print(conjunto)

# união
conjunto1 = {1,2,3,4,5,6}
conjunto2 = {5,6,7,8,9}
conjuntoUniao = conjunto1.union(conjunto2)
print('Uninão: {}' .format(conjuntoUniao))
# interseção
conjuntoIntersecao = conjunto1.intersection(conjunto2)
print('Intersecao: {}' .format(conjuntoIntersecao))
# diferença
conjuntoDiferenca = conjunto1.difference(conjunto2)
print(conjuntoDiferenca)
conjuntoDiferenca2 = conjunto2.difference(conjunto1)
print(conjuntoDiferenca2)

# diferenca simetrica
conjuntoDiffSimentrica = conjunto1.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}' .format(conjuntoDiffSimentrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjuntoSubset = conjunto_a.issubset(conjunto_b)
print(conjuntoSubset)

lista = ['cachorro', 'gato', 'gato', 'elefante', 'cachorro']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)