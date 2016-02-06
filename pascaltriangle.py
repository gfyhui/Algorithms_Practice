def main(height):
	if height == 1:
		row = [0,1,0]
		print row[1:len(row)-1]
		return row
	else:
		rowabove = main(height-1)
		row = [0] * height
		row.append(0)
		row.append(0)
		for index in range(1,height+1):
			row[index] = rowabove[index-1] + rowabove[index]
		print row[1:len(row)-1]
		return row

main(5)