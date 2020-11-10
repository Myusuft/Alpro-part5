kalimat = input()
hitung = 0
for i in range(len(kalimat)):
    if kalimat[i] <= chr(96) and kalimat[i] >= chr(65):
        hitung = hitung + 1
print(hitung)
    

