year = int(input("Enter the year : "))
if year % 4 == 0 and year % 100 == 0 and year % 400 != 0 :
    print("평년")
else:
    print('윤년')