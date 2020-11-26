nama = [ 0 ]* 5
for i in range( 5 ):
    nama[i] = input()
for i in range( 4 ):
    for j in range( 4 ):
        if nama[j] > nama[j+1]:
            tmp = nama[j]
            nama[j] = nama[j+1]
            nama[j+1] = tmp
print(nama)

