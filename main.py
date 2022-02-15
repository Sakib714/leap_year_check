"""
Leap Year Check

If a year divided by 4 is a leap year but

if the same year divided by 100 then it need to also divided by 400 to qualify for leap year

"""
print('Enter a year to check if it\'s a leap year!\n' )

year = int(input("Enter Year: "))

if year%4 == 0:
    if year%100:
        if year%400:
            print('It\'s a Leap Year!')
        print('Not a leap year!')
    print('It\'s a Leap Year!')   
else:
    print('Not a Leap Year!')