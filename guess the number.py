x=77
count=0
while count<10:
      y=int(input("Guess the number: "))
      if y>x:
            print("Your number is greater, try again.")
      elif y<x:
            print("Your number is smaller, try again.")
      elif y==x:
            print("You have found the number")
            print(count,"guesses you took to finish")
            break
      count+=1
      print("Your current guesses left are",10-count)
      if 10-count==0:
            print("You are out of guesses, better luck next time...")
            break
      

      
