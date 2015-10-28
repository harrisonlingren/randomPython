def fib1(n):
	if (n == 1 or n == 2):
		return 1
	return fib1(n-1) + fib1(n-2)

def fib2(n):
	A = []
	A.append(1)
	A.append(1)
	if (n <= 2):
		return A[0]
	for i in range(2,n):
		A.append( A[i-1] + A[i-2] )
	return A[n-1]

def fib3(n):
	a = b = c = 1
	if (n <= 2):
		return a
	for i in range(3,n+1):
		c = a
		a = a + b
		b = c
	return a
	
num = int(input("Enter a number to compute with fib:"))

a3 = fib3(num)
print("fib3: %d" % a3)

a2 = fib2(num)
print("fib2: %d" % a2)

a1 = fib1(num)
print("fib1: %d" % a1)