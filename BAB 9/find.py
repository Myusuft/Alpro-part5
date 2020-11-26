n = int(input()) # nilai yang dicari
list_a = [ 3 , 2 , 4 , 6 , 5 , 11 , 8 , 9 ] # list pencarian
index = 1
for i in range(len(list_a)):
    if list_a[i] == n:
        index = i 
        break
if index != 1 :
    print(n, "ditemukan di indeks" , index)
else :
    print(n, "tidak ditemukan" )