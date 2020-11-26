Data = [7,2,10,9,1]
length = len(Data)
nilai = list(map(int,input().split()))

l = nilai[0]
r = nilai[1]

for i in range(length-1):
    for j in range(length-1):
        if Data[j] < Data[j+1]:
            tmp = Data[j]
            Data[j] = Data[j+1]
            Data[j+1] = tmp
             
print(Data[l-1:r])




5877