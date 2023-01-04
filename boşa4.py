#Load the file 'exchange_rates.csv'. Find the exchange rate for Great British Pounds with the symbol GBP, and enter the numeric value.

import csv

with open('exchange_rates.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'GBP':
            print(row[1])

#Use the function extract(), and print the first 5 rows of the output.

import csv

def extract(filename, symbol):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == symbol:
                return row[1]

print(extract('exchange_rates.csv', 'GBP'))

#Use the function transform(), and print the first 5 rows of the output

import csv

def extract(filename, symbol):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == symbol:
                return row[1]
            
def transform(exchange_rate):
    return 1 / float(exchange_rate)

print(transform(extract('exchange_rates.csv', 'GBP')))





