print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

#.lower/.upper to change the sentence to upper case and lower case
if playing.lower() != "yes":

    quit()

print("OKAZZZ")

score = 0 

answer = input("what does CPU stand for? ")  
if answer.lower() == "central processing unit":
    print('correct')
    score += 1
else:
    print("incorrect")

answer = input("what does GUI stand for? ")  
if answer.lower() == "graphic user interface":
    print('correct')
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ")  
if answer.lower() == "random access memory":
    print('correct')
    score += 1
else:
    print("incorrect")

answer = input("what does ROM stand for? ")  
if answer.lower() == "read only memory":
    print('correct')
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)* 100) + " %")