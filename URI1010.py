leitura1 = raw_input().split()
leitura2 = raw_input().split()
a1,b1,c1 = float(leitura1[0]), float(leitura1[1]), float(leitura1[2])
a2,b2,c2 =  float(leitura2[0]), float(leitura2[1]), float(leitura2[2])
preco1=b1*c1
preco2=b2*c2
total=preco1+preco2
print "VALOR A PAGAR: R$ %1.2f" % total
