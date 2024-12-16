def is_year_leap(year):
    if(year % 400 == 0) or (year % 4 == 0 and year %100!=0):
        print("Año: ",year," ",True)
        return True
    else:
        print("Año: ",year," ",False)
        return False

def days_in_month(year, month):
    #if(month in[1,3,5,7,8,10,12]):
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        days = 31
    elif(month == 2):
        if(is_year_leap(year)):
            days = 29        
        else:
            days = 28      
    #elif(month in[4,6,9,11]):
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        days = 31
    return days


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")