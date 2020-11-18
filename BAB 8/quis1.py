def fungsi_satu (x):
    global L
    L = [1,2,3,4,5]
    for i in L:
        return i + x

x = int(input())
print(x)
print(fungsi_satu(x))
