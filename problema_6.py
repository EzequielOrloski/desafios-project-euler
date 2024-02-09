# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + 3 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

temp1 = 0
temp2 = 0
n = 101

for i in range(1, n):
  temp = i * i
  temp1 = temp + temp1

temp2 = sum(list(range(1, n))) ** 2

print(temp2 - temp1)
