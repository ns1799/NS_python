import random  #importing random module
n = random.randint(1, 100)  #generating random number between 1 to 100
a = None   #initializing variable a with a value not equal to n
guesses = 1 #initializing number of guesses
while(a != n):  #loop until the guessed number is equal to the generated number
    a = int(input("Guess the number: "))  
    if(a >n):       #if guessed number is greater than generated number
        print("Lower number please")
        guesses +=1     #incrementing number of guesses
    elif(a<n):    #if guessed number is less than generated number
        print("Higher number Please")
        guesses +=1  #incrementing number of guesses

print(f"You have guessed the number {n} correctly in {guesses} attempts") #printing success message with number of attempts