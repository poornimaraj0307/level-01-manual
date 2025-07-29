print("Poorni International [p] ltd")
print("no 24,Anna Nagar, chennai")
print("------------------------------")
print("Employee payroll system")
print("-------------------------------")
no=int(input("Enter the employee id:"))
name=input("Enter the employee name:")
salary=int(input("enter the salary:"))
print("INCOME")
bonus=salary*20/100
print("bonus 20% is:",bonus)
overtime=salary*10/100
print("overtime 10% is:",overtime)
travelallowance=salary*5/100
print("travel allowance 5% is:",travelallowance)
grosspay=salary+overtime+travelallowance+bonus
print("grosspay in rupees:",grosspay)
