from __future__ import division
for i in range(110000):
    remaind=i
    flag=True
    for j in range(6):
        if (remaind-1) % 5 ==0:
            remaind=(remaind-1)/5*4
        else:
            flag = False
            break
    if flag == False:
        continue
    else:
        print i
        break

    #s = i * 5 + 1
    #for j in range(6):
        #s=s*5/4 + 1
        #print s
    #if isinstance(s, int):
        #print s
        #break

