a=["my name is rajeev "]
b=""
e=""
d=[]
for i in range(len(a)):
     b=b+a[i]  
     print(b)

for i in range(len(b)):   
         if b[i] !=" ":
          e=e+b[i]
         else :
              d.append(e)
              e=""

print(d)

         
         
        


       
