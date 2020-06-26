# w= novo arquivo a= atualizar arquivo

def escrever_arquivo(texto):
    arquivo = open('C:/temp/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    txt = arquivo.read()
    print(txt)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/PycharmProjects/')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Rafael, 10,10.5,5\nEmerson, 10,7,8,9\nJose,10,5,4,10'
    # atualizar_arquivo('notas.txt',aluno)
    # ler_arquivo('teste.txt')