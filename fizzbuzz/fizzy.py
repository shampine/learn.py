i = 0

def testModulo(i):
  if (i % 15) == 0:
    result = 'fizzbuzz'
  elif (i % 5) == 0:
    result = 'buzz'
  elif (i % 3) == 0:
    result = 'fizz'
  else:
    result = i
  return result

while i < 100:
  print testModulo(i)
  i += 1
