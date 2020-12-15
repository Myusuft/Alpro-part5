n = int(input())
masukan = list(map(int, input().split()))
angka = 0

n = int(input())
print()
for k in range (2,n+1)  :
    cek=True
    for i in range(2,k) :
        if k%i==0:
            cek=False
            break
    if cek==True:
        print(k)