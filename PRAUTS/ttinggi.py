import sys
total = int(input())
data = []
for i in range (total):
    x = int(input())
    data.append(x)

for i in range(len(data)-1):
    for j in range(len(data)-1):
        if data[j] > data[j+1]:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp
def cari (list_a, l, r, nilai):
    idtengah = (l + r) // 2
    if nilai == list_a[idtengah]:
        return idtengah
        
    elif l > r:
        return -1
    elif nilai > list_a[idtengah]:
        return cari(list_a, idtengah+ 1 , r, nilai)
    elif nilai < list_a[idtengah]:
        return cari(list_a, l, idtengah -1 , nilai)
        
adi = 165
n = adi
list_a = data # list pencarian
indeks = cari(list_a, 0 , len(list_a) -1 , n)
if indeks != -1 :
    sys.stdout.write(str(indeks+1))
#else :
 #   sys.stdout.write(str("tidak ditemukan")
