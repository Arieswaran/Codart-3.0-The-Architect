n=int(input())
for i in range(n):
    N,Q=[int(i) for i in (raw_input().strip()).split(' ')]
    s=[int(i) for i in (raw_input().strip()).split(' ')]
    s1=min(s)
    s2=max(s)
    for j in range(Q):
        if(s1<=int(input())<=s2):
            print "Satyam_Y"
        else:
            print "Satyam_N"
