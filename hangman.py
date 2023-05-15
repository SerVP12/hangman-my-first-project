import random
import collections
import time
print("lets play hangman!")

print(
'choose a category...',
'\n1:sports',
'\n2:continents'
'\n3:country'
'\n4:city'
)
while True:
	try:
		choice = int(input())
		if choice == 1:
			sports = ['basketball', 'football', 'tennis', 'hockey', 'soccer']
			word = random.choice(sports)
			time.sleep(1)
			print("\nI am thinking of a sport..." , " It has" , str(len(word)) , "letters")
			hangman_word = list(word)
			#print(hangman_word)
	
		elif choice == 2:
			continents = ['asia', 'north america', 'south america', 'africa', 'australia', 'antartica', 'europe']
			word = random.choice(continents)
			time.sleep(1)
			print("\nI am thinking of a continent..." , " It has" , str(len(word)) , "letters")
			hangman_word = list(word)
			#print(hangman_word)


		elif choice == 3:
			country = ['philippines','japan', 'united states', 'united kingdom', 'denmark', 'australia']
			word = random.choice(country)
			time.sleep(1)
			print("\nI am thinking of a country..." , " It has" , str(len(word)) , "letters")
			hangman_word = list(word)
			#print(hangman_word)
		
		elif choice == 4:
			city = ['tokyo', 'manila','beijing']
			time.sleep(1)
			word = random.choice(city)
			print("\nI am thinking of a city..." , " It has" , str(len(word)) , "letters")
			hangman_word = list(word)
			#print(hangman_word)

		#letters guessed that are in the chosen word
		guessletters = []

		#letters of hangman
		hangman_progress = ['n','a','m','g','n','a','h']
		
		#transfter hangman letters one by one 
		hangman = []	

		underscore = 1

		while True:
			
			guess_a_letter = input("\nguess a letter: ")
			#w = guess_a_letter.isalpha()
			#if w == False:
			if guess_a_letter.isalpha() == False:
				print("not a letter")
				continue
			
			#converts user input to lowercase for any upper case input
			guess_a_letter = guess_a_letter.lower()
			time.sleep(1)
			
			#checks to see if input is more than one letter
			if len(guess_a_letter) > 1:
				print("type only one letter. try again ")
	
			#checks to see if input matches the letters inside the word and prints your progress
			if guess_a_letter in hangman_word:
				guessletters.append(guess_a_letter)
				#print(guessletters)
				combine = ''.join(guessletters)
				print("your word so far..." , combine)
		
			#number of inputs exceed the total letters in word. Deletes letter of choice
			if len(guessletters) > len(hangman_word):
				print(guessletters)
				remove_letter = int(input("first letter value starts at 0.\nYou have exceed the letter count. Which letter do you want to remove? "))
				#guessletters.remove(remove_letter)
				del guessletters[remove_letter]
	
			#initial input is only one letter, and if input letter is not in the chosen word. hangman will be spelt incremently if wrong
			elif guess_a_letter not in hangman_word and len(guess_a_letter) == 1:
				letter = hangman_progress.pop()
				hangman.append(letter)
				x = ''.join(hangman)
				print("\n"+x)
				print("_" * underscore)
				underscore += 1
		
			#once hangman is spelt, program breaks
				if x == 'hangman':
					print("you lose ", "the word was: ", word)
					break
			
			#check to see if letters guessed is the same as the word
			if collections.Counter(guessletters) == collections.Counter(hangman_word):
				print('\ngreat job! your word was', word) 
				break
	
		#option to continue or exit program
		again = input("would you like to try again? ")
		if again == 'n' or again == '':
			print("\nthank you!")
			break
		elif again == 'y':
			continue

	#tells user to choose only the choices
	except ValueError:
		print("enter a number choice")
		continue


