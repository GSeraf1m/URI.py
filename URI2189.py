a=input()
cont=0
while(a!=0):
    cont+=1
    entradas=raw_input().split()
    convidados=[]
    premio=0
    for index in xrange(0,a):
        convidados.append(int(entradas[index]))
    for i in xrange(0,a):
        if convidados[i]==i+1:
            premio= convidados[i]
    print "Teste %d\n%d\n"%(cont, premio)
    a=input()
