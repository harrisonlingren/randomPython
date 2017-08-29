def treeBottom(tree):
    
    def findTreeDepth(t):
        currDepth = 0
        maxDepth = 0
        for symbol in t:
            if symbol == '(':
                currDepth += 1
            elif symbol == ')':
                currDepth -= 1

            if currDepth > maxDepth:
                maxDepth = currDepth

        return maxDepth - 1
    
    def getBottomValues(t, d):
        bottomVals = []
        currDepth = 0
        i = 0
        while i < len(t)-1:
            if t[i] == '(':
                currDepth += 1
            elif t[i] == ')':
                currDepth -= 1

            if currDepth == d and t[i+1].isdigit():
                j = i
                nextNum = ''
                while t[j+1].isdigit():
                    j += 1
                    nextNum += t[j]
                i = j
                bottomVals.append(int(nextNum))
                
            i += 1
        return bottomVals
        
    treeDepth = findTreeDepth(tree)
    return getBottomValues(tree, treeDepth)
