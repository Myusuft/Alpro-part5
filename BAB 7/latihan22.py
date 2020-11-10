kalimat = input()
kalimat = list(kalimat)
kode = [*range(65,91)]

print(kode)
for i in range(0, len(kalimat)):
    for j in kode:
        if(ord(kalimat[i])==j):
            kalimat[i] = kalimat[i].lower()

kalimat[0] = kalimat[0].upper()
kalimat = "".join(kalimat)
print(kalimat)