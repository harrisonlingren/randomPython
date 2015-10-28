import random

def coinFlip(n):
	
	flip = []
	avg = 0.00
	heads = 0
	
	print "\n> Flipping..."
	
	for i in range(n):
		flip.append( random.randint(0,1) )
		heads += flip[i]
	
	
	tails = num - heads
	avg = float( float(heads) / float(num) ) * 100
	
	print "> Flipped %d heads and %d tails" % (heads, tails)
	print "> Toss average was %d%% heads and %d%% tails." % (avg, 100-float(avg) )
	

num = int( raw_input("Enter the number of coin tosses you want to test:") )

coinFlip(num)
