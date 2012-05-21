# ----------
# User Instructions:
# 
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
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
# modify code below
# ----------------------------------------

def optimum_policy():
    ROW=len(grid[0])
    COL=len(grid)
    value = [[99 for row in range(ROW)] for col in range(COL)]
    policy = [[' ' for row in range(ROW)] for col in range(COL)]
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
                    policy[x][y] = '*'
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
                            policy[x][y] = delta_name[a]
            if loop_dict[(x,y)] > 0:
                l_dict.pop((x,y))
                continue

    return policy # Make sure your function returns the expected grid.


for i in optimum_policy():
    print i
import cProfile
cProfile.run('optimum_policy()')

