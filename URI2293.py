entradas=raw_input().split()
n,m=int(entradas[0]),int(entradas[1])
maior=0
soma=0
matriz=[]
for i in range(n):
        matriz.append([0]*m)
for i in xrange(n):
    entradas=raw_input().split()
    for index in xrange(m):
        matriz[i][index]=int(entradas[index])
for i in xrange(n):
    soma=0
    for index in xrange(m):
        soma+=matriz[i][index]
    if maior < soma:
        maior = soma
for i in xrange(m):
    soma=0
    for index in xrange(n):
        soma+=matriz[index][i]
    if maior < soma:
        maior = soma
print maior
