import os
#os.path.dirname(__file__)
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
print template_dir


#def valid_day(day):
    ##if type(day) == type(1):
    #try:
        #day = int(day)
        #return day if day>0 and day<32 else None
    #except:
        #pass
#print valid_day("10")
#print valid_day("10,")
