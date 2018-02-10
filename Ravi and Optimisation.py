n=int(input())
a=[]
c=0
for i in range(n):
    a.append(raw_input().strip())
for i in range(len(a)-1):
    for j in range(i,len(a)):
        f=1
        for k in a[i]:
            if k in a[j]:
                f=0
                break
        if f==1:
            c+=1
print c*2
