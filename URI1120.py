entrada=raw_input()
while(entrada!="0 0"):
    entrada=entrada.split()
    falha=entrada[0]
    valor=entrada[1]
    valormodificado=""
    for i in xrange(len(valor)):
        if ord(valor[i])!=ord(falha):
            valormodificado+=valor[i]
    if len(valormodificado)>0:
        if(valormodificado[0]=='0'):
            for i in xrange(1,len(valormodificado)):
                if valormodificado[i]!='0':
                    valormodificado=valormodificado[i::]
                    break
        if valormodificado[0]=='0':
            valormodificado="0"    
        print valormodificado
    else:
        print "0"
    entrada=raw_input()
