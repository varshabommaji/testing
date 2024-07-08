def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return (a*4)
  else: 
    return (a+b)

def extra_end(str):
 return (str[-2] + str[-1] + str[-2] + str[-1] + str[-2] + str[-1])

def first_two(str):
  if len(str) == 0: 
    return ""
  elif len(str) < 2:
    return str
  else: 
    return (str[0] + str [1])

def first_half(str):
  half = len(str)/2
  return str[:half]

def without_end(str):
  length = len(str)
  newstr = str[:length-1]
  newnewstr = newstr[1:]
  return newnewstr