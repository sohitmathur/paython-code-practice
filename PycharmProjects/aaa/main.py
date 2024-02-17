# year=int(input("enter a year:"))
#
# if (year%4 and year%100 != 0):
#     print("it is not leap year")
# else:
#     print("it is leap year")

# print ("list of month:jan,feb,march,april,may,june,july,aug,sep,oct,nov,dec")
# month=(input("enter a month:"))
# if month in"feb":
#     print("number of days: 28/29")
# elif month in "jan,march,may,july,aug,oct,dec":
#     print("number of days: 31")
# elif month in "april,june,sep,nov":
#     print("no of days: 30")
# else:
#     print("not a month")
per = float(input("enter the per:"))
if per<40:
    print("please try again next year")
elif per>=40 and per<=55:
    print("you are passed with 'C'grade")
elif per>55 and per<=65:
    print("you are passed with 'B'grade")
elif per>65 and per<=75:
    print("you are passed with 'A'grade")
elif per>75 and per<=100:
    print("you are passed with 'A+'grade")
else:
    print("enter valid number")

filename = input("enter a file name:")

if filename.endswith('.pdf'):
    if filename.startwith('copper'):
        print(f
        "prosessing{filename}")
        elif filename.startwith('gold'):
        print(f
        "prosessing{filename}")
        elif filename.startwith('ironore'):
        print(f
        "prosessing{filename}")
        else:
        print("invalid pdf file")
else:
    print("please check file")

sal = int(input("enter a salary:"))
city = input("enter a city name:").lower()
gen = input("enter a gen[M/F]:").lower()

if city == 'pune':
    if gen == 'm':
        bonus = (sal / 100) * 5
        gross_sal = sal + bonus
        print("originl sal before bonus :", sal)
        print("Bonus:", bonus)
        print("total Sal:,gross_sal:")
    else:
        bonus = (sal / 100) * 10
        gross_sal = sal + bonus
        print("original sal before bonas :", sal)
        print("Bonus:", bonus)
        print("total Sal:,gross_sal:")
