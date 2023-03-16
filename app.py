import random
import time
active = True


guesses_left = 0
starting_money = 100

while active:
    time.sleep(1)
    guesses_left += 5
    secret_number = random.randint(1,10)
    print(f"Hello and welcome to the casino. You have {starting_money}.")
    question_money = int(input("How much would you like to bet? "))

    while question_money > starting_money:
        question_money = int(input("You may only bet up to 100! "))
        

    while guesses_left > 0:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret_number:
            print("Congrats you have guessed the number!")
            starting_money += question_money
            print(f"You now have {starting_money}")
            break
        elif guess > secret_number:
            print("Too high, guess again !")
        else:
            print("Too low guess again")

        guesses_left -= 1
    
    if guesses_left == 0:
        starting_money -= question_money
        print(f"You are out of guesses! You now have {starting_money}")