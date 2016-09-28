def  isitpossible( a,  b,  c,  d):
    if a==c and b==d:
        print "Yes"
    elif a==c and b<d:
        isitpossible(a, b+a, c, d)
    elif b==d and a<c:
        isitpossible(a+b, b, c, d)
    elif b<d and a<c:
        isitpossible(a+b, b, c, d)
    else:
        print "No"
        
print isitpossible(1,4,1,3)