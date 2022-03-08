#Sameerah Mustafa
#ID: 1584330

inputPassword = input()

result = ''

for x in inputPassword:

    if(x=='i'):
        result+= "!"

    elif(x=='a'):
        result += "@"

    elif (x == 'm'):
        result += "M"

    elif (x == 'B'):
        result += "8"

    elif (x == 'o'):
        result += "."

    else:
        result += x

result += "q*s"

print(result)

