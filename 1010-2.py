def contagem(string):
    string=string.replace(' ', '')
    conta = {}
    for caractere in string:
        if caractere in conta:
            conta[caractere]+=1
    else: 
        conta[caractere]=1
    return(conta)

texto ="exercicios 2 do dia 10 de outubro"
resultado = contagem(texto)
print(resultado)