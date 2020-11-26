def mergesort (list_a, l, r):
    length = len(list_a)
    if r > l:
        mid = (l + r) // 2
        mergesort(list_a, l, mid)
        mergesort(list_a, mid+ 1 , r)
        i = l
        j = mid+ 1
        k = 0
        temp_list = [ 0 ]*(r-l+ 1 )

    # Merge
        while i <= mid and j <= r:
            if list_a[i] < list_a[j]:
                temp_list[k] = list_a[i]
                i+= 1
            else :
                temp_list[k] = list_a[j]
                j+= 1
                k+= 1
        while i <= mid:
            temp_list[k] = list_a[i]
            i+= 1
            k+= 1
        while j <= r:
            temp_list[k] = list_a[j]
            j+= 1
            k+= 1
        for i in range(len(temp_list)):
            list_a[l+i] = temp_list[i]

list_a = [ 5 , 4 , 2 , 1 , 3 ]
mergesort(list_a, 0 , len(list_a) -1 )
print(list_a)
