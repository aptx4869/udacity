# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    ROW=len(grid[0])
    COL=len(grid)
    value = [[99 for row in range(ROW)] for col in range(COL)]
    loop_dict={}
    for x in range(COL):
        for y in range(ROW):
            loop_dict[(x,y)]=0
    #loop_dict={(x,y):0 for x in range(COL) for y in range(ROW)}
    change = True
    l_dict=loop_dict.copy()

    while change:
        change = False

        loop_dict=l_dict.copy()

        for x,y in loop_dict:
            if goal[0] == x and goal[1] == y:
                if value[x][y] > 0:
                    value[x][y] = 0
                    loop_dict[(x,y)]+=1

                    change = True

            elif grid[x][y] == 0:
                for a in range(len(delta)):
                    x2 = x + delta[a][0]
                    y2 = y + delta[a][1]

                    if x2 >= 0 and x2 < COL and y2 >= 0 and y2 < ROW and grid[x2][y2] == 0:
                        v2 = value[x2][y2] + cost_step

                        if v2 < value[x][y]:
                            loop_dict[(x,y)]+=1
                            change = True
                            value[x][y] = v2
            if loop_dict[(x,y)] > 0:
                l_dict.pop((x,y))
                continue
    return value 
    #make sure your function returns a grid of values as demonstrated in the previous video.

for line in  compute_value():
    print line

import cProfile
cProfile.run('compute_value()')

#[11, 99, 7, 6, 5, 4]
#[10, 99, 6, 5, 4, 3]
#[9, 99, 5, 4, 3, 2]
#[8, 99, 4, 3, 2, 1]
#[7, 6, 5, 4, 99, 0]
    
