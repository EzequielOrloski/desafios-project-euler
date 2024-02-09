# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

menor = 2520
parar = False

while parar == False:
  naoDivide = False
  for i in range(2, 20):
    if menor % i != 0:
      naoDivide = True
      break

  if naoDivide == False:
    parar = True
  else:
    menor = menor + 1

print(menor)
