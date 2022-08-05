print('3.4, @list')
for row in range(2):
    for col in range(7):
        print('@', end="")
    print()
        
print ('\n3.9, number list')
print('Enter a number between 7-10 digits')
number = input()
for a in number:
    print(a)

print('\n3.11, mpg') 
tmiles = 0
tgallons = 0
total = 0
gallons = int(input('Enter the gallons used (-1 to end): '))
while gallons != -1:
    miles = int(input('enter the miles driven: '))
    mpg = miles / gallons
    tmiles += miles
    tgallons += gallons
    print('The miles/gallon for this tank was ', mpg)
    print()
    gallons = int(input('Enter the gallons used (-1 to end): '))
else:
    if tgallons == 0:
        print ('you must enter values to get a total')
    elif tgallons != 0:
        total = tmiles/tgallons
        print('The overall average miles/gallons was ', total)

print('\n3.12, Palindromes')
palindrome = (input('enter a 5 digit number: '))
palcheck = ''
for n in palindrome:
    palcheck = n + palcheck
if palindrome == palcheck:
    print ('this number is a palindrome!')
else:
    print ('this number is not a palindrome :(')
    
print('\n3.14, pi')
pi = 4
m = 1
for i in range(3,5000,2):
    m *= -1
    pi += (4 *m) / i
    print(pi, i)# 3.141 shows up twice when i = 4907
#https://283361150373.signin.aws.amazon.com/console
#https://us-west-1.console.aws.amazon.com/cloud9/ide/ce6b241977ef476ca7d1521e2aefa9d9
