#Sameerah Mustafa
#ID: 1584330
#HW2

#listing month values
def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0
    return month_int

#calling function to enter dates
def main():
    user_string = []
    status = True
    while (status == True):
        user_string.append(input('Please enter date: '))
        if (user_string[-1] == '-1'):
            status = False

    print('\n')
    for strings in user_string:
        if (',' in strings):
            monthString = strings.split(',')[0].split()[0]
            month_int = str(get_month_as_int(monthString))
            date = strings.split(',')[0].split()[1]
            year = strings[-4:]
            final_date = month_int + '/' + date + '/' + year
            print(final_date)
        else:
            pass

        # calling the function


main()