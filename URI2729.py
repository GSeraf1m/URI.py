n=input()
for index in xrange(n):
    lista=raw_input().split()
    lista=set(lista)
    lista=list(lista)
    lista.sort()
    lista = " ".join(lista)
    print lista
