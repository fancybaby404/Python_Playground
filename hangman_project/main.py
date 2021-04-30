
symbols_data = ['!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',"{","}",']','"',"'",'/',':',';','>','<','.',',','|','`','~']
numbers_data = ['1','2','3','4','5','6','7','8','9','0']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
text = list(text)
shift = int(input("Type the shift number:\n"))
cipher_text = ''



def caesar(text_input,shift_input,direction_input):
  global cipher_text
  isSpace = None
  isSymbol = None
  
  if shift > len(alphabet):
    alphabet.append(alphabet)
    
  if direction == "encode":
    for i in range(0, len(text)): 
      #check if space is in the text[i]
      if ' ' in text[i]:
        cipher_text += ' '
        isSpace = True
      elif ' ' not in text[i]:
          isSpace = False
      #check if symbol is in the text[i]
      for s in range(0,len(symbols_data)):
        if symbols_data[s] in text[i]:
          cipher_text += text[i]
          isSymbol = True
          break
        elif symbols_data[s] not in text[i]:
          isSymbol = False
      #if no space or no symbol then:
      if isSpace == False and isSymbol == False:
        indexes = alphabet.index(text[i])
        indexes += shift

      if text[i] in alphabet:
        cipher_text += ''.join(alphabet[indexes])
    print(f"The encoded text is {cipher_text}")
    #restartProgram()
    

  elif direction == "decode":
    for i in range(0, len(text)): 
      if ' ' in text[i]:
        cipher_text += ' '
        isSpace = True
      elif ' ' not in text[i]:
          isSpace = False
          break
      if not isSpace:
        indexes = alphabet.index(text[i])
        indexes -= shift

      if text[i] in alphabet:
        cipher_text += ''.join(alphabet[indexes])
    print(f"The decoded text is {cipher_text}")
    #restartProgram()
  else:
    print("Invalid Input")