print ("Election Results")
print ("...................................")

import os
import csv 

#creating path
election_data = os.path.join("C:/Users/nguye/Downloads/PythonResources/PyPoll/Resources/election_data.csv")

#open and read csv
with open(election_data, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)

  #Declaring variables
  ballot = []
  county = []
  candidates = []

  Charles = []
  Charles_votes = 0

  Diana = []
  Diana_votes = 0

  Raymon = []
  Raymon_votes = 0

  #reading data
  for row in csvreader:
    ballot.append(int(row[0]))
    county.append(row[1])
    candidates.append(row[2])

  #calculate total vote
  total_votes = (len(ballot))
  print ("Total Vote:" + str(total_votes))

  #list of candidate who receive vote
  for candidate in candidates:

   if candidates == "Charles_casper_Stockham"
      Charles.append(candidates)
      Charles_votes = len(Charles)

    elif candidates == "Diana_DeGette"
      Diana.append(candidates)
      Diana_votes = len(Diana)
      
    else:
      Raymon.append(candidates)
      Raymon_votes = len(Raymon)

  #percentage of each vote
  Charles_percent = ((((Charles_votes/total_votes)*100)/3))
  Diana_percent = ((((Diana_votes/total_votes)*100)/3))
  Raymon_percent = ((((Raymon_votes/total_votes)*100)/3))

  print ("...................................")

  print ("Charles Casper Stockham:" + str(Charles_percent) + str(Charles_votes))
  print ("Diana DeGette:" + str(Diana_percent) + str(Diana_votes))
  print ("Raymon Anthony Doane:" + str(Raymon_percent) + str(Raymon_votes))
  print ("...................................")

  print ("Winner:")


      


