from Crypto.Util.number import inverse
X = [8024128649592323171,9457093108975811254,7209505091452067243]
p = 11760071327054544317
a = (X[2]-X[1])* inverse(X[1]-X[0],p) % p
b = (X[1]-a*X[0]) % p

x = X[2]
for i in range(1000):
	x = ((a*x + b)%p)
	print(x %10000)