def is_year_leap(year):
    if(year % 400 == 0) or (year % 4 == 0 and year %100!=0):
        #print("Año: ",year," ",True)
        return True
    else:
        #print("Año: ",year," ",False)
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
        days = 30
    return days


def day_of_year(year,month,day):

    cont = 0
    if(year < 0 or year > 2024 or month < 1 or month > 12 or day < 1 or day > 31):
        cont = 0
    else:
        cont+=day
        for mes in range(1,month):
            cont += days_in_month( year,mes)
        return cont
    

dias = day_of_year(2000, 12, 32)

print(f"El número de dia es: {dias}")

