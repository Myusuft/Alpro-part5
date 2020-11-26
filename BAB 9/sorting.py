list_a = [ 5 , 4 , 2 , 1 , 3 ]
length = len(list_a)
for i in range(length -1 ):
    for j in range(length -1 ):
        if list_a[j] > list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
            print(list_a)


#Selectionsort
