#!/usr/bin/env python3
from random import getrandbits
import sys
flag = open("flag.txt","r").read()

class PRNG:
	a = getrandbits(64)
	b = getrandbits(64)
	p = 11760071327054544317

	def __init__(self, seed):
		self.state = seed

	def next(self):
		self.state = (self.a * self.state + self.b) % self.p
		return self.state

print("Guessing is a important skill in CTF, try to guess my number!")
print("I give you first 3 values of my number,")
print("but you need to guess correctly for next 1000 times in a row!!")
print("If you're lucky enough, you can get the flag as reward!\n")

gen = PRNG(getrandbits(64))
print(f"First 3 values: {gen.next()},{gen.next()},{gen.next()}\n")

for i in range(1000):
	try:
		guess = int(input("Enter a number between 0-9999: "))
	except:
		print("HACKER ALERT! Aborting..")
		sys.exit()
	num = gen.next() % 10000
	if guess == num:
		print("Incredible! Next round!")
	else:
		print("Sorry! Better luck next time..")
		sys.exit()

print(f"Well done!! Good guessing! Flag: {flag}")