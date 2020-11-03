a = [[ 0 , 1 , 2 ], [ 'a' , 'b' , 'c' ], [ 8 , 8 ]]
print(len(a))
print(len(a[ 2 ]))

a = ["x"] * 10
print(a)

c = [[ 0 , 1 , 2 ], [ 3 , 4 ], [ 5 , 6 , 7 ]]
for i in c:
    for j in i:
        print(j)

b = "x" *10
print(b)

a = [[ 0 , 1 , 2 ], [ 3 , 4 ], [ 5 , 6 , 7 ]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

a = [ 0 ]* 3
for i in range(len(a)):
    a[i] = [ 0 ]* 4
    print(a)

b = "x" *10
print(b)

#string
s = "murah" * 3
print(s)

s = "murah" + "123"
print(s)

f = [ 0 ]* 3
for i in range(3):
    f[i] = list(map(int, input().split()))

