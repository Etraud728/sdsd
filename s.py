from random import randint
import sys
s = print('Hi Guess the number with in 10 number with 3 tries')
n = randint(1,10)
ans = None
t = 1
while ans != n:
  ans = int(input('Guess the number: '))
  if ans == n:
    break
  else:
    if t == 3:
      print('You lost')
      sys.exit()
    else:
      if ans < n:
        print('Go high')
        t = t + 1
      elif ans > n:
        print('Go low')
        t = t + 1

print('Well done')
3
# https://www.pythonforbeginners.com
