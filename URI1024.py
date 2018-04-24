n=input()
for index in xrange(n):
    frasepassada=""
    frase=raw_input()
    for i in xrange(len(frase)):
        if (ord(frase[i])>64 and ord(frase[i])<91) or (ord(frase[i])>96 and ord(frase[i])<123):
            letra = ord(frase[i])+3
            frasepassada+=chr(letra)
        else:
            frasepassada+=frase[i]
    fraseinvertida=frasepassada[::-1]
    metade=len(frase)/2
    frasetruncada=fraseinvertida[:metade:]
    for i in xrange(len(frase)/2,len(frase)):
        frasetruncada+=chr(ord(fraseinvertida[i])-1)
    print frasetruncada
