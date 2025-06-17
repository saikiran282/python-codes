n=[1,2,3,4,5,6,7,8]
odd=[]
even=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)
