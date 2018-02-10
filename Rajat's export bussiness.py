#Arieswaran
a=[int(i) for i in (raw_input().strip()).split(' ')]
b=0
b+=a[3]
while(a[2]!=0):
    if(a[0]!=0):
        b+=1
        a[0]-=1
        a[2]-=1
    else:
        b+=a[2]
        a[2]=0
while(a[1]!=0):
    if(a[1]>1):
        b+=1
        a[1]-=2
    elif(a[0]>1):
        b+=1
        a[1]-=1
        a[0]-=2
    elif(a[0]==1):
        b+=1
        a[1]=0
        a[0]=0
while(a[0]!=0):
    r=a[0]/4
    b+=r
    r=a[0]%4
    if(r>0):
        b+=1
print b*500
    
