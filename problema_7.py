# By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def is_prime(n):
  if n <= 1:
    return False
  
  d = 2
  while d*d <= n:
    if n % d == 0:
      return False
    d += 1
  return True

primo = 1
count = 1
count_primo = 1

while count_primo <= 10001:
  value = is_prime(count)
  if value == True:
    primo = count
    count_primo += 1
  count += 1

print(primo)
