import random

while True:
    number=random.randint(1,10)
    try:
        guess=int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("wow, you guessed correctly.")
        elif guess < number:
            print("Too low, better luck next time.")
        elif guess > number:
            print("Oops,too high, Try again.")

    except ValueError:
        print("Invalid input.Please enter a number between 1 and 10.")
        continue #skip to the next round if input is invalid

    print(f"The correct number was: {number}")

    while True:
        again =input("play another round? yes/no: ").strip() .lower()
        if again=="yes":
          break #start next round
        elif again =="no":
          print("Thanks for playing.")
          exit()
        else:
          print("Pleasetype 'yes' or 'no' .")