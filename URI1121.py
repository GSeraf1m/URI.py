entrada=raw_input()
y=[0,1,0,-1]
z=[-1,0,1,0]
cardeais=['N','L','S','O']
while(entrada!="0 0 0"):
    entrada=entrada.split()
    a,b,c=int(entrada[0]),int(entrada[1]),int(entrada[2])
    cont=0
    matriz=[]
    for i in range(a):
        matriz.append([0]*b)
    for i in xrange(a):
        entradas=raw_input()
        for index in xrange(b):
            matriz[i][index]=entradas[index]
            if entradas[index] == "N" or entradas[index] == "S" or entradas[index] == "L" or entradas[index] == "O":
                pi=i
                pindex=index
    for i in xrange(4):
        if matriz[pi][pindex] == cardeais[i]:
            x=i
            break
    entradas=raw_input()
    for i in xrange(c):
        if entradas[i]=='E':
            x=(x+3)%4
        elif entradas[i]=='D':
            x=(x+1)%4
        elif (pi+z[x]!=a)and(pindex+y[x]!=b)and(pi+z[x]>=0)and(pindex+y[x]>=0):
            variavel=matriz[pi+z[x]][pindex+y[x]]
            if(variavel != '#'):
                matriz[pi][pindex]='.'
                if variavel == '*':
                    cont+=1
                pi+=z[x]
                pindex+=y[x]
    print cont
    entrada=raw_input()
##  N
##O   L
##  S 
