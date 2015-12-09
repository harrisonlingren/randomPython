import datetime, sys, dynamic, bruteforce, backtracking, firstBranchBound

def run():
	path = input("Which method do you want to use? \nBrute force (1), Dynamic (2), Best First Branch Bound (3), or Backtracking (4)?\nOr press q to quit  : ")
	
	if path == '1':
		time1 = datetime.datetime.now()
		print( bruteforce.bruteforce(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Brute force: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n")
		run()
		
	elif path == '2':
		time1 = datetime.datetime.now()
		print( dynamic.dynamic(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Dynamic: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n")
		run()
	
	elif path == '3':
		time1 = datetime.datetime.now()
		print( firstBranchBound.firstBranchBound(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Best First Branch Bound: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n")
		run()
	
	elif path == '4':
		time1 = datetime.datetime.now()
		print( backtracking.backtracking(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Backtracking: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n")
		run()
		
	elif path == 'q':
		sys.exit("See ya!")
		
	else:
		print("Error: no valid option chosen. Please try again.")
		print("\n")
		run()
		
# ----------------------------------------------------------------------

# Main program, load items
	
n = int(input("Enter the number of items : "))
W = int(input("Enter total weight : "))

#init 2-dimensional array for items
items = [[0]*4 for i in range(n)]    # create 2-dimensional array

for i in range(n):
	items[i][0] = i+1
	items[i][1] = int(input("Enter profit for %s : " % (i+1) ) )
	items[i][2] = int(input("Enter weight for %s : " % (i+1) ) )
	items[i][3] = int(items[i][1] / items[i][2])

print()
print("Items:  %s" % items)

run()