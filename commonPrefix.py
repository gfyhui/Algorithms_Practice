def longestPrefix(A,B):
	smallest = min(len(A),len(B))
	for i in range(smallest):
		if A[i] != B[i]:
			break
	return A[:i]

print longestPrefix('hellz','hello')
print longestPrefix('qwertyuiop','qwertyzxxc')
print longestPrefix('aabc','aacd')
print longestPrefix('ewa','saa')