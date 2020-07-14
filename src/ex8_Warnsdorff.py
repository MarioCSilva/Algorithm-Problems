def isValidMove(grid, x, y):
        maxL = len(grid)-1
        if x > maxL or y > maxL or x < 0 or y < 0 or grid[x][y] > -1 :
                return False
        return True

def getValidMoves(grid, x, y, validMoves):
        return [ (i,j) for i,j in validMoves if isValidMove(grid, x+i, y+j) ]

def movesSortedbyNumNextValidMoves(grid, x, y, legalMoves):
        nextValidMoves = [ (i,j) for i,j in getValidMoves(grid,x,y,legalMoves) ]
        # find the number of valid moves for each of the possible valid mode from x,y
        withNumNextValidMoves = [ (len(getValidMoves(grid,x+i,y+j,legalMoves)),i,j) for i,j in nextValidMoves]
        # sort based on the number so that the one with smallest number of valid moves comes on the top
        return [ (t[1],t[2]) for t in sorted(withNumNextValidMoves) ]


def _solveKnightsTour(grid, x, y, num, legalMoves):
        if num == pow(len(grid),2):
                return True
        for i,j in movesSortedbyNumNextValidMoves(grid,x,y,legalMoves):
        #For testing the advantage of warnsdorff heuristics, comment the above line and uncomment the below line
        #for i,j in getValidMoves(grid,x,y,legalMoves):
                xN,yN = x+i,y+j
                if isValidMove(grid,xN,yN):
                        grid[xN][yN] = num
                        if _solveKnightsTour(grid, xN, yN, num+1, legalMoves):
                                return True
                        grid[xN][yN] = -2
        return False

def printSolution(gridSize, grid): 
    ''' 
        A utility function to print Chessboard matrix 
    '''
    for i in range(gridSize): 
        for j in range(gridSize):
            if len(str(grid[i][j]))==1:
                print("0"+str(grid[i][j]),end =' ')
            else:
                print(grid[i][j],end =' ') 
        print() 

def solveKnightsTour(gridSize, startX=0, startY=0):
    legalMoves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    #Initializing the grid
    grid = [ x[:] for x in [[-1]*gridSize]*gridSize ]
    grid[startX][startY] = 0
    if _solveKnightsTour(grid,startX,startY,1,legalMoves):
        printSolution(gridSize, grid)
    else:
        print('Could not solve the problem..')

if __name__ == "__main__":  
    
    # Chessboard Size 
    n = 8

    str_input = input()

    pos_init = int(str_input)

    init_x = pos_init // n
    init_y = pos_init - n * init_x

    solveKnightsTour(n, init_x, init_y)