import string

def main(word):
	d = dict()
	for character in word:
		if character in d:
			return False
		else:
			d[character] = 1
	return True

def changestr(word):
    output = ''
    lastspaceindex = -1
    previousspaceindex = -1
    for i in range(len(word)):
        if word[i] == ' ':
            output = output + word[previousspaceindex+1:i] + '%20'
            lastspaceindex = i
            previousspaceindex = i
    output = output + word[lastspaceindex+1:]
    return output


# a = ' hello   world    '
# print a
# print changestr(a)

word = 'aabcccccaaa'
# print word
# print countletters(word)

# def compress(word):
#     count = 0
#     previous = ''
#     compressed = ''
#     for letter in word:
#         if letter != previous:
#             if count > 0:
#                 compressed = compressed + previous + str(count)
#             count = 1
#             previous = letter
#         else:
#             count = count + 1
#     compressed = compressed + previous + str(count)
#     if len(compressed) < len(word):
#     	return compressed
#     else:
#     	return word

def compress(word):
	word_list = []
	thing = word[0]
	count = 1
	for i in range(1,len(word)):
		if thing == word[i]:
			count = count + 1
		else:
			word_list.append(thing)
			word_list.append(str(count))
			thing = word[i]
			count = 1
	word_list.append(thing)
	word_list.append(str(count))
	temp = ''.join(word_list)
	if len(temp) < len(word):
		return temp
	else:
		return word

print word
print compress(word)

def rotate(matrix):
	N = len(matrix)
	# output = [[0]*N]*N
	output = []
	for i in range(N):
		output.append([])
		for j in range(N):
			output[i].append(0)
	print output
	for row in range(N):
		for col in range(N):
			# print output
			output[N-col-1][row] = matrix[row][col]
			print (N-col-1,row)
			print output
			# print (row,col)
			print matrix[N-col-1][row]
	# print output[0]
	# print output[1]
	return output

# def rotate2(matrix):
#     N = len(matrix)
#     for i in range(N//2):
#         top = matrix[i][i:N-i]
#         print i
#         matrix[i][i:N-i] = matrix[i:N-i][N-i]
#         bottom = matrix[N-i][i+1:N-i+1]
#         bottom.reverse()
#         matrix[i:N-i][N-i] = bottom
#         matrix[N-i][i+1:N-i+1] = matrix[i+1:N-i+1][i]
#         top.reverse()
# #         matrix[i+1:N-i+1][i] = top
#     return matrix


M1 = [[1,2],[3,4]]
# M2 = [[9,8],[7,8]]
M5 = [[1,2,3],[4,5,6],[7,8,9]]
# # print M1
# # print M2
# # M3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[53,14,15,16]]
# # M4 = [[5,5321,1,3],[3,643,1,2],[7,4,2,3],[1,3,4,6]]

print M1
print rotate2(M1)
print M5
print rotate2(M5)
# print new