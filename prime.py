for i in range(1,3000):
	is_prime = True
	for k in range(2,i):
		if (i%k) == 0:
			print(i, " is divisible by ", k)
			is_prime = False
			break
	if is_prime:
		print(i, " is prime ")


	
