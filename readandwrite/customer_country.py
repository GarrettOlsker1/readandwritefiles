import csv

customers = open("customers.csv", "r")
country_customer = open("customer_country.csv", "w")

readcsv = csv.reader(customers, delimiter=(","))

next(readcsv)

country_customer.write("Name" + ", " + "Country" + "\n")
print()
for row in readcsv:
    country_customer.write(row[1] + " " + row[2] + ", " + row[4] + "\n")

customers.close()
country_customer.close()
