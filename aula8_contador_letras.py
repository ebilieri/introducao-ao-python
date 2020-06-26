def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quatidade = len(x)
        contador.append(quatidade)
    return contador

def teste():
    return 'teste'


if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
