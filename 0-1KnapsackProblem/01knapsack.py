import datetime, sys

def run():
	path = input("Which method do you want to use? \nRecursive (1), Dynamic (2), Greedy (3), or Backtracking (4)?\nOr press q to quit  : ")
	
	if path == '1':
		time1 = datetime.datetime.now()
		print( knapsack1(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Recursive: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n \n \n")
		run()
		
	elif path == '2':
		time1 = datetime.datetime.now()
		print( knapsack2(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Dynamic: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n \n \n")
		run()
	
	elif path == '3':
		time1 = datetime.datetime.now()
		print( knapsack3(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Greedy: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n \n \n")
		run()
	
	elif path == '4':
		time1 = datetime.datetime.now()
		print( knapsack4(W, items[2], items[1], len(items[0])) )
		time2 = datetime.datetime.now()
		tdelta = time2 - time1
		print("Backtracking: Time taken: %s ms" % int(tdelta.total_seconds()*1000) )
		print("\n \n \n")
		run()
		
	elif path == 'q':
		sys.exit("End.")
		
	else:
		print("Error: no valid option chosen. Please try again.")
		print("\n \n \n")
		run()
		
# ----------------------------------------------------------------------

# A recursive solution to the 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapsack1(W , wt , val , n):
    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapsack1(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapsack1(W-wt[n-1] , wt , val , n-1), knapsack1(W , wt , val , n-1))
# end of function knapsack1

# ----------------------------------------------------------------------

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapsack2(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
# end of function knapsack2
	
# ----------------------------------------------------------------------

def knapsack3(W, wt, val, n):
	return "null"

def knapsack4(W, wt, val, n):
	return "null"

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