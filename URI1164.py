n=input()
for index in xrange(n):
    a=input()
    soma=0
    for i in xrange(1,a):
          if a%i==0:
              soma+=i
    if (soma==a):
        print a,"eh perfeito"
    else:
        print a,"nao eh perfeito"
