from stack import Stack 

#Solves the tower of hanoi problem.

def main(height):
	s1 = Stack()
	s2 = Stack()
	s3 = Stack()
	for a in range(1,height+1):
		s2.push(a)
	while not s2.isEmpty():
		s1.push(s2.pop())
	helper(height,s1,s2,s3)
	return s1,s2,s3

def helper(height,frompole,topole,withpole):
	if height >= 1:
		helper(height-1,frompole,withpole,topole)
		topole.push(frompole.pop())
		helper(height-1,withpole,topole,frompole)

stack1, stack2, stack3 = main(8)
print stack1
print stack2
print stack3