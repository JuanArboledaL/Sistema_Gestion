def is_year_leap(year):
#
# Tu código del LABORATORIO 4.3.6.
#
 
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f" Año {year} true")
        return True
    else:
        print(f" Año {year} false")
        return False


def days_in_month(year, month):
#
# Escribe tu código aquí.
#
	if():

	else:


        

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

