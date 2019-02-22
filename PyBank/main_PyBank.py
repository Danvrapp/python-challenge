# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:16:47 2019

@author: Dan
"""

#Initialize all variables
rec_count = 0
profit = 0
temp_value = 0
prof_loss = 0
changes = []
chg_tot = 0
max = 0
max_month = ''
min_month = ''
months = []
min = 0

#open the file
data_file = open('HW_Bank.csv', 'rt')

#read one record from the file
record = data_file.readline()

#while there continue to be records in the file
while True:
    
#read and count a record and 
    record = data_file.readline()
    rec_count += 1

#Get the record into a list, separated into "month" and "Profit or loss"
    line_data = record.rpartition(',')
    month = line_data[0]    
    prof_loss = line_data[2]
        
    #If not EOF
    if prof_loss != "":            
        prof_loss = int(prof_loss)        
        #Add to total sum of profits/losses
        profit = profit + prof_loss
        #Calculate the change from previous month...except for month 1
        if rec_count > 0:
            changes.append(prof_loss - temp_value)
            months.append(month)             
        temp_value = int(prof_loss)
    #If EOF
    if not record:   
        #Subtract out the last, blank, record from total
        rec_count -= 1
        break        

#Loop to get sum of chnages, and find max & min changes
for files in range(len(changes)):
    #Add to running sum of total change amount
    if files > 0:
        chg_tot += changes[files]        
    #If a new max is found
    if changes[files] > max:
            max = changes[files]
            max_month = months[files]
    #If a new min is found
    if changes[files] < min:
            min = changes[files]
            min_month = months[files]

#Calculate Average change 
chg_tot = chg_tot / (rec_count - 1)

#Close the file
data_file.close()

#Print results to screen
print ("\n", "\n")
print("Financial analysis:")
print("------------------------------")
print("Total months: ", rec_count)
print ("Profit is: $",profit)
print("Average change: $", "%0.2f" %chg_tot)
print("Greatest increase: ", max_month, "$", "%0.0f" %max)
print("Greatest decrease: ", min_month, "$", "%0.0f" %min)

file_out = open('PY_Bank_Data.txt', 'wt')
print("Financial analyisis:", file=file_out)
print("------------------------------", file=file_out)
print("Total months: ", rec_count, file=file_out)
print ("Profit is: $",profit, file=file_out)
print("Average change: $", "%0.2f" %chg_tot, file=file_out)
print("Greatest increase: ", max_month, "$", "%0.0f" %max, file=file_out)
print("Greatest decrease: ", min_month, "$", "%0.0f" %min, file=file_out)

file_out.close()