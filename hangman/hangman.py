import random

def hangman():
   word_list = ["python", "java", "ruby", "javascript", "csharp"]
   random_word = random.choice(word_list)
   guessed_letters = []
   attempts = 10

   print("Let's play Hangman!")
   print("_ " * len(random_word))
   print("\n")

   while attempts > 0:
       guess = input("Please guess a letter or type 'quit' to exit: ").lower()

       if guess == "quit":
           break

       if len(guess) != 1:
           print("Please input only one letter at a time.")
           print("\n")
           continue

       if guess in guessed_letters:
           print("You already guessed this letter.")
           print("\n")
           continue

       guessed_letters.append(guess)

       if guess in random_word:
           print("Correct guess!")
           print("_ " * random_word.count(guess))
           print("\n")
       else:
           print("Incorrect guess.")
           attempts -= 1
           print("_ " * len(random_word))
           print("\n")

       if "_" not in "_ " * len(random_word):
           print("Congratulations, you won! The word was " + random_word + ".")
           break

   if attempts == 0:
       print("You lost! The word was " + random_word + ".")

hangman()