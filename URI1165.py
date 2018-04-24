n=input()
for index in xrange(n):
    a=input()
    cont=0
    for i in xrange(1,a):
          if a%i==0:
              cont+=i
    if cont<2:
        print a,"eh primo"
    else:
        print a,"nao eh primo"
