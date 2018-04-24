a=input()
if a>0 and a<=400:
    b=0.15*a
    print "Novo salario: %1.2f\nReajuste ganho: %1.2f\nEm percentual: 15 %%"%(a+b,b)
elif a>400 and a<=800:
    b=0.12*a
    print "Novo salario: %1.2f\nReajuste ganho: %1.2f\nEm percentual: 12 %%"%(a+b,b)
elif a>800 and a<=1200:
    b=0.10*a
    print "Novo salario: %1.2f\nReajuste ganho: %1.2f\nEm percentual: 10 %%"%(a+b,b)
elif a>1200 and a<=2000:
    b=0.07*a
    print "Novo salario: %1.2f\nReajuste ganho: %1.2f\nEm percentual: 7 %%"%(a+b,b)
else:
    b=0.04*a
    print "Novo salario: %1.2f\nReajuste ganho: %1.2f\nEm percentual: 4 %%"%(a+b,b)
