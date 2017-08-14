from collections import deque

def simplifyPath(path):
    folders = path.split('/')
    pathQ = deque()
    for folder in folders:
        pathQ.append(folder)
    
    simplifiedPath = deque()
    
    while len(pathQ) > 0:
        nextFolder = pathQ.popleft()
        if nextFolder == '..':
            if len(simplifiedPath) > 0:
                simplifiedPath.pop()
        elif nextFolder == '.' or nextFolder == '':
            pass
        else:
            simplifiedPath.append(nextFolder)
    
    out = '/'
    for i in simplifiedPath:
        out += i + '/'
    
    if len(out) > 1:
        return out[:-1]
    else:
        return out
