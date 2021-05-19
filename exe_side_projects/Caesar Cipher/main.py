from art import logo
import time
import os

def screen_clear():
    os.system('cls')

symbols_data = ['!','?','@','#','$','%','^','&','*','(',')','-','=','_','+','[',"{","}",']','"',"'",'/',':',';','>','<','.',',','|','`','~']
numbers_data = ['1','2','3','4','5','6','7','8','9','0']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
get_direction = ''
get_text = ''
get_shift = ''


#BUG: Make the user input if they want to repeat the program or not
#BUG: Make the alphabet repeat if it goes over the shift number

def caesar(get_text, get_shift, get_direction):
  screen_clear()
  print(logo)
  get_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  get_text = input("Type your message:\n").lower()
  get_text = list(get_text)
  get_shift = int(input("Type the shift number:\n"))
  cipher_text = ''

  isSpace = None
  isSymbol = None
  isDone = False
  
  #purpose: to make it shift for any number

  get_shift = get_shift % 24

  # what i could have done better is that instead of checking
  # for symbols or space, i could have just checked if the
  # text we are checking is a text or not, if not then just
  # print it out and not do the indexes part.  

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
        indexes = alphabet.index(get_text[i])
        indexes += get_shift

      if get_text[i] in alphabet:
        cipher_text += ''.join(alphabet[indexes])
    print(f"The encoded text is {cipher_text}")
    isDone = True
    time.sleep(1)
    #END

    #START
  elif get_direction == "decode":
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
        indexes = alphabet.index(get_text[i])
        indexes -= get_shift

      if get_text[i] in alphabet:
        cipher_text += ''.join(alphabet[indexes])
    print(f"The decoded text is {cipher_text}")
    isDone = True
    time.sleep(1)
  else:
    print("Invalid Input")
    #END

  def restartProgram():
    restartCipher = input("\nWould you like to restart the cipher program?\nType 'yes' if you would like to restart\nType 'no' if you want to exit\n").lower()
    if restartCipher == 'yes':
      time.sleep(1)
      screen_clear()
      caesar(get_text, get_shift, get_direction)
    elif restartCipher == 'no':
      time.sleep(1.5)
      screen_clear()
      exit()

  if isDone == True:
    restartProgram()

caesar(get_text, get_shift, get_direction)
