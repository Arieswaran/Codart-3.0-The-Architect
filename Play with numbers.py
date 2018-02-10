n=int(input())
for i in range(n):
    a=[int(j) for j in (raw_input().strip()).split(' ')]
    arr=[int(j) for j in (raw_input().strip()).split(' ')]
    c=0
    for j in range(1,a[0]+1):
        for k in arr:
            if j%k==0:
                c+=1
                break
    print c
        
