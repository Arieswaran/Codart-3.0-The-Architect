n=int(input())
for i in range(n):
    a=[int(i) for i in (raw_input().strip()).split(' ')]
    if (a[1]-a[0]>1):
        print "NO"
    else:
        print "YES"
