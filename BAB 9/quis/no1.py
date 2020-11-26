Data = [7,2,10,9,1]
length = len(Data)
nilai = int(input())

for i in range(length-1):
    for j in range(length-1):
        if Data[j] < Data[j+1]:
            tmp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = tmp

print(Data[:nilai])
