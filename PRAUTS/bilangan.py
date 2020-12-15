digit = int(input())
x = list(map(int, input().split()))

for i in x:
    while 
for i in range(0,x):
    
    cek = True
    for j in range(2, i):
        if i % j == 0:
            cek = False
            break
    if cek:
        nilai = i
if nilai <= 2:
    print("Tidak ada bilangan prima lebih kecil dari 2")

else:
    print("bilangan prima terbesar sebelum",x, "adalah", nilai)