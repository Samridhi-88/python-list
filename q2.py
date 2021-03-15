a=[50,40,23,70,56,12,5,10,7]
i=0
b=[]
c=0
while i<len(a):
    if a[i]>20 and a[i]<40:
        b.append(a[i])
        c+=1
    i+=1
print(b,c)