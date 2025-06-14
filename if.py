order=input("chicken,bief,mutton,fish")
bill=0
if order=='chicken' or order=='CHICKEN' or order=='Chicken':
    Quantity=int(input('how much you want'))
    bill+=200*Quantity
elif order=='bief' or order=='BIEF' or order=='Bief':
    Quntity=int(input('how much you want'))
    bill+=500*Quantity
elif order=='mutton' or order=='MUTTON' or order=='Mutton':
      Quantity=int(input('how much you want'))
      bill+=700*Quantity
elif order=='fish' or order=='FISH' or order=='Fish':
    Quantity=int(input('how much you want'))
    bill+=100*Quantity
elif order=='chicken,mutton' or order=='Chicken,Mutton' or order=='CHICKEN,MUTTON' or order=='Chicken,mutton' :
    chicken=int(input('how much chicken'))
    mutton=int(input('how much mutton'))
    bill+=(chicken*200)+(mutton*700)
else:
    print('ok')

print(bill)
