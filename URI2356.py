try:
    while True:
        d=raw_input()
        s=raw_input()
        resistente=True
        for i in xrange(len(s)):
            if s not in d:
                resistente = False
        if resistente:
            print "Resistente"
        else:
            print "Nao resistente"
except EOFError:
    pass
