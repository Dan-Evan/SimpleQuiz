#Name of author: Daniel Evans
#Date created: August 9, 2021
#Description: This program plays a quiz game where the user is asked various questions and the
#             program will tell them if it is correct and at the send they will get their total 
#             score and percentage.
#Credit: Made this following along with YouTuber 'Tech with Tim'

#Welcome to Daniel's Computer Quiz!
print("Welcome to Daniel's Computer Quiz! \n")

#ask the user if they want to play and stores there response in var 'playing'
playing = input("Do you want to play? ")

#If they type anyting other than 'yes' the program will quit
#Using playing.lower() function, it converts all the letters in the text to lowercase
#no matter what it is. This will eliviate the problem of users typing 'yes' with various 
#cases and thus not being able to play the game.
if playing.lower() != "yes":
    quit()

print("\nOkay! Lets Play :)")
score = 0 

#question 1 response stored in 'answer' and checked if it is correct using 
#the following 'if' statement
answer = input("\n1. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 2 response stored in 'answer' and checked if it is correct using 
#the following 'if' statement
answer = input("\n2. What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 3 response stored in 'answer' and checked if it is correct using 
#the following 'if' statement
answer = input("\n3. What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")    
    score += 1
else:
    print("Incorrect!")

#question 4 response stored in 'answer' and checked if it is correct using 
#the following 'if' statement
answer = input("\n4. What does PS stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#question 5 response stored in 'answer' and checked if it is correct using 
#the following 'if' statement
answer = input("\n5. What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Note that for all the question's answers are store in the var 'answer'

print("\nYou got " + str(score) + " questions correct!")
print("\nYou got " + str((score/5) *100) + "%")#calculating and getting the percentage of correct questions 
#str(score) converts the integer variable 'score' to a string

#END.