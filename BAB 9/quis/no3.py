Data = [10, 50, 40,85, 85, 10, 85, 30, 10, 85]
length = len(Data)
nilai = 0

for i in range(length-1):
    for j in range(length-1):
        if Data[j] < Data[j+1]:
            tmp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = tmp

for i in range(length):
    if Data[i]==Data[0]:
        nilai = nilai +1

print("nilai terbesarnya berjumlah:", nilai)