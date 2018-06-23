try:
    while True:
        cont=0
        vogais=raw_input()
        frase=raw_input()
        for i in xrange(len(frase)):
            if frase[i] in vogais:
                cont+=1
        print cont
except EOFError:
    pass
