
import random

guesses_made = 0

answer = raw_input('Hi Darling! Do you want to play a game? Y/N \n')

if answer == 'Y' or answer == 'y':
	number = random.randint(1, 10)

	print 'Well, I am thinking of a number between 1 and 10.'

	while guesses_made < 6:

	    guess = int(raw_input('Take a guess: '))

	    guesses_made += 1

	    if guess < number:
	        print 'Your guess is too low.'

	    if guess > number:
	        print 'Your guess is too high.'

	    if guess == number:
	        break

	if guess == number:
	    print 'Good job, honey! You guessed my number in {0} guesses!'.format(guesses_made)
	else:
	    print 'Nope. The number I was thinking of was {0}'.format(number)

	print 'I want to show you I care about the things you care, like python. But most of all I care about you. I truly love u :) \n'


	print('    ### ###\n  ###########\n  ##M#&#J####      Happy\n   #########       Valentine\'s!\n    #######\n     #####\n      ###\n       #\n')
	name = raw_input('Now Kiss me You Fool')
else:
	print(':(')