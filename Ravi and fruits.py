n=int(input())
for i in range(n):
    a=[int(j) for j in (raw_input().strip()).split(' ')]
    c=1
    for j in range(1,a[0]):
        c+=c+2
    r=c%a[1]
    print r
