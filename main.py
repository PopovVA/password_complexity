import urwid


def on_ask_change(edit, password):
    reply.set_text("Complexity score: %s" % get_complexity(password))

def get_complexity(password):

  score = 0
  checks = [
  is_very_long,
  has_digit,
  has_letters,
  has_upper_letters,
  has_lower_letters,
  has_symbols,
  has_only_symbols
  ]

  for check in checks:
    if check(password):
      score+=2
  
  return score

def is_very_long(password):
  return len(password) >= 12

def has_digit(password):
  return any(symbol.isdigit() for symbol in password) 

def has_letters(password):
  return any(symbol.isalpha() for symbol in password)

def has_upper_letters(password):
  return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
  return any(symbol.islower() for symbol in password)

def has_symbols(password):
   for symbol in password:
    if not symbol.isdigit() and not symbol.isalpha():
      return True
   return False

def has_only_symbols(password):
  amount_symbols = 0
  for symbol in password:
    if not symbol.isdigit() and not symbol.isalpha():
        amount_symbols += 1 
  if amount_symbols==len(password):
      return True
  return False



if __name__ == '__main__':
  ask = urwid.Edit('Type your password : ')
  reply = urwid.Text("")
  menu = urwid.Pile([ask, reply])
  menu = urwid.Filler(menu, valign='top')
  urwid.connect_signal(ask, 'change', on_ask_change)
  urwid.MainLoop(menu).run()
