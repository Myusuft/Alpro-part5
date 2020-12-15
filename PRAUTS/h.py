import sys
n = int(input())
xi = list(map(int,input().split()))
length = len(xi)
nilai = 0

for i in range(length-1):
    for j in range(length-1):
        if xi[j] < xi[j+1]:
            tmp = xi[j]
            xi[j] = xi[j+1]
            xi[j+1] = tmp

for i in range(length):
    if xi[i]==xi[0]:
        nilai = nilai +1


yi = list(map(int,input().split()))
length = len(yi)
nilai = 0

for i in range(length-1):
    for j in range(length-1):
        if yi[j] < yi[j+1]:
            tmp = yi[j]
            yi[j] = yi[j+1]
            yi[j+1] = tmp

for i in range(length):
    if yi[i]==yi[0]:
        nilai = nilai +1


for i in xi:
    for j in yi:
        if len(xi) == len(yi):
            hasil = i*j
            print(hasil)




