def fatora(a):
    vezes = a
    for i in xrange(a-1,0,-1):
        vezes*=i
    print vezes
fatora(input())
