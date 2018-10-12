#!/usr/bin/python3
import os

###############################################################################
#Author:            Louvie Tucker
#Version:           1.1
#Last Modified:     10.11.2018
#
#Description:
# This program reads in hex values to output its ASCII equivalent. The program
# consists of a main loop with three option: read from file, read from console,
# and quit program. As of now, ASCII values 20h - 7Fh are supported. In 
# addition, input must be an even number of characters with no new lines else 
# it may not calculate an appropriate value.
#
###############################################################################
## Variable Declarations
###############################################################################

#Map of the ascii characters
asciiMap = {'20':' ', '21':'!', '22':'"', '23':'#', '24':'$', '25':'%', '26':'&', '27':"'",
'28':'(', '29':')', '2A':'*', '2B':'+', '2C':',', '2D':'-', '2E':'.', '2F':'/', 
'30':'0', '31':'1', '32':'2', '33':'3', '34':'4', '35':'5', '36':'6', '37':'7', '38':'8', '39':'9', '3A':':', '3B':';', '3C':'<', '3D':'=', '3E':'>', '3F':'?',
'40':'@', '41':'A', '42':'B', '43':'C', '44':'D', '45':'E', '46':'F', '47':'G', '48':'H',
	'49':'I', '4A':'J','4B':'K', '4C':'L', '4D':'M', '4E':'N', '4F':'O', '50':'P', 
	'51':'Q', '52':'R', '53':'S', '54':'T', '55':'U', '56':'V', '57':'W', '58':'X', '59':'Y',
	'5A':'Z', '5B':'[', '5C':'\\', '5D':']', '5E':'^', '5F':'_', '60':'`', 
'61':'a', '62':'b', '63':'c', '64':'d', '65':'e', '66':'f', '67':'g', '68':'h',
	'69':'i', '6A':'j','6B':'k', '6C':'l', '6D':'m', '6E':'n', '6F':'o', '70':'p', 
	'71':'q', '72':'r', '73':'s', '74':'t', '75':'u', '76':'v', '77':'w', '78':'x', '79':'y',
        '7A':'z', '7B':'{', '7C':'|', '7D':'}', '7E':'~', '7F':'DEL'}


inFile = ''     #File to read text from
inStr = ''      #Text string from file or console
hexStr = ''     #String for hex decoding
ans = ''        #Main loop input

mainLoop = True 	#The program.

###############################################################################
##Functions
###############################################################################
#/////////////////////////////////////////////////////////////////////////////#

def isHex(h1):      #Check if a character is a hex value
    if h1 >= '0' and h1 <= '9':                     #0-9
        return True
    elif h1.upper() >= 'A' and h1.upper() <= 'F':   #a-f && A-F
        return True
    else:
        return False
#/////////////////////////////////////////////////////////////////////////////#

def checkUp(a1, a2):   #Make sure letter values are upper case
    if a1 >= 'a' and a1 <= 'f':     #Convert a1 for mapping
        a1 = a1.upper()
    if a2 >= 'a' and a2 <= 'f':     #Convert a2 for mapping
        a2 = a2.upper()

    return a1 + a2
#/////////////////////////////////////////////////////////////////////////////# 

def inParse(i):         #Take input and parse through it to build the hex string
    c = 0                   #Count var
    h = ''                  #Hex string to return
    while c < len(i):       #Build the hex string
        if (c+1) < len(i):  #Check for NUL
            #Check two characters at the same time.
            if isHex(i[c]) == True and isHex(i[c+1]) == True:
                h = h + checkUp(i[c],i[c+1])
        c = c + 2
    return h
#/////////////////////////////////////////////////////////////////////////////#

def decode(h):          #Convert hex values to ASCII. Does not run if the value is an odd number length
    c = 0               #count var
    o = ''              #output string
    le = len(h) %2      #Find if the hex string length is even or odd
    
    #Even
    if le == 0:         
        while c < len(h):
            if(h[c]) > '1' and h[c] < '8':      #Make sure first character is valid for mapping
                o = o + asciiMap[h[c:c+2]]
            else:
                print("This code has no mapping: " + h[c:c+2] )     #The first character is invalid for mapping
                o = o + '(?)'
 
            c = c + 2

        print('Your hex input was [ ' + h + ' ].\nThe output is [ ' + o + ' ].\n')      #Print the result
    
    #Odd
    else:
        print('This hex string is not an even number length.\nInput was [ '+ h + ' ]')
        print('The input length is ' + str(len(h)) + ' characters long.')


###############################################################################
#Start Of The Program. 
#Ask if the hex value will come from a file or from user input.
###############################################################################

print('Welcome to HexDec!!!\nThis program takes in a hex value and prints out the ASCII equivalent.The first 32 ASCII values are not included in this program. For accurate results, each hex value should be either 2 or 4 characters long. For example: 0x39 or 39. Avoid using newlines (ENTER key) if using a text file to input your values.')

while mainLoop == True:
    #Reset variables
    hexStr = ''
    inStr = ''
    ans = ''

    print('Press "F" to read from a file. Press "S" to read from stdin. Press "Q" to quit this program.\n')
    ans = input('Command: ')
 
    #Read from file
    if ans.lower() == 'f':
        inFile = input("What file do you want to read: ")
        
        if os.path.isfile(inFile) == True:  #Make sure the file exist
            f = open(inFile)

            while ans != '':                #Read one byte at a time
                ans = f.read(1)
                inStr = inStr + ans         #Create the string used to analyze for hex codes.
           
            f.close()                       #close the file            
            hexStr = inParse(inStr)         #Create hex string for decoding
            decode(hexStr)                  #Find ASCII value                  

        else:                               #File does not exist
            print("Not a valid file. Check your filepath and try again.\n")

    #Read from Console
    elif ans.lower() == 's':
        #Retrieve Hex Value or end code
        inStr = input("Enter a HEX value and I will give you a character.\n(EX:7A)")
        hexStr = inParse(inStr)             #Create hex string for decoding
        decode(hexStr)                      #Find ASCII value

    #Quit program
    elif ans.lower() == 'q':
        mainLoop = False
        print("Goodbye ;)")
###############################################################################
