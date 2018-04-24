n=input()
for i in xrange(n):
    nmr=raw_input()
    resposta=3
    if len(nmr)==3:
        if ("on" in nmr) or ("oe" in nmr) or ("ne" in nmr) or ("o" in nmr and "e" in nmr):
            resposta=1
        else:
            resposta=2
    print resposta
