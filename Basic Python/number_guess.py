'''
1.ფუნქც()
    დაგენერირდა რიცხვი
    ფუნქცია ეკითხება რა რიცხვი შეიძლება იყოს
    მომხ-ს შეჰყავს რიცხვი, მოწმდება
    თუ მეტია ამბობს მეტია
    თუ ნაკლებია ამბობს ნაკლებია
    თუ ტოლია მაშინ გილოცავ
'''


from random import randint

def guess():
# block 1
    x = randint(0,100)
    print(x)
    
# block 2
    g = int(input('Enter number ' + f'\t'))
    while g!=x:
        if g<x:
            g = int(input('enter bigger number'))
            
        elif g>x:
           g = int(input('enter smaller number'))
        
    print(f'Congratulation!! you correctly  guess number {x}')        
        
guess()        
    


