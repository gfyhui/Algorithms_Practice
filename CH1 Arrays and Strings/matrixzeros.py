def bruteforce(matrix):
    zeros = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                zeros.append((i,j))
    for coord in zeros:
        for index in range(len(matrix[coord[0]])):
            matrix[coord[0]][index] = 0
        for index in range(len(matrix)):
            matrix[index][coord[1]] = 0

M1 = [[1,2],[0,4]]
M3 = [[1,2,0,4],[5,6,0,8],[9,0,11,12],[53,14,15,16]]

# print M1
# bruteforce(M1)
# print M1

print M3
bruteforce(M3)
print M3