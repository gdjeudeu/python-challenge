import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    #The total number of months included in the dataset
    counter = 0
    counter_2 = 0
    largest = 0
    smallest = 0
    average = []
    newav = []
    months = []
    for row in csvreader:
        counter = counter + 1
        counter_2 = counter_2+float(row[1])
        average.append(int(row[1]))
        months.append(row[0])
    cur=0
    nxt=0
    l = 0
    s=0
    for i in range(len(average)-1):
        cur=average[i]
        nxt=average[i+1]
      #  print(cur-nxt)
        newav.append(nxt-cur)
        if largest < float(nxt-cur):
            largest = float(nxt-cur)
            l=i+1
        if smallest > float(nxt-cur):
            smallest = float(nxt-cur)
            s=i+1
    finav=round(sum(newav)/len(newav), +2)

    print("Financial Analysis")
    print("----------------------------------------")
    #The net total amount of "Profit/Losses" over the entire period
    print("Total months: " + str(counter) + " months")
    print("Total:  $" + str(counter_2))
    print("Average  Change:  $" + str(finav))
    print("Greatest Increase in Profits: " + months[l] + " ($" + str(largest) +")")
    print("Greatest Decrease in Profits: " + months[s] + " ($" + str(smallest) + ")")

    output_file = os.path.join("pyBank_data.txt")
    with open(output_file, "w", newline="") as datafile:
         datafile.write("Financial Analysis \n")
         datafile.write("----------------------------------------\n")
         #The net total amount of "Profit/Losses" over the entire period
         datafile.write("Total months: " + str(counter) + " months \n")
         datafile.write("Total:  $ " + str(counter_2) + "\ln")
         datafile.write("Average  Change:  $ " + str(finav) + "\n")
         datafile.write("Greatest Increase in Profits: " + months[l] + " ($" + str(largest) +") \n")
         datafile.write("Greatest Decrease in Profits: " + months[s] + " ($" + str(smallest) + ") \n")
