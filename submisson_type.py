char=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
a_c,n_c,t_c,x_c,u_c,g_c=0,0,0,0,0,0
while i<len(char):
    if char[i]=="a":
        a_c+=1
    elif char[i]=="n":
        n_c+=1
    elif char[i]=="t":
        t_c+=1
    elif char[i]=="x":
        x_c+=1
    elif char[i]=="u":
        u_c+=1
    elif char[i]=="g":
        g_c+=1
    else:
        print("no")
    i+=1
print("a",a_c)
print("n",n_c)
print("t",t_c)
print("x",x_c)
print("u",u_c)
print("g",g_c)