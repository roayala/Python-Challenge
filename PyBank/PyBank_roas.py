'''
    PyBank:

Instructions:
From the budget_data.csv, do the following operations and print them in a .txt file:
-The total number of months included in the dataset
-The net total amount of "Profit/Losses" over the entire period
-The average of the changes in "Profit/Losses" over the entire period
-The greatest increase in profits (date and amount) over the entire period
-The greatest decrease in losses (date and amount) over the entire period

'''


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv # Module for reading CSV files


#Open the path with csv library
csvpath = os.path.join('/Users/roas/Projects_Git/Python_Challenge/Resources', 'budget_data.csv')

count = 0
net_total = 0
increase = 0
decrease = 0
inicial = 1
final_val = 0


#Read the file, row by row
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    
    # Read each row of data after the header
    for row in csvreader:
        net_total = net_total + int(row[1])
        count += 1
        inicial_val = int(row[1])
        '''
        Checks the max increase and the min decrease. 
        '''
        if (increase > (final_val - inicial_val)):
            increase = final_val - inicial_val
            mincrease = row[0]
        if (decrease < (final_val - inicial_val)):
            decrease = final_val - inicial_val
            mdecrease = row[0]
        final_val = inicial_val
        
       
        if inicial == 1 :
            valorinicial = int(row[1])
            inicial = 0
        if count == 86:
            valorfinal = int(row[1])

    average = (valorfinal-valorinicial)/(count-1)

    file1 = open('/Users/roas/Projects_Git/Python_Challenge/Resources/PyBank_resume.txt','w+')
    file1.write ("\t \t Financial Analysis\n")
    file1.write("="*80)
    file1.write("\nTotal of number of months analyzed: %s" %(count) )
    file1.write("\nNet total amount: %1.1f" %(net_total) )
    file1.write("\nAverage: %1.2f" %(average) )
    file1.write("\nGreatest increase in profits: %1.1f, from the month of %s" %(-increase, mincrease) )
    file1.write("\nGreatest decrease in losses: %1.1f, from the month of %s\n" %(-decrease, mdecrease) )
    file1.write("="*80)
    file1.close()


    print("\t \t Financial Analysis")
    print("-"*80)
    print("Total of number of months analyzed: %s" %(count))
    print("Net total amount: %1.1f" %(net_total))
    print("Average: %1.2f" %(average))
    print("Greatest increase in profits: %1.1f, from the month of %s" %(increase, mincrease))
    print("Greatest decrease in losses: %1.1f, from the month of %s" %(decrease, mdecrease))
    print("-"*80)
 