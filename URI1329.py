n=input()
while(n!=0):
    mary=0
    john=0
    entradas=raw_input().split()
    for i in xrange(0,n):
        if int(entradas[i])==0:
            mary+=1
        elif int(entradas[i])==1:
            john+=1
    print "Mary won %d times and John won %d times"%(mary,john)
    n=input()
