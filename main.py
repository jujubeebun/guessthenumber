import random
counter=0

number=random.randint(0,100)

answer=int(input("my number is between 0 and 100, try to guess it! "))

while answer!=number:
  if answer>number:
    counter=counter+1
    print("smaller!")
    answer=int(input("guess again! "))

  if answer<number:
    counter=counter+1
    print("bigger!")
    answer=int(input("guess again! "))

if answer==number:
  print("correct! good job. you guessed in", counter, "tries.")

if counter<5:
  print("wow! that's less than 5 tries!")