# Long Crypto Guessing
Description:
> Guessing is a important skill in CTF, try to guess my number to proof your guessing skill! Connect with nc 159.89.198.90 2000

Attachment:
- [server.py](server.py)

We were given a python script:
```py
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
```
Try netcat the server:
```
nc 159.89.198.90 2000
Guessing is a important skill in CTF, try to guess my number!
I give you first 3 values of my number,
but you need to guess correctly for next 1000 times in a row!!
If you're lucky enough, you can get the flag as reward!

First 3 values: 4147294294122806512,3200450807340402416,9987904953671074292

Enter a number between 0-9999: 1337
Sorry! Better luck next time..
```
As you can see, we need to some how predict the number generate by the PRNG (Pseudorandom number generator).

And need answer it 1K times in a row!

The challenge title already indicate, that is **[LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator)**

For more details of how to solve this, you can see my [previous writeup on FwordCTF](https://github.com/Hong5489/FwordCTF2020/tree/master/random) *(Actually I was inspired from this challenge)*

I solve this using [python script](solve.py):
```py
from Crypto.Util.number import inverse
X = [8400704725634319499,3036744318011607195,10829220720803385147]
p = 11760071327054544317
a = (X[2]-X[1])* inverse(X[1]-X[0],p) % p
b = (X[1]-a*X[0]) % p

x = X[2]
for i in range(1000):
	x = ((a*x + b)%p)
	print(x %10000)
```
Then pipe the output to `xclip` to copy it:
```bash
python3 solve.py | xclip -in -selection clipboard
```
Then paste it in the netcat shell *(For people who lazy to write a script)*:
```
nc 159.89.198.90 2000
Guessing is a important skill in CTF, try to guess my number!
I give you first 3 values of my number,
but you need to guess correctly for next 1000 times in a row!!
If you're lucky enough, you can get the flag as reward!

First 3 values: 8024128649592323171,9457093108975811254,7209505091452067243

Enter a number between 0-9999: 
...
...
...
Enter a number between 0-9999: Incredible! Next round!
Enter a number between 0-9999: Incredible! Next round!
Enter a number between 0-9999: Incredible! Next round!
Enter a number between 0-9999: Incredible! Next round!
Enter a number between 0-9999: Incredible! Next round!
Well done!! Good guessing! Flag: wgmy{e42a0eeb24c8c9c4a473309f8d8c7feb}
```
## Flag
> wgmy{e42a0eeb24c8c9c4a473309f8d8c7feb}