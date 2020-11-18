#Buatlah sebuah fungsi yang memiliki sebuah parameter yang bertipe list dan berisi
#daftar nama orang (hanya terdiri dari satu kata). Lalu kembalikan sebuah string yang
#merupakan nama terpanjang.
x = list(map(str,input().split(" ")))

def namaya(nama):
    terpanjang = ""
    panjang = 0
    for i in range(len(nama)):
        if len(nama[i]) > panjang:
            terpanjang = nama[i]
            panjang = len(nama[i])

    return terpanjang

print (namaya(x))

