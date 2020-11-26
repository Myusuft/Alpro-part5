def tukar (l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
id = [ 1 , 2 , 3 , 4 , 5 ]
n1 = [ 90 , 80 , 70 , 80 , 90 ]
n2 = [ 10 , 10 , 20 , 40 , 80 ]
length = len(id)
for i in range(length -1 ):
    for j in range(length -1 ):
        if n1[j] < n1[j +1 ]:
            tukar(id, j, j +1 )
            tukar(n1, j, j +1 )
            tukar(n2, j, j +1 )
        elif n1[j] == n1[j +1 ]:
            if n2[j] > n2[j +1 ]:
                tukar(id, j, j +1 )
                tukar(n1, j, j +1 )
                tukar(n2, j, j +1 )
print(id)

