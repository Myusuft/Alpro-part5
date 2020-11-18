#Buatlah sebuah fungsi yang memiliki parameter tiga buah nilai, lalu mengembalikan
#nilai terbesar dari ketiga nilai tersebut.
def mulai():
    nilai = list(map(int,input().split()))

    if nilai[0] >= nilai[1] and nilai[0] >= nilai[2]:
        return nilai[0]

    if nilai[1] >= nilai[0] and nilai[1] >= nilai[2]:
        return nilai[1]

    if nilai[2] >= nilai[0] and nilai[2] >= nilai[1]:
        return nilai[2]

print(mulai())

