from binheap import MinHeap

def main(array):
	heap = MinHeap()
	for elem in array:
		heap.insert(elem)
	index = 0
	while index < len(array):
		array[index] = heap.delMin()
		index = index + 1
		print heap.size()
	return array

# array = [6,7,2,4,2,8,5,3,8]
# print array
# print main(array)