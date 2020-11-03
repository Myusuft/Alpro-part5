a = [[ 0 , 1 , 2 ], [ 'a' , 'b' , 'c' ], [ 8 , 8 ]]
print(len(a))
print(len(a[ 2 ]))


#perulanganlist
a = [[ 0 , 1 , 2 ], [ 3, 4 ], [ 5 , 6 , 7 ]]
for i in a:
    for j in i:
        print(j)

#indexlist
a = [[ 0 , 1 , 2 ], [ 3 , 4 ], [ 5 , 6 , 7 ]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

