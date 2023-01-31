import csv

sales = open("sales.csv", "r")
customer_sales_report = open("customer_sales_report.csv", "w")

csvreader = csv.reader(sales, delimiter=(","))

next(csvreader)

customer_sales_report.write("Customer ID" + "Total" + "\n")
print()

customerID = 250
total = 0

for z in csvreader:
    if int(z[0]) == customerID:
        total = total + float(z[3]) + float(z[4] + float(z[5]))
    elif int(z[0]) != customerID:
        customer_sales_report.write("\t" + str(customerID) + "\t")
        total = 0
        customerID += 1
        total = total + float(z[3]) + float(z[4] + float(z[5]))
    elif customerID == 262:
        StopIteration


sales.close()
customer_sales_report.close()
