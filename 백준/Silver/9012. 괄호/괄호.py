t = int(input())


for i in range(t):
    j = input()
    fl = 0

    for i in j:
        if i == "(":
            fl +=1
        elif i == ")":
            fl -=1
        
        if fl < 0:
            break
    
    if fl == 0:
        print ("YES")

    else:
        print ("NO")