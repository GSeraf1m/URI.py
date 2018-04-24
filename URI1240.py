n=input()
for index in xrange(n):
    entrada = raw_input().split()
    a = entrada[0]
    b = entrada[1]
    cont = 1
    for i in range(len(b)):
        cont *= 10
    if int(a)%cont == int(b):
        print "encaixa"
    else:
        print "nao encaixa"
