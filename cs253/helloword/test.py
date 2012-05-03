def valid_day(day):
    #if type(day) == type(1):
    try:
        day = int(day)
        return day if day>0 and day<32 else None
    except:
        pass
print valid_day("10")
print valid_day("10,")
