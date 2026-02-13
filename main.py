import random

score = 0
ch = None
def menu():
    print("Choose an interval you want to play:\n"
          "1. [0,5] (1 point)\n"
          "2. [0,10] (2 points)\n"
          "3. [0,15] (3 points)\n"
          "4. [0,25] (4 points)\n"
          "5. EXIT")
def game(a, b):
    global score
    answer = random.randint(a,b)
    guess = int(input("Enter your guess int the interval"+ str(a) + "-" + str(b) + ": "))
    if guess == answer:
        score += ch
        print("TRUE! Your score is now ", score)
    else:
        score -= 1
        print("Incorrect:( Answer is ", answer, "\n"
              "Your score is now ", score)

if __name__ == '__main__':
 print("GUESS THE NUMBER\n"
       "Correct guesses get you some points, incorrect guesses decreases 1 point")
 flag = True
 while flag:
     menu()
     ch = int(input())
     if ch not in [1,2,3,4,5]:
      print("Please enter valid option")
      continue
     elif ch == 5:
         print("You completed the game with a score ", score)
         break
     elif ch == 1: game(0,5)
     elif ch == 2: game(0,10)
     elif ch == 3: game(0,15)
     elif ch == 4: game(0,25)



