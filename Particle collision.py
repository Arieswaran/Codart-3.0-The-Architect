#Arieswaran
n=int(input())
for i in range(n):
    p=int(input())
    if(p==1):
        print 0
        continue
    e=0
    for j in range(1,p):
        for k in range(j+1,p+1):
            e+=j*k
    print e
