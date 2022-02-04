# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
coffee_bot()

def get_size():
  res = input('What size drink can I get for you?        \n[a] Small \n[b] Medium \n[c] Large \n>')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

get_size()