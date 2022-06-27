import random

print("Number Guessing Game")

number = random.randint(1,20)
chances = 0
print("Guess a number between 1 and 20:")

while chances < 7:

 guess = int(input("Enter your guess:"))
 
 if guess == number:
  print("Congrats, you guess the number", guess)		
  break
 elif guess < number:
  print("Your guess was low: Guess the number higher than", guess)

 else:
  print("Your guess was high: Guess the number lower than", guess)
        
chances +=1

if not chances < 7:

  	print("You lost! The number is", number)
