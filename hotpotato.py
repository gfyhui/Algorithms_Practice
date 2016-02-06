from queue import Queue
import random

def main(people,num):
	q = initialize(people)
	count = 1
	while q.size() > 1:
		if count == num:
			q.dequeue()
			count = 1
		else:
			first = q.dequeue()
			q.enqueue(first)
			count = count + 1
	return q.dequeue()

def initialize(people):
	q = Queue()
	for person in people:
		q.enqueue(person)
	return q

people = ['Aaron', 'Bob', 'Courtney', 'Dillon', 'Ellen', 'Fred', 'George']
# people = ['a','b','c']
# people = ['a','b']
num = 3

print main(people,num)