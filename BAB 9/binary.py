def cari_binary (list_a, l, r, nilai):
    idtengah = (l + r) // 2
    if nilai == list_a[idtengah]:
        return idtengah
        
    elif l > r:
        return -1
    elif nilai > list_a[idtengah]:
        return cari_binary(list_a, idtengah+ 1 , r, nilai)
    elif nilai < list_a[idtengah]:
        return cari_binary(list_a, l, idtengah -1 , nilai)

n = int(input()) # nilai yang dicai
list_a = [ 1 , 3 , 5 , 6 , 6 , 7 , 8 , 9 ] # list pencarian
indeks = cari_binary(list_a, 0 , len(list_a) -1 , n)
if indeks != -1 :
    print(n, "ditemukan di indeks" , indeks)
else :
    print(n, "tidak ditemukan" )

