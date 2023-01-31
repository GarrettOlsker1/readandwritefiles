import csv

employee_bonus = open("EmployeePay.csv", "r")

readcsv = csv.reader(employee_bonus, delimiter=(","))

next(readcsv)
print("ID", "EmpFName", "EmpLName", "Salary", "Bonus")

for row in readcsv:
    print(row[0], row[1], row[2], row[3], row[4])


employee_bonus.close
