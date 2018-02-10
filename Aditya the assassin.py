n=int(input())
a=[i for i in range(1,n+1)]
n=int(input())
for i in range(n):
    b=(raw_input().strip()).split(' ')
    if(b[0]=='?'):
        print len(a)
    else:
        for j in range(int(b[1]),int(b[2])+1):
            if j in a:
                a.remove(j)
