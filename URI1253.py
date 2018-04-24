n=input()
for index in xrange(n):
    cdg=""
    texto=raw_input()
    chave=input()
    for i in xrange(len(texto)):
        if (ord(texto[i])-chave)<65:
            cdg+=chr((ord(texto[i])+26)-chave)
        else:
            cdg+=chr(ord(texto[i])-chave)
    print cdg
