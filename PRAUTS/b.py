import sys
n = int(input())
list_a = list(map(int,input().split()))
length = len(list_a)
angka = 0
for i in range(length -1 ):
    for j in range(length -1 ):
        if list_a[j] > list_a[j+1]:
            angka = angka +1
            tmp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = tmp
#print(list_a)
#print(angka)
sys.stdout.write(str(list_a))
sys.stdout.write(str(angka))
