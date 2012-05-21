colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8

def show(p):
    print '='*10
    for i in range(len(p)):
        print p[i]
    print '='*10
##Given the list motions=[1,1] which means the robot 
##moves right and then right again, compute the posterior 
##distribution if the robot first senses red, then moves 
##right one, then senses green, then moves right again, 
##starting with a uniform prior distribution.

#p=[0.2, 0.2, 0.2, 0.2, 0.2]
#colors=['green', 'red', 'red', 'green', 'green']
#measurements = ['red', 'green']
#motions = [1,1]
#sensor_right = 0.6
#(1 - sensor_right) = 0.2
#p_move = 0.8
#pOvershoot = 0.1
#pUndershoot = 0.1

pOvershoot=(1.0-p_move)/2
pUndershoot=pOvershoot

def sense(p, Z):
    if p==[]:
        p=[[1.0 / (len(colors) * len(colors[0]))]*len(colors[0])]*len(colors)
    q=[]
    for i in range(len(colors)): 
        t=[]
        for j in range(len(colors[i])):
            hit = (Z == colors[i][j])
            t.append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
        q.append(t)
    s=0
    for i in range(len(q)): 
        s += sum(q[i])
 #   print s
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= s
    return q

def move(p, U):
    if p==[]:
        p=[[1.0 / (len(colors) * len(colors[0]))]*len(colors[0])]*len(colors)
    q = []
    if U[0]==0:   #move left right
     #   if U[1]==0:return p
        for i in range(len(p)): 
            t=[]
            for j in range(len(p[i])):
                s = p_move * p[i][(j-U[1]) % len(p[i])]
          #      print (j - U[1]) % len(p[i])
           #     s += pOvershoot * p[i][(j-U[1]-1) % len(p[i])]
                s += (1 - p_move) * p[i][(j-U[1]+1) % len(p[i])]
                t.append(s)
            q.append(t)

    elif U[1]==0:  #move up down
        for i in range(len(p)): 
            t=[]
            for j in range(len(p[i])):
                s = p_move * p[(i-U[0]) % len(p)][j]
                #s += pOvershoot * p[(i-U[0]-1) % len(p)][j]
                s += (1-p_move) * p[(i-U[0]+1) % len(p)][j]
                t.append(s)
            q.append(t)
    else:
        raise
    s=0
    for i in range(len(q)): 
        s += sum(q[i])
 #   print s
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] /= s
#    show(q)
    return q

#p = [[0,0,0],[1,0,0]]
#p=move(p,[0,1])
p=[]
for i in range(len(measurements)):
    p=move(p,motions[i])
    p=sense(p,measurements[i])

#p=[]
#colors=[['green','green','green'],
        #['green','red','red'],
        #['green','green','green']]
#measurements=['red', 'red']
#motions=[[0,0],[0,1]]
#sensor_right = 1
#p_move=0.5

##p=[]
##p=sense(p,measurements[0])
##show(p)
#for i in range(len(measurements)):
    #p=move(p,motions[i])
    #print 'after moved:'
    #show(p)
    #p=sense(p,measurements[i])
    #print 'after sense:'
    #show(p)


show(p)
#Your probability array must be printed 
#with the following code.

#show(p)

