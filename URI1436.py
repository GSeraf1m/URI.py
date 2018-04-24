t=input()
for i in xrange(t):
    entradas=raw_input().split()
    n=int(entradas[0])
    idade=[]
    for index in xrange(0,n-1):
        idade.append(int(entradas[index+1]))
        capitao=(n-1)/2
    print "Case %d: %d"%(i+1,idade[capitao])
