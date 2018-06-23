n=input()
for index in xrange(n):
    frase=raw_input()
    frase=frase.lower()
    letras=[0]*27
    maior=0
    cont=""
    for i in xrange(len(frase)):
        if ord(frase[i])>96 and ord(frase[i])<123:
            letras[(ord(frase[i])-97)]+=1
    for i in xrange(26):
        if letras[i]>maior:
            maior=letras[i]
            cont=chr(i+97)
        elif letras[i]==maior:
            cont+=chr(i+97)
    print cont
