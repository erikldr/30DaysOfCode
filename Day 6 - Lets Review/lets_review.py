N = int(input().strip())

list_strings = []
for i in range(N):
    list_strings.append(input())


for x in list_strings:
    str_1 = ""
    str_2 = ""
    for i, j in zip(range(len(x)), x):
        if(i % 2 == 0):
            str_1 += j
        else:
            str_2 += j
    print(str_1, str_2)
        
