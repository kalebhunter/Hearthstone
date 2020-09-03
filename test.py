hourly_rate = int(input("What is your hourly rate? "))
hours_worked = int(input ("how many hours have you worked this week"))
weekly_wages = hourly_rate * hours_worked

print("Here are your weekly wages",weekly_wages)
annual_salary = weekly_wages * 52
print("your annual salary is", annual_salary)

if annual_salary <= 30000:
    print("you pay lowest tax rate")
else:
    print("you pay high tax rate")



