from math import sqrt

class board(object):
  "A sudoku board"
  grid = []
  dim = 0
  
  def __init__(self, dim=9):
    self.dim = dim
    self.grid = [[x for x in [0]*dim] for y in [0]*dim]
  
def checkBoard(B):
  return row(B) and col(B) and sec(B)
  
def row(b):
  for y in range(b.dim):
    check = set()
    for x in range(b.dim):
      #print('row check on: %d,%d' % (x,y))
      if b.grid[x][y] in check:
        return False
      if b.grid[x][y] > 9 or b.grid[x][y] < 1:
        return False
      check.add(b.grid[x][y])
  return True
  
def col(b):
  for x in range(b.dim):
    check = set()
    for y in range(b.dim):
      #print('col check on: %d,%d' % (x,y))
      if b.grid[x][y] in check:
        return False
      check.add(b.grid[x][y])
  return True
  
def sec(b):
  for x,y in zip([0,3,6,0,3,6,0,3,6],[0,0,0,3,3,3,6,6,6]):
    check = set()
    for xx in range(x, x+int(sqrt(b.dim))):
      for yy in range(y, y+int(sqrt(b.dim))):
        #print('sec check on: %d,%d' % (xx,yy))
        if b.grid[xx][yy] in check:
          return False
        check.add(b.grid[xx][yy])
  return True
  
def main():
  b = board(dim=9)
  b.grid = [
    [2,7,6,3,1,4,9,5,8],
    [8,5,4,9,6,2,7,1,3],
    [9,1,3,8,7,5,2,6,4],
    [4,6,8,1,2,7,3,9,5],
    [5,9,7,4,3,8,6,2,1],
    [1,3,2,5,9,6,4,8,7],
    [3,2,5,7,8,9,1,4,6],
    [6,4,1,2,5,3,8,7,9],
    [7,8,9,6,4,1,5,3,2]]
    
  print(checkBoard(b))
  
main()
