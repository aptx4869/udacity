# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():
    ROW=len(grid[0])
    COL=len(grid)
    value = [[99 for row in range(ROW)] for col in range(COL)]
    policy = [[' ' for row in range(ROW)] for col in range(COL)]
    loop_dict={}
    for x in range(COL):
        for y in range(ROW):
            loop_dict[(x,y)]=0
    #loop_dict={(x,y):0 for x in range(COL) for y in range(ROW)}
    v_change = True
    l_dict=loop_dict.copy()
    action_dict={(1,0,"up"):(1,1)
            (1,0,"left"):(0,1)
            (1,0,"down"):(None,None)
            (1,0,"right"):(2,1)

            (0,1,"up"):2,
            (0,1,"left"):1,
            (0,1,"down"):0,
            (0,1,"right"):None,
            (0,-1,"up"):0,
            (0,-1,"left"):None,
            (0,-1,"down"):2,
            (0,-1,"right"):1,

            (-1,0,"up"):None,
            (-1,0,"left"):2,
            (-1,0,"down"):1,
            (-1,0,"right"):0}
    def Action_Index(x,y,x1,y1,policy):
        """return the action index"""
        state=policy[x][y]
        #for i in policy:
            #print i
        try:
            return action_dict[x1-x,y1-y,state]
        except:
            return 1


    while v_change or p_change:
        v_change = False
        p_change = False
        for x in range(COL):
            for y in range(ROW):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        v_change = True
                elif init[0] == x and goal[1]==y:
                    state = policy[x][y]
                    if state != forward_name[init[2]]:
                        policy[x][y] = action_name[init[2]]
                        #p_change = True
                        #print x ,y

                elif grid[x][y] == 0:
                    for a in range(len(forward)):
                        x2 = x + forward[a][0]
                        y2 = y + forward[a][1]

                        if 0 <= x2 < COL and 0 <= y2 < ROW and grid[x2][y2] == 0:
                            action_index=Action_Index(x,y,x2,y2,policy)
                            policy[x][y] = forward_name[a]
                            v2=98
                            if action_index:
                                cost_step=cost[action_index]
                                v2 = value[x2][y2] + cost_step
                                print v2

                            if v2 < value[x][y]:
                                v_change = True
                                value[x][y] = v2
                                print v2
                                policy[x][y] = forward_name[a]


            #elif grid[x][y] == 0:
                #for a in range(len(delta)):
                    #x2 = x + delta[a][0]
                    #y2 = y + delta[a][1]

                    #if x2 >= 0 and x2 < COL and y2 >= 0 and y2 < ROW and grid[x2][y2] == 0:
                        #v2 = value[x2][y2] + cost_step

                        #if v2 < value[x][y]:
                            #loop_dict[(x,y)]+=1
                            #v_change = True
                            #value[x][y] = v2
                            #policy[x][y] = delta_name[a]
    for line in value:
        print line
    return policy # Make sure your function returns the expected grid.
#
    #while v_change:
        #v_change = False

        #loop_dict=l_dict.copy()

        #for x,y in loop_dict:
            #if goal[0] == x and goal[1] == y:
                #if value[x][y] > 0:
                    #value[x][y] = 0
                    #policy[x][y] = '*'
                    #loop_dict[(x,y)]+=1

                    #v_change = True

            #elif grid[x][y] == 0:
                #for a in range(len(delta)):
                    #x2 = x + delta[a][0]
                    #y2 = y + delta[a][1]

                    #if x2 >= 0 and x2 < COL and y2 >= 0 and y2 < ROW and grid[x2][y2] == 0:
                        #v2 = value[x2][y2] + cost_step

                        #if v2 < value[x][y]:
                            #loop_dict[(x,y)]+=1
                            #v_change = True
                            #value[x][y] = v2
                            #policy[x][y] = delta_name[a]
            #if loop_dict[(x,y)] > 0:
                #l_dict.pop((x,y))
                #continue

    #return policy # Make sure your function returns the expected grid.

for line in  optimum_policy2D():
    print line
