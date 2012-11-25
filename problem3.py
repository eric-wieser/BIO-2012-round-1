from collections import defaultdict
import math

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def asString(num):
	s = ""
	while num > 0:
		s = digits[num % 10] + s
		num //= 10
	return s

def differenceBetweenStrings(a, b):
	aLetters = defaultdict(int)
	bLetters = defaultdict(int)

	for letter in a:
		aLetters[letter] += 1
	for letter in b:
		bLetters[letter] += 1

	difference = 0
	for l in set(aLetters.keys() + bLetters.keys()):
		difference += abs(aLetters[l] - bLetters[l])
	return difference

def differenceBetween(n, m):
	return differenceBetweenStrings(asString(n), asString(m))

def stepsBetween(n, m):
	d = differenceBetween(n, m)
	return (d + 4) // 5

a = map(int, raw_input("1st: ").split())
b = map(int, raw_input("2nd: ").split())
c = map(int, raw_input("3rd: ").split())

print stepsBetween(*a)
print stepsBetween(*b)
print stepsBetween(*c)
