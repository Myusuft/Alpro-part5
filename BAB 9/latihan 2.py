def anagram(t1, t2):
    if sorted(t1) == sorted(t2):
        #return True
        print("sama")
    else:
        print("tidak sama")

kata = list(map(str,input().split()))
print(anagram(kata[0],kata[1]))

