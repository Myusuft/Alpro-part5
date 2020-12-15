
def selection_sort(angka):
    for pos in range(len(angka)-1,0,-1):
        pos_max = 0
        for x in range(1,pos+1):
            max_sementara = angka[pos_max]
            if max_sementara < angka[x]:
                pos_max = x
        angka[pos_max], angka[pos] = angka[pos], angka[pos_max]

angka = list(map(int,input().split()))
selection_sort(angka)
print(angka)

