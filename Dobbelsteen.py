import random

def Dobbelsteen(min, max):
    Dice = int(random.randint(min, max))
    
    print('Het gegooide getal is ' + str(Dice))
    
    if Dice >= 6:
        print('Er is een fout ontstaan')
    else:
        print('De functie is goed gegaan')


Dobbelsteen(1, 6)

