try:
    while True:
        e=raw_input()
        num,nocaps,caps,simb,= False,False,False,False
        if len(e)>=6 and len(e)<=32:
            for i in xrange(len(e)):
                if e[i].isdigit():
                    num=True
                elif e[i].islower():
                    nocaps=True
                elif e[i].isupper():
                    caps=True
                else:
                    simb=True
            if num and nocaps and caps and not simb:
                print "Senha valida."
            else:
                print "Senha invalida."
        else:
            print "Senha invalida."
except EOFError:
    pass
