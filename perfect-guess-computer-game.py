import random as rd

computer_random_number = rd.randint(1,10)
user_guess_number = -1
guess = 0

while(user_guess_number != computer_random_number):
    guess+=1
    user_guess_number = int(input("Enter the Number that is your Guess between 1 to 10 : "))    
    if(user_guess_number>computer_random_number):
        print("Lower please")
    elif(user_guess_number<computer_random_number):
        print("HIhger please")

print(f"You have guess the Number correctly as {computer_random_number}")
print(f" Your total guess are {guess}")
