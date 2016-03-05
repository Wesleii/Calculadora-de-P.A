#!usr/bin/python

perg = raw_input('---> Qual vc quer descobrir? an, a1, n ou r? ')

if perg == 'an':
    a1 = int(raw_input('Diga o valor do primeiro termo: '))
    n = int(raw_input('O numero de termos e igual a? '))
    r = int(raw_input('Qual a razao? '))
    an = a1 + (n-1)*r
    print 'an = ',an
    lista = range(a1, an+r, r)
    print lista

if perg == 'a1':
    an = int(raw_input('Qual o valor de an? '))
    n = int(raw_input('O numero de termos e igual a? '))
    r = int(raw_input('Qual a razao? '))
    a1 = (n-1)*r
    s = an - a1
    print 'a1 = ',s
    lista = range(s, an+r, r)
    print lista

if perg == 'n':
    an = int(raw_input('Qual o valor de an? '))
    a1 = int(raw_input('Diga o valor do primeiro termo: '))
    r = int(raw_input('Qual a razao? '))
    a = an - a1
    n = a / r
    print 'n = ',n + 1
    lista = range(a1, an+r, r)
    print lista


if perg == 'r':
    an = int(raw_input('Qual o valor de an? '))
    a1 = int(raw_input('Diga o valor do primeiro termo: '))
    n = int(raw_input('O numero de termos e igual a? '))
    a = a1 + (n-1)
    r = an / a
    print 'r = ',r
    lista = range(a1, an+r, r)
    print lista
