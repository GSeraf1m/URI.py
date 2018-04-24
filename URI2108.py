frase=raw_input().split()
maior=0
palavramaior=""
while(frase[0]!='0'):
    tamanho=[]*len(frase)
    for i in xrange(len(frase)):
        tam=frase[i].count("")-1
        tamanho.append(str(tam))
        if tam>=maior:
            maior=tam
            palavramaior=frase[i]
    print ('-'.join(tamanho))
    frase=raw_input().split()
print "\nThe biggest word:",palavramaior
