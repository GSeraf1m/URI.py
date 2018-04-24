n=input()
alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for index in xrange(n):
    cont=0
    entrada=raw_input()
    for i in xrange(len(alfabeto)):
        if alfabeto[i] in entrada:
            cont+=1
    if cont==26:
        print "frase completa"
    elif cont>12:
        print "frase quase completa"
    else:
        print "frase mal elaborada"
