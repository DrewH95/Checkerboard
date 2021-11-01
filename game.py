def Checkerboard (x,y): 
    result = []
    for i in range(0,x):
        temp = []
        for j in range (0,y):
            temp.append((i+j) % 2)
        result.append(temp)


    return result

collumn = Checkerboard(8,8)
for row in collumn:
    print (row)