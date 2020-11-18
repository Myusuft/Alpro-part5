def cek_huruf(huruf, kata):
    ada = False
    for i in kata:
        if huruf == i:
            ada = True

        if ada:
            print("huruf ditemukan")
            
        else:
            print("huruf tidak ada")
            
cek_huruf("a","Pakaian")


