print('Welcome To PanuPassword Generator!')
#Simple Version
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=''
for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password+=random_char

for char in range(1,nr_symbols+1):
    random_char=random.choice(symbols)
    password+=random_char

for char in range(1,nr_numbers+1):
    random_char=random.choice(numbers)
    password+=random_char

print(f'You can use this password:{password}')

q=input('Do You want to create Another Password?,which will be more stronger!')
if q=='yes':
    #Complex Version
#Simple Version
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  password_list=[]
  for char in range(1,nr_letters+1):
      random_char=random.choice(letters)
      password_list+=random_char

  for char in range(1,nr_symbols+1):
      random_char=random.choice(symbols)
      password_list+=random_char

  for char in range(1,nr_numbers+1):
      random_char=random.choice(numbers)
      password_list+=random_char

  random.shuffle(password_list)

  Strongest_Password=''
  for j in password_list:
     Strongest_Password+=j

  print('You can also use this password this is stronger than previous:',Strongest_Password)
else:
    print('Thank you for using our service❤️')
