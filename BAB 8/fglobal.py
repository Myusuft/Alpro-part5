def fungsi_satu (n):
    global x
    x = 14

def fungsi_dua (n):
    return n+x
    
x = 5
print(x)
print(fungsi_dua(10))
fungsi_satu(10)
print(fungsi_dua(50))


