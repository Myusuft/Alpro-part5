
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charset1 = 'abcdefghijklmnopqrstuvwxyz' 
charlist = list(charset)
charlist1 = list(charset1)
numlist = list(range(1,27)) 

def a1z26(source, extras):
    if come[1] == 0:
        come[1] = charset 
        res_adder = []
        len_processor = 0 
        length = len(source) 
        for searcher in source: 
            while len_processor < length: 
                try: 
                    processor = source[len_processor] 
                    founder = numlist.index(processor) 
                    converter = charlist[founder] 
                    len_processor += 1 
                    res_adder.append(converter)
                except: 
                    converter = ' ' 
                    len_processor += 1 
                    res_adder.append(converter) 
        result = ''.join(res_adder) + extras 
        print(result)
    if come[1] == 0:
        come[1] = charset1
        res_adder = []
        len_processor = 0 
        length = len(source) 
        for searcher in source: 
            while len_processor < length: 
                try: 
                    processor = source[len_processor] 
                    founder = numlist.index(processor) 
                    converter = charlist1[founder] 
                    len_processor += 1 
                    res_adder.append(converter)
                except: 
                    converter = ' ' 
                    len_processor += 1 
                    res_adder.append(converter) 
        result = ''.join(res_adder) + extras 
        print(result)  
    	
come = list(map(int,input().split()))
source = list(map(int, input().split()))
extras = ''
a1z26(source, extras) 
