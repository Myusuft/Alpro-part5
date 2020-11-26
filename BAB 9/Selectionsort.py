list_a = [ 5 , 4 , 2 , 1 , 3 ]
length = len(list_a)
for i in range(length -1 ):
    smallest = i
    for j in range(i+ 1 , length):
        if list_a[j] < list_a[smallest]:
            smallest = j
            tmp = list_a[smallest]
            list_a[smallest] = list_a[i]
            list_a[i] = tmp
            print(list_a)

