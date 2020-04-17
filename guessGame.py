
import random
print('Welcome to guess game\n Please guess a number between 0 and 100')
guessNum = random.randrange(0, 100)
count = 1
while count <=5:
    guessInput = int(input(f'{count} guess : '))
    if guessInput == guessNum:
        print('You won the game')
        break
    elif guessInput < guessNum and count < 5:
        print('Increase your guessed number')
    elif guessInput > guessNum and count < 5:
        print('decrease your guessed number')
    count = count + 1
else:
    print('You fail')
