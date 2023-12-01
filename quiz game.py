print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay lets play :) ")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")
answer = input("what does CLI stand for? ")
if answer.lower() == "command line interface":
    print('correct!')
    score += 1
else:
    print("incorrect!")
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print("incorrect!")
answer = input("what does ROM stand for? ")
if answer.lower() == "read only memory":
    print('correct!')
    score += 1
else:
    print("incorrect!")
print("you got " + str(score) + "questions correct!")
print("you got " + str((score / 5) * 100) + "%.")
