#RandPasswordGen
#This programm is a password generator that cretes a password based on the usser choices

import secrets
import string
import pyperclip

def password(lenght,lower, upper, digits, symbols):
  print('Generating Password...')
  pool = ''

  if lower:
    pool += string.ascii_lowercase
  if upper:
    pool += string.ascii_uppercase
  if digits:  
    pool += string.digits
  if symbols:
    pool += string.punctuation  

  if not pool:
    print('No character types selected')
    return None

  #build the password
  result = ''.join(secrets.choice(pool) for _ in range(lenght))
  return result
  
  

def yesno(prompt = 'Choose Y/N'):
  while True:
    usser_input = input(prompt).upper()
    if usser_input == 'Y':
      print('said yes')
      return True
    elif usser_input =='N':
      print('said no')
      return False
    else :
      print('Try again')


#Menu of choices
escape =True
while escape: 
    print('Welcome to the random Generator Password'.center(50,'='))
    print('Select your choices')

    #Lenght of password
    valid_Length =True
    while valid_Length:
        print('Lenght (Limit 30): ')
        try:
            lenght = int(input())
            if lenght > 0 and lenght <= 30:
                valid_Length = False
            elif lenght >30:
             print("That goes over the limit.\nTry again")  
            else:
                print('It has to be a positive number')
        except ValueError:
            print('It must be int ynumbers hun')
            continue

    #yes and no options
    lower = yesno('Do you want lowercase letters? (Y/N) ')
    upper = yesno('Do you want uppercase letters? (Y/N) ')
    digits = yesno('Do you want to add digits? (Y/N) ')
    symbols = yesno('Do you want to include simbols? (Y/N) ')
    print(lenght,lower, upper, digits, symbols)

    #generate the password
    result = password(lenght,lower, upper, digits, symbols)
    
    #Show password
    if result:
        pyperclip.copy(result)
        print(f'Your password is: {result}')
        print('Your password has been succesfully copied into your clipboard')

#ask if they want to continue        
escape = yesno('Do you want to create another one? (Y/N)')