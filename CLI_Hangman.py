#!/usr/bin/python

'''
hangman.py
Initial start August 03, 2017

Author: Emil Davis
Current revision: 0.9
Current Date: August 31, 2017


Core functionality is implimented.
Gameplay works as intended.
Known Bugs:
    1.) FIXED! If an incorrect guess is made and a letter is revealed on game board, the user may see a 'You already guessed' message if they typed in a previously revealed letter. Fix: reset alreadyGuessed when displaying message
    2.) Entering non-alphabet charactors is not showing the message to that affect.
    3.) No way out for the user if they wish to stop playing in the middle of a game.
    4.)

'''

#we will need the random mondule to generate a random integer to pick a word from a read file at random
import random

#open file of list of words and import to a list
#This code assumes a file with one word per line sepperated by the newline (\n) character)

#declare variable to store data from read file
hangmanWords=[]
with open("words.txt","r") as words:
    for line in words:
        hangmanWords.append(line)

#strip newline '\n' charactor off each line by stripping the last charactor in each string
strippedHangmanWords=[]
for string in hangmanWords:
    strippedHangmanWords.append(string[0:-1])
    #TODO: add code to save the last charactor in file. Currently it will strip the last charator off the file even if it is not \n


#psudorandom number generator between 1 and the length of list of words
randWordIndex = random.randint(1,len(strippedHangmanWords))

#use psudorandom number as an index to grab a word
testWord=strippedHangmanWords[randWordIndex]

#convert the word to uppercase
testWord=testWord.upper()






#declare integer variable to store number of guesses remaining until game over
guessesRemaining = 10
#declare list variable to store the history of the letters the user has guessed
guessedLetters = []
#declare string variable to store the current letter the user has input
letterInput=''
#declare boolean variable to store weather user had already entered that letter
alreadyGuessed=False

#build the initial blank gameBoard
#declare list variable to store the state of the word / game board
#it simply loops through the word and adds an underscore (_) for each letter of the word
gameBoard=[]
for char in testWord:
    gameBoard+='_'

#declare list variable to store the alphabet upper and lower case. This will be used for imput validation later.
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#define function to print game board
def prntGameBoard(gameBoard):
    #clear screen first using ANSI VT100 clear screen code
    #Note: This will only work in a Linux/Unix terminal or emulator
    print("\033[H\033[J")
    #print gameBoard - this works similar to the code earlier
    #code to print out an ascii art version of a person getting hung
    if guessesRemaining == 0:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        /|\       |')
        print('|         |        |')
        print('|        / \       |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 1:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        /|\       |')
        print('|         |        |')
        print('|        /         |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 2:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        /|\       |')
        print('|         |        |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 3:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        /|\       |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 4:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        / \       |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 5:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|        /         |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 6:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|         |        |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 7:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|         0        |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 8:
        print('====================')
        print('|         +--------|')
        print('|         |        |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 9:
        print('====================')
        print('|         +--------|')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    if guessesRemaining == 10:
        print('====================')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|                  |')
        print('|__________________|')
    print()
    print()
    for item in gameBoard:
        print(item+' ',end="")
    print()

#call function to print the game board
prntGameBoard(gameBoard)

#main game code. runs until victory or the user has zero guesses remaining
while(guessesRemaining>0):
    print(guessesRemaining,'incorrect guesses remaining')
    #prompt user for a letter
    letterInput = input("Enter a letter or type 'quit' to exit: ")
    #check if input is a valid letter of the alphabet, if not prompt the user
    if letterInput == 'quit':
        print("\033[H\033[J")
        quit()
    if letterInput in alphabet:
        #if letter was lowercase, change to uppercase
        if letterInput.islower():
            letterInput=letterInput.upper()
        #check if the letter is in the game word
        if not letterInput in testWord:
            #add the incorrect guessed letter to the list and decriment number of guesses
            if not letterInput in guessedLetters:
                guessedLetters.append(letterInput)
                alreadyGuessed=False
                guessesRemaining-=1
            else:
                alreadyGuessed=True
        #declare integer variable iters. Used in a loop to update the game board with the correct index value
        iters=0
        #This loops through the game word checking if the letter the user entered is that chracter. If they match, replace the underscore (_) with the letter.
        for char in testWord:
            if char == letterInput:
                gameBoard[iters]=testWord[iters]
                iters+=1
            else:
                iters+=1
    else:
        print('Enter a valid letter please!')




    #print game board again now that it has been updated        
    prntGameBoard(gameBoard)

    #print letters the user already incorrectly guessed
    print('Incorrect letters you guessed: ', guessedLetters)


    #check if the letter entered had already been guessed by the user and display a messge
    #reset to False
    if alreadyGuessed:
        print('You already guessed', letterInput, '- no penalty')
        alreadyGuessed=False

    #victory condition: no underscores (_) left on the game board
    if not '_' in gameBoard:
        print('CONGRATULATIONS! You Won!')
        quit()

    #defeat condition: user ran out of guesses
    if guessesRemaining==0:
        print('Sorry you lost; out of guesses!')
        print('The word was: ', testWord)
        quit()

