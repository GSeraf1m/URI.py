try:
    while True:
        n=input()
        cont=0
        tamanhos=[]
        pes=[]
        for index in xrange(n):
            sapato=raw_input().split()
            tamanho=sapato[0]
            pe=sapato[1]
            entrou=False
            for i in xrange(len(tamanhos)):
                if tamanhos[i]==tamanho and pe!=pes[i]:
                    cont+=1
                    entrou=True
                    del tamanhos[i]
                    del pes[i]
                    break
            if not entrou:
                tamanhos.append(tamanho)
                pes.append(pe)
        print cont
except EOFError:
    pass
