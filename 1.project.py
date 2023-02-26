print("welcome to computer quiz!")
answer = input("Do you want to play quiz? ")
if answer.lower() != "yes":
    quit()

print("lets play")
score = 0
answer = input("what dose CPU stand for? ")  #1
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("what does GPU stand for? ")   #2
if answer.lower() == "graphics processing unit":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what does ALU stand for ")  #3
if answer.lower() == "arithmatic and logic unit":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what does RAM stand for ")  #4
if answer.lower() == "random access memory":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what does O.S stand for ") #5
if answer.lower() == "operating system":
    print("correct")
    score +=1
else:
    print("Incorrect")

print("You got"+ str(score)+"questions correct")
print("You got"+str((score/5)*100)+"%")