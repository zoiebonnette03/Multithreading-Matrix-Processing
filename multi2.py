import argparse
from multiprocessing import Pool

# global variables
prime = (0,1,4,6,8)
even = (2,4,6,8)
offsets = [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]

# command line arguments
parser = argparse.ArgumentParser(description="Matrix multiprocessing")
parser.add_argument("-i", "--input", help="Input file", required=True)
parser.add_argument("-o", "--output", help="Output file", required=True)
parser.add_argument("-p", "--processes", help="Number of processes", default=1)
args = parser.parse_args()

def main():
  print("Project :: R11910353")

  # define processing pool
  maxpro = int(args.processes)
  processPool = Pool(processes=maxpro)
  
  matrix = makematrix(args.input)
  length = len(matrix)
  timestep = 0
  # loops while timestep < 100
  while timestep < 100:
    poolData = []
    # matrixData includes matrix, length, x, y as it goes through matrix
    for x in range(length):
      for y in range(length):
        matrixData = [matrix, length, x, y]
        poolData.append(matrixData)
    finalData = processPool.map(matty, poolData)
    del(poolData)
    # get data from finalData and make a matrix
    for i in range(length):
      for j in range(length):
        matrix[i][j] = finalData[i * length + j]
    del(finalData)
    # increment timestep
    timestep += 1

  # copy final matrix to output file
  with open(args.output, "w") as out:
    for row in matrix:
      out.write("".join(row) + '\n')
      
# algorithm to count neighbors and returns '.' or 'O'
def matty(matrixData):
  matrix = matrixData[0]
  length = matrixData[1]
  x, y = matrixData[2], matrixData[3]
  data = '.'
  count = 0
  for a, b in offsets:
    if(matrix[(x+a)%length][(y+b)%length] == 'O'):
      count += 1
  if matrix[x][y] == 'O':
    data ='O'
    if count in prime:
      data = '.'
  elif count in even and matrix[x][y] == '.':
    data = 'O'
  return data

# define a matrix from the given input file
def makematrix(inputfile):
  matrix = []
  with open(inputfile, "r") as f:
    for line in f:
      matrix.append(list(line.strip()))
  return matrix 

if __name__ == "__main__":
  main()