def recursive(i):
	if i==0 or i==1:
		return 1
	else:
		return recursive(i-1) + recursive(i-2)

# for i in range(10):
# 	print recursive(i)

def iterative(i):
	a = 1
	b = 1
	cur = 1
	count = 1
	while count < i:
		cur = a + b
		a = b
		b = cur
		count = count + 1
	return cur

for i in range(10):
	print iterative(i)