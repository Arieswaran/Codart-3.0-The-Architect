t=int(input())
for i in range(t):
    n=int(input())
    c=4
    for j in range(1,n+1):
        c+=2**j
    print c%1000000007
