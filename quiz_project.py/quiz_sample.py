print("welcome to my computer quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":
  quit()
    
print("okay let's play :)")
score = 0
  
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
  print('correct!')
  score += 1
else:
  print("NOPE, TRY AGAIN!")

answer = input("ASG stand for? ")
if answer.lower() == "auto scaling group":
  print('Good. There is a future in Tech for you!')
  score += 1
else:
  print("So... you haven't done the Udemy course!?!")

answer = input("RAM stand for? ")
if answer.lower() == "random access memory":
  print('A SIX FIGURE INCOME AWAITS YOU!')
  score += 1
else:
  print("How did you miss this ya dumbass?")

answer = input("ALB stand for? ")
if answer.lower() == "application load balancer":
  print('Correct, Your a Guru Bro!')
  score += 1
else:
  print("Walmart is hiring Bruh")
  
print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
  
  
