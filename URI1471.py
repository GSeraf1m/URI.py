try:
    while True:
        entradas=raw_input().split()
        tam=int(entradas[0])
        n=int(entradas[1])
        voltaram=raw_input().split()
        nvoltaram=[]
        if tam==n:
            print "*"
        else:
            mergulhadores= []
            for i in xrange(1,tam+1):
                mergulhadores.append(str(i))
            for i in xrange(tam):
                if mergulhadores[i] not in voltaram:
                    print mergulhadores[i],
            print "\n",
except EOFError:
    pass
