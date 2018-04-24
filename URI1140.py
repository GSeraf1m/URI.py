frase=raw_input()
inicial=""
while frase[0]!='*':
    frase=frase.lower()
    frase=frase.split()
    tautograma=True
    inicial=frase[0][0]
    for i in xrange(1,len(frase)):
        if frase[i][0]!=inicial:
            tautograma=False
    if tautograma:
        print 'Y'
    else:
        print 'N'
    frase=raw_input()
