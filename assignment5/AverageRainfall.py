'''
@author Andrew Cunningham
@date 15 Dec 2024
CSC 500 - Critical Thinking Assignment 4

Part 1:
Write a program that uses nested loops to collect data 
and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. 
The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display 
the number of months, the total inches of rainfall, 
and the average rainfall per month for the entire period.
'''

from collections import defaultdict
import json

class AverageRainfall:
    def __init__(self):
        '''
        initializes an empty dictionary
        usage: 
            key: integer year (with the [0] year being when recording began)
            value: dictionary
                {
                key: month number (between 1 and 12)
                value: rainfall as a float
                }
        '''

        # rainfall_tracker is a dictionary of dictionaries of (int, float) tuples
        # the lambda function creates a factory of default dicts
        self.rainfall_tracker = defaultdict(lambda: defaultdict(float))

    def update_rainfall(self, year, month, rainfall = 0.0):
        '''
        updates an existing value
        inputs a new value
        '''
        # since rainfall_tracker a defaultdict, updating is straightfoward
        self.rainfall_tracker[year][month] = rainfall

    def number_of_months(self):
        """
        Returns the number of months tracked in the tracker
        """
        total_months = 0
        for year, months in self.rainfall_tracker.items():
            total_months += len(months)

        return total_months
    
    def total_rainfall(self):
        '''
        returns the sum of all rainfall values stored in the tracker as a float
        '''
        total = 0.0
        for year, months in self.rainfall_tracker.items():
            for month, rainfall in months.items():
                total += rainfall
        
        return total

    def __str__(self):
        '''
        returns a string of the rainfall tracker without a specific format but more readible in console.
        '''
        output = ""

        for year, months in self.rainfall_tracker.items():
            output += f"{year} , "
            output += json.dumps(months)
            output += "\n"

        return output

def get_rainfall_terminal():
    """
    Builds a rainfall tracker from the terminal
    outputs:
        number of months
        total rainfall
        average rainfall
    Does not do any input verification
    """
    rainfall_tracker = AverageRainfall()
    print("rainfall tracker format {year number (starting at 1), {month[i] (starting at 1), rainfall (float)}}")
    
    # The program should first ask for the number of years. 
    number_of_years = int(input("Number of years: "))

    # The outer loop will iterate once for each year. 
    for year in range(1, number_of_years + 1, 1):
        
        # The inner loop will iterate twelve times, once for each month. 
        for month in range(1, 13, 1):
            
            # Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
            rainfall = float(input(f"How much rain on the {month} of year {year}: "))

            rainfall_tracker.update_rainfall(year, month, rainfall)

    # After all iterations, the program should display 

    count_months = rainfall_tracker.number_of_months()
    total_rainfall = rainfall_tracker.total_rainfall()
    average_rainfall = total_rainfall / count_months

    # the number of months, 
    print(f"months: {count_months}")

    # the total inches of rainfall, 
    print(f"total rainfall: {total_rainfall}")

    # and the average rainfall per month for the entire period.
    print(f"average rainfall: {average_rainfall}")
    

def get_rainfall_test():
    '''
    Helper method to simplify working and debugging
    '''
    rainfall_tracker = AverageRainfall()
    for year in range(1, 2, 1):
        for month in range(1, 13, 1):
            rainfall_tracker.update_rainfall(year, month, 1)

    count_months = rainfall_tracker.number_of_months()
    total_rainfall = rainfall_tracker.total_rainfall()
    average_rainfall = count_months / total_rainfall

    print(rainfall_tracker)
    print(f"months: {count_months}")
    print(f"total rainfall: {total_rainfall}")
    print(f"average rainfall: {average_rainfall}")

if __name__ == '__main__':
    get_rainfall_terminal()