import math

n = int(raw_input("Number: "))
factors = set()
for i in xrange(2, n+1):
	while n % i == 0:
		n /= i
		factors.add(i)

print reduce(lambda x, y: x * y, factors)