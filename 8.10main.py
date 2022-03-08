#Sameerah Mustafa
#ID: 1584330

string = input()
modified = ''.join(string.split(' '))

if(modified == modified[::-1]):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")