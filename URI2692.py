entradas=raw_input().split()
e=[]
s=[]
saida=[]
for i in xrange(int(entradas[0])):
    entrada=raw_input().split()
    e.append(entrada[0])
    s.append(entrada[1])
for index in xrange(int(entradas[1])):
    consertada=""
    frase=raw_input()
    for i in xrange(len(frase)):
        if frase[i] in e:
            for ind in xrange(len(e)):
                if frase[i]==e[ind]:
                    consertada+=s[ind]
        elif frase[i] in s:
            for ind in xrange(len(s)):
                if frase[i]==s[ind]:
                    consertada+=e[ind]
        else:
            consertada+=frase[i]
    saida.append(consertada)
for i in xrange(len(saida)):
    print saida[i]
