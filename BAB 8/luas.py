def luas_segitiga (a, t):
    return a * t * 0.5
def luas_trapesium (a, b, t):
    return (a + b) * t * 0.5

def mulai ():
    print( "Pilih menu berikut:" )
    print( "[1] Luas Segitiga" )
    print( "[2] Luas Trapesium")
    print( "inputkan pilihan (1, 2, atau 3):" )
    inp = input()
    if inp == 1 :
        print( "Inputkan alas dan tinggi:" )
        a = int(input())
        t = int(input())
        print(luas_segitiga(a, t))
    elif inp == 2 :
        print( "Inputkan dua sisi sejajar dan tinggi:" )
        a = int(input())
        b = int(input())
        t = int(input())
        print(luas_trapesium(a, b, t))
    else :
        print( "Inputan tidak valid!" )

print( "Memulai program..." )
mulai()
print( "Program selesai..." )
