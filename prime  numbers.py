n=[1,2,3,4,5,6,7,8,17]
d=0
np=[]
for i in n:
    d=0
    for m in range(1,len(n)+1):
        if i%m==0: 
            d+=1
        if d>2:
            n.remove(i)
            np.append(i)
            d=0
           
print(f"Prime numbers={n}")
print(f"Notprime numbers={np}")

    
 
