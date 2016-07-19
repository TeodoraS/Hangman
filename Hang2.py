import random
import os
import sys
import subprocess as sp
from datetime import date
from datetime import datetime
import random
from lxml import html
import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.dictionary.com/wordoftheday/'

def random_date():
        #Generate a random date to a extract a word within the website
	year = random.randint(2000, date.today().year)
	month = random.randint(1, 12)
	day = random.randint(1, 28)
	ran_date = (date(year, month, day).strftime('%Y/%m/%d'))
	return ran_date

def url_get():
        #With given url extracts the class in which the word is placed
    url = 'http://www.dictionary.com/wordoftheday/'+ date + '/'
    r = requests.get(url)   
    soup = BeautifulSoup(r.content, 'lxml')
    g_data = soup.find_all('h1')
    for item in g_data:
        string = str(item)
        string = string.replace(" ","")
        return string
        print string
 
def hang_word():
        #Regex to extract the word
    word = re.search(r'<strong>(.*)</strong>', url_get())
    word = str(word.group(1))
    return word

def definition():
        #With given url extracts the class in which the def is placed
        #and uses regex to extract it
        url = 'http://www.dictionary.com/wordoftheday/'+ date + '/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        definition = soup.find_all('li', {'class':'first'})
        for item in definition:
                definition = str(item)
                definition = re.search(r'<span>(.*)</span>', definition)
                definition = definition.group(1)
                return definition
def clrscr():
        #Clears the terminal screen
	sp.call('cls', shell = True)

def design0():
	clrscr()
	print """
	WELCOME TO HANGMAN!
 _________
 |/     | 
 |           
 |                
 |                 
 |               
 |                   
 |___   
"""
	
def design1():
	print """
	
 _________
 |/     | 
 |    (._.)     
 |               
 |                 
 |               
 |                   
 |___   
"""

def design2():
		print """
		
 _________
 |/     |        
 |    (._.)          
 |      |           
 |      |         
 | 
 | 
 |___   
"""

def design3():
	print """
	
 _________
 |/     |        
 |    (._.)          
 |      |           
 |     /|         
 |  
 | 
 |___   
"""

def design4():
	print """
	
 _________
 |/     |        
 |    (._.)          
 |      |           
 |     /|\         
 |  
 | 
 |___   
"""

def design5():
	print """
	
 _________
 |/     |        
 |    (._.)       
 |      |     
 |     /|\       
 |     /           
 |
 |___   
"""

def design6():
	print """
	
 _________
 |/     |        
 |    (o_o)       
 |      |     
 |     /|\       
 |     / \          
 |
 |___   
 """

def design7():
	print """
	
 _________
 |/     |      
 |    (o_O)  Help!    
 |      |     
 |     /|\       
 |     / \          
 |
 |___   
"""

def design8():
	print """
	
 _________
 |/     |      
 |    (x_x)      
 |      |     
 |     /|\       
 |     / \          
 |
 |___   
 GAME OVER!
"""

design = {0:design0, \
		1:design1, \
		2:design2, \
		3:design3, \
		4:design4, \
		5:design5, \
		6:design6, \
		7:design7, \
		8:design8
		}

def hangman():
        guess_word = hang_word()
        guessed = '*' * len(guess_word)
        missed_guess = 0
        while (missed_guess < 8):			
                x = raw_input("The word is %s ... Take a guess\t"%guessed).lower()
                if x.isalpha() and (len(x) == 1):			
                        if x in guess_word:
                                print '\nCorrect!'
                                new_guessed = ''		
                                for index, char in enumerate(guess_word):
                                        if char == x:
                                                new_guessed += x
                                        else:
                                                new_guessed += guessed[index]
                                guessed = new_guessed			
			
                                if guessed == guess_word:
                                        print 'You have guessed the word. You win!'
                                        print '\n' + guess_word + '=' + definition()
                                        return True
                        else:
                                missed_guess += 1
                                clrscr()
                                design[missed_guess]()					
		
                else:
                        print "Type a LETTER!"
        print "You lost the game!"
        print "The word was " + guess_word + '.'
        print "Deffinition = " + definition()
 

def main():
        while True:
                design0()
                hangman()
                game_over = raw_input("\n Quit game? Y/N:\t")
                if game_over.upper() == "Y":
                        break
                else:
                        continue

date = random_date()
main()
