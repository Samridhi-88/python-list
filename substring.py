mainstr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah"
newstr=mainstr.split(" ")
i=0
a=" "
while i<len(newstr):
    if newstr[i]=="over":
        a=a+"on"+" "
    else:
        a=a+newstr[i]+" "
    i+=1
print(a)