#rotate image
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
e=[]
for i in range(len(a)):
    c=[]
    for j in range(len(a[i])-1,-1,-1):
        c.append(a[j][i])
    e.append(c)
print(e) 


        

        
