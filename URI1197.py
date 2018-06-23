try:
    while True:
        entrada=raw_input().split()
        v=int(entrada[0])
        t=int(entrada[1])
        print 2*v*t
except EOFError:
    pass
