# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million.

def is_prime(n):
  if n <= 1:
    return False
  
  d = 2
  while d*d <= n:
    if n % d == 0:
      return False
    d += 1
  return True

count = 0
soma = 0

while count <= 2000000:
  value = is_prime(count)
  if value == True:
    soma += count
  count += 1

print(soma)
