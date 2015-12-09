def bruteforce(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0 :
        return 0

    if (wt[n-1] > W):
        return bruteforce(W , wt , val , n-1)
    else:
        return max(val[n-1] + bruteforce(W-wt[n-1] , wt , val , n-1), bruteforce(W , wt , val , n-1))