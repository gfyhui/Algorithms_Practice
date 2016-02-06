def addMatrices(A,B):
	C = []
	for i in range(len(A)):
		C.append([])
		for j in range(len(A)):
			C[i].append(A[i][j] + B[i][j])
	return C

def subMatrices(A,B):
	C = []
	for i in range(len(A)):
		C.append([])
		for j in range(len(A)):
			C[i].append(A[i][j] - B[i][j])
	return C

M1 = [[1,2],[3,4]]
M2 = [[9,8],[7,8]]
# print M1
# print M2
M3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[53,14,15,16]]
M4 = [[5,5321,1,3],[3,643,1,2],[7,4,2,3],[1,3,4,6]]
# print M1
# print M2
# print addMatrices(M1,M2)
# print subMatrices(M1,M2)

def strassen(A,B):
	n = len(A)
	C = []
	for i in range(n):
		C.append([])
		for j in range(n):
			C[i].append(None)
	
	if n == 1:
		C[0][0] = A[0][0] * B[0][0]
		return C
	else:
		A11 = []
		A12 = []
		A21 = []
		A22 = []
		B11 = []
		B12 = []
		B21 = []
		B22 = []
		for i in range(n//2):
			A11.append([])
			A12.append([])
			A21.append([])
			A22.append([])
			B11.append([])
			B12.append([])
			B21.append([])
			B22.append([])
			for j in range(n//2):
				A11[i].append(A[i][j])
				A12[i].append(A[i][j+n//2])
				A21[i].append(A[i+n//2][j])
				A22[i].append(A[i+n//2][j+n//2])
				B11[i].append(B[i][j])
				B12[i].append(B[i][j+n//2])
				B21[i].append(B[i+n//2][j])
				B22[i].append(B[i+n//2][j+n//2])
		C11 = []
		C12 = []
		C21 = []
		C22 = []
		for i in range(n//2):
			C11.append([])
			C12.append([])
			C21.append([])
			C22.append([])
			for j in range(n//2):
				C11[i].append(None)
				C12[i].append(None)
				C21[i].append(None)
				C22[i].append(None)
		S1 = subMatrices(B12,B22)
		S2 = addMatrices(A11,A12)
		S3 = addMatrices(A21,A22)
		S4 = subMatrices(B21,B11)
		S5 = addMatrices(A11,A22)
		S6 = addMatrices(B11,B22)
		S7 = subMatrices(A12,A22)
		S8 = addMatrices(B21,B22)
		S9 = subMatrices(A11,A21)
		S10 = addMatrices(B11,B12)
		P1 = strassen(A11,S1)
		P2 = strassen(S2,B22)
		P3 = strassen(S3,B11)
		P4 = strassen(A22,S4)
		P5 = strassen(S5,S6)
		P6 = strassen(S7,S8)
		P7 = strassen(S9,S10)
		C11 = addMatrices(addMatrices(P5,P4),subMatrices(P6,P2))
		C12 = addMatrices(P1,P2)
		C21 = addMatrices(P3,P4)
		C22 = subMatrices(addMatrices(P5,P1),addMatrices(P3,P7))
		# print C11
		# print C12
		# print C21
		# print C22
		for i in range(n//2):
			for j in range(n//2):
				C[i][j] = C11[i][j]
				C[i][j+n//2] = C12[i][j]
				C[i+n//2][j] = C21[i][j]
				C[i+n//2][j+n//2] = C22[i][j]
		return C

def regular(A,B):
	C = []
	for i in range(len(A)):
		C.append([])
		for j in range(len(A)):
			total = 0
			for k in range(len(A)):
				total = total + A[i][k]*B[k][j]
			C[i].append(total)
	return C

# print M1
# print M2
# print regular(M1,M2)
# print strassen(M1,M2)
# print
# print M3
# print M4
print regular(M3,M4)
print strassen(M3,M4)