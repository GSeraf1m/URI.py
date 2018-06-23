entrada=raw_input().split()
n=int(entrada[0])
m=int(entrada[1])
words=[]
values=[]
for i in xrange(n):
    entrada=raw_input().split()
    words.append(entrada[0])
    values.append(int(entrada[1]))
for index in xrange(m):
    cont=0
    texto=[]
    while x[0]!='.':
        x=raw_input().split()
        if x[0]=='.':
            break
        for i in xrange(len(x)):
            texto.append(x[i])
    for i in xrange(len(texto)):
        if texto[i] in words:
            for ind in xrange(n):
                if texto[i]==words[ind]:
                    cont+=values[ind]
    print cont
