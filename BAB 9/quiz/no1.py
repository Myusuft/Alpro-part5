list_a = [ 3 , 5 , 2 , 5 , 7 , 8 , 1 , 0 , 4 , 14 , 3 , 5 , 12 , 5 , 9 , 8 , 11 , 10 , 5 , 1 ,
13 , 1 , 8 , 5 , 7 , 2 , 1 , 0 , 0 , 41 ]
length = len(list_a)
for i in range(length -1 ):
    for j in range(length -1 ):
        if list_a[j] > list_a[j+1]:
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
            print(list_a)

#binarysearch
n = int(input()) # nilai yang dicari
index = 1
for i in range(len(list_a)):
    if list_a[i] == n:
        index = i 
        break
if index != 1 :
    print(n, "ditemukan di indeks" , index)
else :
    print(n, "tidak ditemukan" )