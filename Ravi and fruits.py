n=int(input())
for i in range(n):
    a=[int(j) for j in (raw_input().strip()).split(' ')]
    c=1
    cc=2
    t=1
    for j in range(1,a[0]):
        c+=cc
        cc+=1
        #t+=c
    #print t,c
    r=c%a[1]
    print r
