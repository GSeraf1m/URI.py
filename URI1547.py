n=input()
for index in xrange(n):
    perto=101
    entrada=raw_input().split()
    a=int(entrada[0])
    nmr=int(entrada[1])
    valores=[0]*a
    entradas=raw_input().split()
    for i in xrange(a):
        if abs(int(entradas[i])-nmr)<perto:
            posicao=i+1
            perto=abs(nmr-int(entradas[i]))
    print posicao
