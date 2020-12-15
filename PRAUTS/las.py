
Data = input().split()
Data = list(Data)

for i in range(len(Data)-1):
    for j in range(len(Data)-1):
        if Data[j] > Data[j+1]:
            tmp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = tmp
Data.reverse()
print(Data[1])