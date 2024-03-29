# A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, a^2+b^2 = c^2
# For example, 3^2+4^2= 9 + 6 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a+b+c=1000.
# Find the product abc.

for a in range(1, 1000):
  for b in range(1, 1000):
    for c in range(1, 1000):
      if a < b < c:
        if (a * a) + (b * b) == (c * c):
          if a + b + c == 1000:
            print([a,b,c])
            print(a * b * c)
