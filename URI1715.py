entradas=raw_input().split()
n,m=int(entradas[0]),int(entradas[1])
a = [[] for i in xrange(n)]
cont = 0
for index in xrange(n):
    entradas=raw_input().split()
    for i in xrange(m):
        a[i].append(int(entradas[i]))
for i in xrange(m):
    if 0 not in a[]:
        cont+=1
print cont
