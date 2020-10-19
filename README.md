# Python-Challenge
**Submitted By:** Saloni Gupta\
_Date_: october, 12th, 2020\
Python Homework - **Py Me Up, Charlie**

PyBank and PyPoll
PyBank: Analysis on monthly Profit/Loss data
PyPoll: Analysis on election result
Background\
In this work, I created python scripts for analyzing the financial records of PyBank and the election result of PyPoll.


# Pybank

## Purpose
This python program takes a list of financial records included in budget_data_1.csv and budget_data_2.csv and determines some summary statistics. Each file contains two columns: Date and Revenue. It returns a results file that includes the number of months included, the net revenue, the average change in revenue between months, the date and amount of the greatest increase in revenue, and the date and amount of the greatest decrease in revenue.

## Requirements
It requires python to be installed. Python 3.6.2 was used during development. It utilizes the os, and csv libraries to read the data file and to write the results file. The data is included in the raw_data file contained within the repository.

## Running the Code
to run enter the following into the command line: 
`$ python budget_analyis.py`

## Results
Results can be seen in pybank_results_summary_1.txt and pybank_results_summary_2.txt. <br/>
The results for each file can be seen in <br/>

budget_data_2.csv: <br/>

Financial_Analysis
*************************
Total Months: 86 <br/>
Total: $38382578 <br/>
Average  Change: $-2315.12 <br/>
Greatest Increase in Profits: Feb-2012 ($1926159) <br/>
Greatest Decrease in Profits: Sep-2013 ($-2196167)

PyPoll
Vote_Counting
--------------------
************************
In this work, I created a Python script for analyzing the votes of election result of PyPoll.

With a set of poll data called election_data.csv, the dataset is composed of three columns: Voter ID, County, and Candidate.

Create a Python script that analyzes the votes and calculates each of the following:

-The total number of votes cast

-A complete list of candidates who received votes

-The percentage of votes each candidate won

-The total number of votes each candidate won

-The winner of the election based on popular vote.

Election_Results
*************************
Total Votes: 3521001\
*************************
Khan: 63.000% (2218231)\
Correy: 20.000% (704200)\
Li: 14.000% (492940)\
O'Tooley: 3.000% (105630)\
************************
Winner: Khan
************************
