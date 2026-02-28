import sys
from colorama import Fore, init

init()

def cipher_start(msg, key, decrypt=False):
    #initalize empty string
    result = ''
    for char in msg:
        #check if char is alpha
        if char.isalpha():
            #determine the shift amount based.
            shift = key if not decrypt else -key
            #check if char is lowercased
            if char.islower():
                #apply cipher transfromation for lowercase
                result += chr(((ord(char) - ord('a') +  shift) % 26) + ord('a'))
            else:
                #apply cipher transfromation for uppercase
                result += chr(((ord(char) - ord('A') +  shift) % 26) + ord('A'))
        else:
            #preserve nonalpha chars as is
            result += char
    return result #return the encrypted/crypted result

#prompt user to enter text to encrypt
textToEncrypt = input(f'{Fore.GREEN}[?] Enter text/message: ')
#prompt user to specify shift length(key)
key = int(input(f'{Fore.GREEN}[?] Specify shift length: '))
#check if specified key is within valid range(0 - 25)
if key > 25 or key < 0:
    #display error msg if key is out of range
    print(f'{Fore.Green}[?] Shift length should be between 0 & 25!')
    sys.exit() #exit program if key is invalid

#encrypt the user's input using the specified key
encrpytedText = cipher_start(textToEncrypt, key)
#display the encrypted text
print(f'{Fore.GREEN}[+] {textToEncrypt} has been encrypted as {Fore.RED}{encrpytedText}')
