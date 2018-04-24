oitavas=[["A","B"],["C","D"],["E","F"],["G","H"],["I","J"],["K","L"],["M","N"],["O","P"]]
quartas=[[],[],[],[]]
semi=[[],[]]
final=[]
for i in xrange(0,8):
    gols=raw_input().split()
    time1=int(gols[0])
    time2=int(gols[1])
    if time1>time2:
        quartas[i-int((i+1)/2)].append(oitavas[i][0])
    else:
        quartas[i-int((i+1)/2)].append(oitavas[i][1])
for i in xrange(4):
    gols=raw_input().split()
    time1=int(gols[0])
    time2=int(gols[1])
    if time1>time2:
        semi[i-int((i+1)/2)].append(quartas[i][0])
    else:
        semi[i-int((i+1)/2)].append(quartas[i][1])
for i in xrange(2):
    gols=raw_input().split()
    time1=int(gols[0])
    time2=int(gols[1])
    if time1>time2:
        final.append(semi[i][0])
    else:
        final.append(semi[i][1])
gols=raw_input().split()
time1=int(gols[0])
time2=int(gols[1])
if time1>time2:
    print final[0]
else:
    print final[1]
