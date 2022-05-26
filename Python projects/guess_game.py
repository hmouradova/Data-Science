import random 

number=random.randint(0, 100)
count=0

while True:
    n=int(input('Try to guess the number I am thinking of!: '))
    count+=1
    
    if n==number:
        print(f'Congrats! You guessed it correctly!\nIt took you {count} guesses!')
        break
        
    elif n>number:
        print('The number is lower than what you guessed!')
        
    else:
        print('The number is greater than what you guessed!')