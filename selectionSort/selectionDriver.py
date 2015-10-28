from selectionSort import selectionSort
input = raw_input("please input a list of numbers:  ")
numbers = map(int, input.split(","))
selectionSort(numbers)
for i in range(0,len(numbers)):
	print numbers[i]
