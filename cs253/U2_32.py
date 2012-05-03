
def valid_year(year):
    try:
        int_year=int(year)
        return int_year if int_year > 1900 and int_year < 2100 else None
    except:
        return None


# valid_year('0') => None    
# valid_year('-11') => None
# valid_year('1950') => 1950
# valid_year('2000') => 2000

print valid_year('1')
print valid_year('-11')
print valid_year('1950,')
print valid_year('2030')
