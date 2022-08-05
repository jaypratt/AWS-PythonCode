#2.3
grade = 91
if grade > 90:
    print ('Congratulations! Your grade of ', grade, ' earns you an A in this course!')

#2.4
print (27.5 + 2)
print (27.5 - 2)
print (27.5 * 2)
print (27.5 / 2)
print (27.5 // 2)
print (27.5 ** 2)

#2.5
r = 2
pi = 3.14159
diameter = 2 * r
circumference = 2 * pi * r
area = (pi * r)**2  #  There should be white space before and after the operator.
print ('r:  ', r)
print ('pi:  ', pi)
print ('diameter:  ', diameter)
print ('circumference:  ', circumference)
print ('area:  ', area)

#2.6
number = 5

if (number % 2) == 1:
    print ('this number is odd!')
    
if (number % 2) == 0:
    print ('this number is even!')


#2.7
if (1024 % 4) == 0:
    print ('true')

if (2 % 10) == 0:
    print ('also true')

#2.8
print ('number\tsquare\tcube') 
print (0,'\t', 0**2,'\t', 0**3) #  There should be white space before and after the operator.
print (1,'\t', 1**2,'\t', 1**3)
print (2,'\t', 2**2,'\t', 2**3)
print (3,'\t', 3**2,'\t', 3**3)
print (4,'\t', 4**2,'\t', 4**3)
print (5,'\t', 5**2,'\t', 5**3)
