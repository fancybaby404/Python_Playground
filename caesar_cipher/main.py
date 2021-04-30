from art import logo
import time
from itertools import repeat
symbols_data = ['!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',"{","}",']','"',"'",'/',':',';','>','<','.',',','|','`','~']
numbers_data = ['1','2','3','4','5','6','7','8','9','0']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
text = list(text)
shift = int(input("Type the shift number:\n"))
cipher_text = ''

#BUG TO FIX:
#BUG: Make the user input if they want to repeat the program or not
#BUG: Make the alphabet repeat if it goes over the shift number

def caesar(get_text, get_shift, get_direction):
  global cipher_text
  isSpace = None
  isSymbol = None
  isDone = False
  new_alphabet = ''
  if get_shift > len(alphabet):
    alphabet += repeat(new_alphabet, shift)
    #new_alphabet = ([alphabet] * shift)
    #new_alphabet.extend(alphabet * shift)
    

  #START  
  if get_direction == "encode":
    for i in range(0, len(get_text)): 
      #check if space is in the text[i]
      if ' ' in get_text[i]:
        cipher_text += ' '
        isSpace = True
      elif ' ' not in get_text[i]:
          isSpace = False
      #check if symbol is in the text[i]
      for s in range(0,len(symbols_data)):
        if symbols_data[s] in get_text[i]:
          cipher_text += get_text[i]
          isSymbol = True
          break
        elif symbols_data[s] not in get_text[i]:
          isSymbol = False
      #if no space or no symbol then:
      if isSpace == False and isSymbol == False:
        indexes = new_alphabet.index(get_text[i])
        indexes += get_shift

      if get_text[i] in new_alphabet:
        cipher_text += ''.join(new_alphabet[indexes])
    print(f"The encoded text is {cipher_text}")
    isDone = True
    time.sleep(.5)
    #END

    #START
  elif get_direction == "decode":
    for i in range(0, len(get_text)): 
      if ' ' in get_text[i]:
        cipher_text += ' '
        isSpace = True
      elif ' ' not in get_text[i]:
          isSpace = False
          break
      if not isSpace:
        indexes = new_alphabet.index(get_text[i])
        indexes -= get_shift

      if get_text[i] in new_alphabet:
        cipher_text += ''.join(new_alphabet[indexes])
    print(f"The decoded text is {cipher_text}")
    time.sleep(.5)
    isDone = True
  else:
    print("Invalid Input")
    #END

  def restartProgram():
    restartCipher = input("Would you like to restart the cipher program?\nType 'yes' if you would like to restart\nType 'no' if you want to exit\n").lower()
    if restartCipher == 'yes':
      caesar(get_text = text, get_shift = shift, get_direction = direction)
    elif restartCipher == 'no':
      exit()

  if isDone == True:
    restartProgram()

caesar(get_text = text,get_shift = shift,get_direction = direction)