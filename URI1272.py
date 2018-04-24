n=input()
for index in xrange(n):
    e=raw_input().split()
    resposta=""
    for i in xrange(len(e)):
        resposta+=e[i][0]
    print resposta
