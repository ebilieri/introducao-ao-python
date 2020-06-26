contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['coelho', 'gato', 'boi']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b

print(soma(5, 10))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print(soma(10,5))
print(multiplicacao(10,5))

valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)
print(resultado)