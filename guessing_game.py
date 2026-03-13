import random
lowest_value=1
highest_value=100
guesses=0
is_running=True
answer=random.randint(lowest_value,highest_value)

print("-----------PYTHON GUESSING GAME-----------")
print(f"CHOOSE A NUMBER BETWEEN {lowest_value} - {highest_value}.")

while is_active:
    guess=input("ENTER YOUR GUESS:")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess < lowest_value or guess > highest_value:
            print("GUESS IS OUT OF RANGE.")
            print(f"PLEASE SELECT A NUMBER BETWEEN {lowest_value} and {highest_value}:")
        elif guess> answer:
            print("Too High! Try again!")
        elif guess<answer:
            print("Too Low! Try again!")
        else:
            print(f"CORRECT! THE ANSWER WAS {answer}")
            print(f"NO OF GUESSES ={guesses}")
            is_running=False     
    else:
        print("INVALID GUESS")
        print(f"PLEASE SELECT A NUMBER BETWEEN {lowest_value}-{highest_value}:")

