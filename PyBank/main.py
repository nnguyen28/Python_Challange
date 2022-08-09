print ("Financial Analysis")
print (".........................")

import os
import csv 

#creating path
budget_data = os.path.join("C:/Users/nguye/Downloads/PythonResources/Resource/budget_data.csv")

#open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #declaring variables
    profit = []
    months = []
    revenue_change =[]


    #reading data
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    #calculating total length of months
    total_months = len(months)
    print ("Total Months:" + str(total_months))

    #calculating total amount profit/loss
    total_amount = sum(profit)
    print ("Total Amount:" + "$" + str(sum(profit)))

    #calculating revenue change
    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))

    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)
    print ("Average Change:" + "$" + str(revenue_average))

    #greatest increase in revenue
    greatest_increase = max(revenue_change)
    print ("Greatest Increase in Profits:" + str(greatest_increase))

    #greatest decrease in revenue
    greatest_decrease = min(revenue_change)
    print ("Greatest Decrease in Profits:" + str(greatest_decrease))


   



