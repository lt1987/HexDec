#!/usr/bin/python3
import os

###############################################################################
#Author:            Louvie Tucker
#Version:           1.2
#Last Modified:     11.30.2018
#
#Description:
# This program reads in either hex or ascii values and convert it to the other.
# The program consists of a main loop with four options: read from file, read 
# from console, change mode, and quit program.
#
# All hex values read in must be an even number length string. For example, 
# "0x340x3E" is valid but "0x34 0x3E" is not. Currently there are no restrictions
# for ascii string inputs.
###############################################################################
## Variable Declarations
###############################################################################

#Map of hex-ascii characters
asciiMap = {'00':'[NUL]', '01':'[SOH]', '02':'[STX]', '03':'[ETX]', '04':'[EOT]', '05':'[ENQ]', '06':'[ACK]', '07':'[BEL]',
'08':'[BS]', '09':'[HT]', '0A':'[LF]', '0B':'[VT]', '0C':'[FF]', '0D':'[CR]', '0E':'[SO]', '0F':'[SI]','10':'[DLE]', '11':'[DC1]', '12':'[DC2]', '13':'[DC3]', '14':'[DC4]', '15':'[NAK]', '16':'[SYN]', '17':'[ETB]',
'18':'[CAN]', '19':'[EM]', '1A':'[SUB]', '1B':'[ESC]', '1C':'[FS]', '1D':'[GS]', '1E':'[RS]', '1F':'[US]', '20':' ', '21':'!', '22':'"', '23':'#', '24':'$', '25':'%', '26':'&', '27':"'",
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

#Map of ascii-hex characters
hexMap = {' ':'20', '!':'21', '"':'22', '#':'23', '$':'24', '%':'25', '&':'26', "'":'27', '(':'28', ')':'29', '*':'2A', '+':'2B', ',':'2C', '-':'2D', '.':'2E', '/':'2F', '0':'30', '1':'31', '2':'32', '3':'33', '4':'34', '5':'35', '6':'36', '7':'37', '8':'38', '9':'39', ':':'3A', ';':'3B', '<':'3C', '=':'3D', '>':'3E', '?':'3F', '@':'40', 'A':'41', 'B':'42', 'C':'43', 'D':'44', 'E':'45', 'F':'46', 'G':'47', 'H':'48', 'I':'49', 'J':'4A', 'K':'4B', 'L':'4C', 'M':'4D', 'N':'4E', 'O':'4F', 'P':'50', 'Q':'51', 'R':'52', 'S':'53', 'T':'54', 'U':'55', 'V':'56', 'W':'57', 'X':'58', 'Y':'59', 'Z':'5A', '[':'5B', '\\':'5C', ']':'5D', '^':'5E', '_':'5F', '`':'60', 'a':'61', 'b':'62', 'c':'63', 'd':'64', 'e':'65', 'f':'66', 'g':'67', 'h':'68', 'i':'69', 'j':'6A', 'k':'6B', 'l':'6C', 'm':'6D', 'n':'6E', 'o':'6F', 'p':'70', 'q':'71', 'r':'72', 's':'73', 't':'74', 'u':'75', 'v':'76', 'w':'77', 'x':'78', 'y':'79', 'z':'7A', '{':'7B', '|':'7C', '}':'7D', '~':'7E'}


inFile = ''     #File to read text from
outFile = ''    #File to write to
inStr = ''      #Text string from file or console
hexStr = ''     #String for hex decoding
ans = ''        #Main loop input

mainLoop = True 	#The program.
mode = True             #Control coversion direction: T (h->a) || F (a ->h)

###############################################################################
##Functions
###############################################################################
#/////////////////////////////////////////////////////////////////////////////#

def writeResult(f, s):      #Write result to file
    saveLoop = True             #Figure out how to save
    output = ''                 #Output file
    switch = 'w'                #Determine how to write to file. Default is simply "write".

    #Check if the file exists or not. If it doesn't, simply create and write to file
    #Else, decide if the results will overwrite, append or be written to a new file
    while saveLoop == True:
        if os.path.isfile(f) == True:
            a = input('This file already exists!\nDo you want to overwrite, append, create a new file, or quit without saving? (O/A/C/Q)\n-> ')
            if a.upper() == 'O':
                switch = 'w'
                saveLoop = False
            elif a.upper() == 'A':
                switch = 'a'
                saveLoop = False
            elif a.upper() == 'C':
                f = input('Please enter a new filename.\n-> ')
            elif a.upper() == 'Q':
                saveLoop = False
                return
            else:
                print('Invalid input!')

        else:
            saveLoop = False

    output = open(f, switch)    #Open up file for manipulation
    output.write(s)             #Write to file
    output.close()              #Close the filestream
#/////////////////////////////////////////////////////////////////////////////#

def isHex(h1):      #Check if a character is a hex value
    if h1 >= '0' and h1 <= '9':                     #0-9
        return True
    elif h1.upper() >= 'A' and h1.upper() <= 'F':   #a-f && A-F
        return True
    else:
        return False
#/////////////////////////////////////////////////////////////////////////////#

def checkUp(a1, a2):   #Make sure letter values are upper case (Hex->ASCII fx)
    if a1 >= 'a' and a1 <= 'f':     #Convert a1 for mapping
        a1 = a1.upper()
    if a2 >= 'a' and a2 <= 'f':     #Convert a2 for mapping
        a2 = a2.upper()

    return a1 + a2
#/////////////////////////////////////////////////////////////////////////////# 

def inParse(i):         #Take input and parse through it to build the hex string (Hex->ASCII fx)
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

def decode(s, m):       #Convert string into ascii or hex based on the program mode 
    c = 0               #count var
    o = ''              #output string
    w = ''              #Answer for write to file           
    output = ''         #Output file name
    le = len(s) %2      #Find if the hex string length is even or odd
    
    if m == True:   #Hex -> ASCII. Do not convert if hex string is odd length
        #Even
        if le == 0:         
            while c < len(s):
                if(s[c]) >= '0' and s[c] < '8':      #Make sure first character is valid for mapping
                    o = o + asciiMap[s[c:c+2]]
                else:
                    print("This code has no mapping: " + s[c:c+2] )     #The first character is invalid for mapping
                    o = o + '(?)'
 
                c = c + 2

            print('Your hex input was [ ' + s + ' ].\nThe output is [ ' + o + ' ].\n')      #Print the result
        
        #Odd
        else:
            print('This hex string is not an even number length.\nInput was [ '+ s + ' ]')
            print('The input length is ' + str(len(s)) + ' characters long.')


    else:       #ASCII -> HEX
        while c < len(s):                               #Create output string
            if s[c] != '\n':                            #Make sure the current character isn't a new line.
                o = o + "0x" + hexMap[s[c]] + " "       
            c = c + 1

        print('Your ascii input was [ ' + s + ' ].\nThe output is [ ' + o + ' ].\n')        #Print the result
 

    w = input('Want to save results to a file? (Y/N)\n-> ')     #Prompt to save file
    if w.upper() == 'Y':
        output = input('Where do you want to save?\n-> ')       #Filepath/name
        writeResult(output, o+'\n')                             #Write out to file

###############################################################################
#Start Of The Program. 
#Ask if the hex value will come from a file or from user input.
###############################################################################

#Print Title
print("\n\n")
print("#############################################################################################################################\n")
print("\t\tHHHHHH      HHHHHH      EEEEEEEEEEEEEEEEEE      XXXXXX       XXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEEEEEEEEEEEEEE       XXXXXX     XXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEE                     XXXXXX XXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEE                      XXXXXXXXXXX")
print("\t\tHHHHHHHHHHHHHHHHHH      EEEEEEEEEEEE                  XXXXXXX")
print("\t\tHHHHHHHHHHHHHHHHHH      EEEEEEEEEEEE                  XXXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEE                      XXXXXXXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEE                     XXXXXX XXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEEEEEEEEEEEEEE       XXXXXX     XXXXXX")
print("\t\tHHHHHH      HHHHHH      EEEEEEEEEEEEEEEEEE      XXXXXX       XXXXXX")
print("\n\n")
print("\t\t\t\tDDDDDDDDDDDDDD          EEEEEEEEEEEEEEEEEE         CCCCCCCCCCCCC")
print("\t\t\t\tDDDDDDDDDDDDDDD         EEEEEEEEEEEEEEEEEE        CCCCCCCCCCCCCCC")
print("\t\t\t\tDDDD        DDDD        EEEEEE                   CCCCCC       CCCC")
print("\t\t\t\tDDDD         DDDD       EEEEEE                  CCCCCC          CC")
print("\t\t\t\tDDDD         DDDD       EEEEEEEEEEEE            CCCCCC")
print("\t\t\t\tDDDD         DDDD       EEEEEEEEEEEE            CCCCCC")
print("\t\t\t\tDDDD         DDDD       EEEEEE                  CCCCCC          CC")
print("\t\t\t\tDDDD        DDDD        EEEEEE                   CCCCCC       CCCC")
print("\t\t\t\tDDDDDDDDDDDDDDD         EEEEEEEEEEEEEEEEEE        CCCCCCCCCCCCCCC")
print("\t\t\t\tDDDDDDDDDDDDDD          EEEEEEEEEEEEEEEEEE         CCCCCCCCCCCCC\n")
print("#############################################################################################################################\n\n")

print('Welcome to HexDec!!!\n\nThis program takes in a hex value and prints out the ASCII equivalent and vice versa. For accurate results, each hex value should be either 2 or 4 characters long. For example: 0x39 or 39. If there is no mapping "(?)" will be displayed. Avoid using newlines (ENTER key) if using a text file to input your values.')

while mainLoop == True:
    #Reset string variables
    hexStr = ''
    inStr = ''
    ans = ''

    
    #print('Press "F" to read from a file. Press "S" to read from stdin. Press "M" to change mode. Press "Q" to quit this program.\n')
    ans = input('Press "F" to read from a file. Press "S" to read from stdin. Press "M" to change mode. Press "Q" to quit this program.\n-> ')
 
    #Read from file
    if ans.lower() == 'f':
        inFile = input('What file do you want to read?\n-> ')
        
        if os.path.isfile(inFile) == True:  #Make sure the file exist
            f = open(inFile)

            while ans != '':                #Read one byte at a time
                ans = f.read(1)
                inStr = inStr + ans         #Create the string used to analyze for hex codes.
           
            f.close()                       #close the file            
            if mode == True:
                hexStr = inParse(inStr)         #Create hex string for decoding
                decode(hexStr, mode)           #Find ASCII value
            else:
                decode(inStr, mode)

        else:                               #File does not exist
            print('Not a valid file. Check your filepath and try again.\n')

    #Read from Console
    elif ans.lower() == 's':
        #Retrieve Hex Value or end code
        if mode == True:
            inStr = input('Enter a HEX value and I will give you a character. (EX:7A)\n-> ')
            hexStr = inParse(inStr)             #Create hex string for decoding
            decode(hexStr, mode)                      #Find ASCII value

        else:
            inStr = input('Enter ASCII charaters and I wil give you the HEX values.\n-> ')
            decode(inStr, mode)

    #Switch mode
    elif ans.lower() == 'm':
        if mode == True:
            mode = False
            print('MODE: ASCII -> HEX\n')
        else:
            mode = True
            print('MODE: HEX -> ASCII\n')

    #Quit program
    elif ans.lower() == 'q':
        mainLoop = False
        print('Thanks for using HexDec! Come on back now ya hear?\n')
###############################################################################
