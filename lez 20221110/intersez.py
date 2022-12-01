'''Scrivete un programma Python per trovare l'intersezione (i numeri comuni) di due liste usando:. 
funzione lambda
funzione filter → non ancora vista insieme
lista_uno = [2, 4, 6, 8, 10]
lista_due = [1, 2, 3, 8, 94, 9]'''
l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3, 8, 94, 9]

l1 = [1, 2, 3]
l2 = [11, 12, 13, 14, 15, 15]

#print (*map(lambda x : x * y, list((map(lambda s : s in l2))), l1))

#print(list(map(lambda x, y: x + y, l1, l2)))

#print( list((map(lambda s : s, l2))))



'''lista_uno = [2, 4, 6, 8, 9]
lista_due = [1, 2, 3, 8, 94, 21, 38, 9]
print("Liste originali")
print(lista_uno)
print(lista_due)
numeri_comuni = list(filter(lambda x: x in lista_uno, lista_due))
print ("I numeri comuni sono: ",numeri_comuni)
'''

l1 = [12, 11, 3]
l2 = [11, 12, 13]

fnz = lambda x: lambda y: x == y

matrix = list(map(lambda x: list(filter(x, l1)), map(fnz, l2)))
print(matrix)