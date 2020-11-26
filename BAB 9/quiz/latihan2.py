def urutkan (s, length):
    for i in range(length -1 ):
        for j in range(length -1 ):
            if s[j]>s[j+1]:
                tmp = s[j]
                s[j] = s[j+1]
                s[j+1] = tmp
s = list(input())
z = list(input())

urutkan(s, len(s))
urutkan(z, len(z))

if s==z:
    print( "SAMA" )
else :
    print( "TIDAK SAMA" )