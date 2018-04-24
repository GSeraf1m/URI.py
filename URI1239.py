try:
    while True:
        e=raw_input()
        b=0
        i=0
        resposta=""
        for ind in xrange(len(e)):
            if e[ind]=='_':
                if i==0:
                    resposta+="<i>"
                    i=1
                else:
                    resposta+="</i>"
                    i=0
            elif e[ind]=='*':
                if b==0:
                    resposta+="<b>"
                    b=1
                else:
                    resposta+="</b>"
                    b=0
            else:
                resposta+=e[ind]
        print resposta
except EOFError:
    pass
