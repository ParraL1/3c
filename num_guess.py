#Name: Lilliana Parra
#Github username: ParraL1
#Date: 1/19/2022
#description: guess the number, display how many tries it took to get the number

# asking user for input
num = int(input("Enter the integer for the player to guess.\n"))
# declaring variable to hold number of guess
count = 0
guess = int(input("Enter your guess.\n"))

while (True):
    count = count + 1
    # checking if larger
    if (guess > num):
        guess = int(input("Too high - try again:\n"))
        continue
    # checking if smaller
    elif (guess < num):
        guess = int(input("Too low - try again:\n"))
        continue
    else:
        break

# printing result
if count > 1:
     print("You guessed it in", count, "tries.")

if count == 1:
    print ("You guessed it in 1 try.")

