while True:
    
        import random 
        number=random.randint(1,10)
        guess=int(input("Guess a number between 1 and 10: "))
        if guess ==number:
            print("wow, you guessed correctly.")
        elif guess< number:
            print("too low, better luck next time.")
        elif guess> number:
            print("Oops,too high ,try again later.")
        else:
            print("Invalid input,try again")
        print(f"The correct number was : {number} ")
        again=input("play another round? yes/ no : ")
        if again.lower()!="yes":
                break
print("Thanks for playing.")