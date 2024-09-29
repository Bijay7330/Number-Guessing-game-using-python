print('''\tWelcome to the game.
          Today we are guessing the random number.
          If your input number matches the computer's generated random number,
          You will win. 
      ''')

import random
def GuessTheNumber(number):
     random_number = random.randint(1,101)

     if number <= 0 :
        print("please enter natural number")
          
     else: 
        if random_number == number :
          print(f"You won , you guess the right number {number}") 
        else :
          print(f"Oops! sorry you guess the wrong number , correct number is {random_number} and your guess is {number}")



def main():
    
    number = int(input("please , enter your number >>"))
    
    result = GuessTheNumber(number)
    print(result)


main()    
    