#Buatlah sebuah fungsi yang memiliki sebuah parameter yang bertipe list dan berisi
#daftar nama orang (hanya terdiri dari satu kata). Lalu kembalikan sebuah string yang
#merupakan nama terpanjang.

def mulai():
    nama1 = str(input())
    nama2 = str(input())
    nama3 = str(input())
    if len(nama1) >= len(nama2) and len(nama1) >= len(nama3):
        return nama1
    if len(nama2) >= len(nama1) and len(nama2) >= len(nama3):
        return nama2
    if len(nama3) >= len(nama2) and len(nama3) >= len(nama1):
        return nama3

print(mulai())
