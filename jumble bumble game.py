
import random

words =["ironman","thor","hawkeye","wanda","vision"]
word = random.choice(words)
print(word)

jumble = " ".join(random.sample(word,len(words)))
#print(jumble)

chances = 3
print("^"*30)
print("^^^ Jumble Bumble^^^")
print("^"*30)
while chances!=0:
    print("the word is",jumble)
    guess = input("enter your guessed word: ").lower()
    if guess == word:
     print("correct guess ! !")
     print("you won !")
     break
    else:
     chances = 1
     print("Incorrect Guess !!")
     print("Remaning chances are:",chances)

else:
  print("all you chances are exhausted")
  print("you lose")
  print(" The correct word is",word)

print("thank you for playing")


   
 
 

