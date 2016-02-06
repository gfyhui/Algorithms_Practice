# test = open("foo.txt",'r')
# line = test.readline()
# print line
# line = test.readline()
# print line
# line = test.readline()
# print line
# line = test.readline()
# print line

# test = open("foo.txt",'r')
# for line in test:
# 	if line != "\n":
# 		if line[-1] == "\n":
# 			print line[:-1]
# 		else:
# 			print line

# for line in test:
# 	for letter in line:
# 		if ord(letter)>=48 and ord(letter)<=57:
# 			print letter

text = open("foo.txt",'r')
for line in text:
	linedisp = []
	for letter in line:
		if (letter == 'x') or (ord(letter)>=48 and ord(letter)<=57):
			linedisp.append(letter)
	for val in linedisp:
		print val,
		print ' ',
