def segitiga(x):
    string = ""
    nilai = 1
    while nilai <= x:
        jml = nilai

        while jml > 0:
            string = string +"*"
            jml = jml - 1

        string = string + "\n"
        nilai = nilai + 1

    print(string)


segitiga(int(input()))


