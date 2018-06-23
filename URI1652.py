entrada=raw_input().split()
regular=[]*int(entrada[0])
irregular=[]*int(entrada[0])
respostas=[]*int(entrada[1])
for index in xrange(int(entrada[0])):
    entradas=raw_input().split()
    regular.append(entradas[0])
    irregular.append(entradas[1])
for index in xrange(int(entrada[1])):
    palavra=raw_input()
    if palavra in regular:
        for i in xrange(int(entrada[0])):
            if palavra==regular[i]:
                palavra=irregular[i]
    elif palavra.endswith('y') and palavra[-2]!='a' and palavra[-2]!='e' and palavra[-2]!='i' and palavra[-2]!='o' and palavra[-2]!='u':
        palavra=palavra[0:-1:]
        palavra+="ies"
    elif palavra.endswith('o') or palavra.endswith('s') or palavra.endswith('ch') or palavra.endswith('sh') or palavra.endswith('x'):
        palavra+="es"
    else:
        palavra+='s'
    respostas.append(palavra)
for index in xrange(len(respostas)):
    print respostas[index]
