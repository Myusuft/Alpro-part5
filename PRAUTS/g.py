N = int(input())
Data = list(map(int,input().split()))
length = len(Data)
nilai = 0
for i in range(length-1):
    for j in range(length-1):
        if Data[j] > Data[j+1]:
            tmp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = tmp

print(Data[1])
print(length)