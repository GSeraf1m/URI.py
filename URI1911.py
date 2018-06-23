while True:
    nomes=[]
    cont=0
    original=[]
    n=input()
    if n==0:
        break
    for i in xrange(n):
        entrada=raw_input().split()
        nomes.append(entrada[0])
        original.append(entrada[1])
    n=input()
    for index in xrange(n):
        entrada=raw_input().split()
        nome=entrada[0]
        aula=entrada[1]
        for i in xrange(len(nomes)):
            errado=0
            if nome==nomes[i]:
                for ind in xrange(len(original[i])):
                    if original[i][ind]!=aula[ind]:
                        errado+=1
                if errado>1:
                    cont+=1
    print cont
