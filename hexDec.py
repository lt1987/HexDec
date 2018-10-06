#!/usr/bin/python3
import os

###############################################################################
#Author:            Louvie Tucker
#Version:           1.0
#Last Modified:     10.4.2018
#
#Description:
# This program is divided into three sections. The first section asks how the
# hex code will be read for decoding. The hex code can either be read in by a
# file or through console.
#
# The second section reads from console to decode. The third section reads from
# file.
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


outStr = ''     #Result
inFile = ''     #File to read hex values from if chosen
hexStr = ''     #String for hex evaluation
ans = ''        #Hold a char to determin if it goes in hexStr

mainLoop = True 	#Landing page of the program.
mainSTD = False 	#Main program for stdin
mainFile = False 	#Main program for file input
###############################################################################
#
#
#
###############################################################################
##Functions
###############################################################################
#/////////////////////////////////////////////////////////////////////////////#

def buildHex(a):
     #Check if character is a hex value
        if a >= 'a'and a <= 'f':
            a = a.upper()
            return a
        elif a >= 'A' and a <= 'F':
            return a
        elif a >= '0' and a <= '9':
            return a

        return ''
#/////////////////////////////////////////////////////////////////////////////# 

def decode(h):
    c = 0
    o = ''
    l = len(h)
    le = l % 2
    if le == 0:
        while c < len(h):
            if(h[c]) > '1' and h[c] < '8':
                o = o + asciiMap[h[c:c+2]]
            else:
                print("This code has no mapping: " + h[c:c+2] )
                o = o + '(0_o)'
 
            c = c + 2

        print('Your hex input was [ ' + h + ' ].\nThe output is [ ' + o + ' ].\n')
    else:
        print('This hex string is not an even number length.\nInput was [ '+ h + ' ]')
        print('The input lenght is ' + str(l) + 'chacters long.')
#/////////////////////////////////////////////////////////////////////////////#
###############################################################################
#
#
#
###############################################################################
#Start Of The Program. 
#Ask if the hex value will come from a file or from user input.
###############################################################################

print('Welcome to HexDec!!!\nThis program takes in a hex value and prints out the ascii equivalent.\n')

while mainLoop == True:
    print('Press "F" to read from a file. Press "S" to read from stdin. Press "Q" to quit this program.\n')

    ans = input('Command: ')
  
    if ans.lower() == 'f':
        inFile = input("What file do you want to read: ")
        if os.path.isfile(inFile)==True:
            f = open(inFile)
            while ans != '':                #Read one byte at a time
                ans = f.read(1)
                hexStr = hexStr + buildHex(ans)
       
            f.close()                       #close the file
            decode(hexStr)    
        else:
            print("Not a valid file. Check your filepath and try again.\n")


    elif ans.lower() == 's':
        #Retrieve Hex Value or end code
        ans = input("Enter a HEX value and I will give you a character.\n(EX:7A)")
        decode(ans)

    elif ans.lower() == 'q':
        mainLoop = False
###############################################################################
#
#
#
###############################################################################
## Takes a singe hex value and builds the string (STDIN LOOP)
###############################################################################

while mainSTD==True:
	#Retrieve Hex Value or end code
	ans = input("Enter a HEX value and I will give you a character.\n(EX:7A):")
	if ans.lower() =='q':
		mainSTD = False
		print("Ending Program.")
	elif len(ans) == 2:
		outStr = outStr + asciiMap[ans] 
###############################################################################


#print("Your hexing: " + hexStr)
#print("Your result: " + outStr) 
print("Goodbye ;)")
