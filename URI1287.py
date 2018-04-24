try:
    while True:
        numero=raw_input()
        saida=""
        for i in xrange(len(numero)):
            if numero[i]=='l':
                saida+='1'
            elif numero[i]=='o' or numero[i]=='O':
                saida+='0'
            elif ord(numero[i])>47 and ord(numero[i])<58:
                saida+=numero[i]
            elif not (numero[i]==' ' or numero[i]==','):
                saida=''
                break
        if len(saida)>0:
            if int(saida)>=0 and int(saida)<=2147483647:
                if(saida[0]=='0'):
                    for i in xrange(1,len(saida)):
                        if saida[i]!='0':
                            saida=saida[i::]
                            break
                    if saida[0]=='0':
                        saida="0" 
                print saida
            else:
                print "error"
        else:
            print "error"
except EOFError:
    pass
