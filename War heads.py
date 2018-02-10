n,r=[int(i) for i in (raw_input().strip()).split(' ')]
b=[int(i) for i in (raw_input().strip()).split(' ')]
c=0
while(len(b)!=0):
    s=b[0]
    i=1
    if(len(b)==1):
        c+=1
        break
    while(s+r>=b[i]):
        i+=1
        if(len(b)>=i):
            break
    del b[0:i+r]
    c+=1
print c
