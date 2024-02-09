# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.

maior = 100 * 100

for i in range(100, 999):
  for j in range(100, 999):
    temp = i * j

    if str(temp) == str(temp)[::-1]:
      if (temp > maior):
        maior = temp

print(maior)
