
def mulai(nilai):
    for i in range (1,nilai+1,1):
        print(i)
    for i in range(nilai-1,0,-1):
        print(i)

nilai = int(input())
print(mulai(nilai))