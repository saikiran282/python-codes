size=input('size of the cake(s/m/l)')
bill=0
if size=='s' or size=='S':
    bill+=100
elif size=='m' or size=='M':
    bill+=150
else:
    bill+=200
candle=input('do you want to candles (yes/no)')
if candle=='yes' or candle=='YES' or candle=='Yes' or candle=='YEs' or candle=='YeS' or candle=='yES' or candle=="y":
    size=input('enter the size of the candles (s/m/l)')
    if size=='s' or size=='S':
        bill+=15
    elif size=='m' or size=='M':
        bill+=20
    else:
        bill+=30
else:
    print('ok')
crackers=input('do you want to shorts(y/n)')
if crackers=='y' or crackers=='y':
    count=int(input('how many shoarts you want'))
    if count>=5:
       bill+=100*count
    elif count>=10:
        bill+=count*95
    else:
        bill+=count*105
fire=input('do you want to match matchbox or lighter(y/n)')
if fire=='y' or fire=='Y':
    fire2=input('lighter or matchbox')
    if fire2=='lighter':
        count=int(input('how many you want'))
        if (count>=1 ):
                bill+=10*count
       #small=int(input("how many lighters you want"))
       #if small>=1:
        #    bill+=10*small
    else:
       #large=int(input('how many match boxes you want'))
       #if large>=1:
        #   bill+=2*large
       count=int('how mant matchboxes you want')
       if count>=1:
            bill+=2*count               
else:
    print('ok')
    
print(bill)


         
          
