n=input()
horas=n/3600
minutos=(n/60)-(horas*60)
segundos=(n-(minutos*60))-(horas*3600)
print "%d:%d:%d" % (horas, minutos, segundos)
