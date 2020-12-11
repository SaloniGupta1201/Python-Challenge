# Python-Challenge
**Submitted By:** Saloni Gupta\
_Date_: october, 12th, 2020\
Python Homework - **Py Me Up, Charlie**

PyBank and PyPoll</br>
PyBank: Created python scripts for analyzing the financial records of PyBank like monthly Profit/Loss data.</br>
PyPoll: created python scripts for analyzing the election result of PyPoll.</br>

# Pybank

## Purpose
This python program takes a list of financial records included in Budget_data.csv and determines some summary statistics. Each file contains two columns: Date and Profits/Losses. It returns a results file that includes the number of months included, the net revenue, the average change in revenue between months, the date and amount of the greatest increase in revenue, and the date and amount of the greatest decrease in revenue.

## Requirements
It requires python to be installed. Visual Studio Code 1.49.3 was used during development. It utilizes the os, and csv libraries to read the data file and to write the results file. The data is included in the Resources file contained within the repository.

## Results
Results can be seen in PyBank/analysis folder pybank_analysis.txt <br/>

Financial_Analysis

Total Months: 86 <br/>
Total: $38382578 <br/>
Average  Change: $-2315.12 <br/>
Greatest Increase in Profits: Feb-2012 ($1926159) <br/>
Greatest Decrease in Profits: Sep-2013 ($-2196167)


# PyPoll

## Purpose
This python program takes a list of votes included in Election_data.csv and determines election results. The file contains three columns: Voter ID, County, and Candidate. It outputs a results file that includes the percentage of votes received, and total number of votes received for each candidate. The results file also specifies the winner.

## Requirements
Running this file requires python to be installed. Visual Studio Code 1.49.3 was used during development. This program utilizes the os, and csv libraries to read the data file and to write the results file. The data is included in the Resources file contained within the repository.

## Results
Results can be seen in pypoll_analysis.txt
Khan won the second election with 2218231 votes which constituted about 63% of the total votes.

Election_Results

Total Votes: 3521001 <br/>
Khan: 63.000% (2218231) <br/>
Correy: 20.000% (704200) <br/>
Li: 14.000% (492940) <br/>
O'Tooley: 3.000% (105630) <br/>

Winner: Khan

