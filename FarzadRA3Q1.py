# A3Q1
# Author: Farzad Rahman
# Date Start: 28/03/20
# ICS3UI - 03, Ms. Harris

"""
I/O Question: Find a data set you are interested in. (If stuck,
go to Environment Canada or U of W weather stats and
download something.) The data set must have at least 100
rows and 10 columns. (or 200 rows and 5 columns). Ask if
your data does not comply before proceeding. Create a
flowchart and IPO chart, then write a program that reads in
your txt or csv or xml file and writes out a summary file
containing averages &amp;/or max and min values for the data set
and whatever other total information is relevant. (Level 3) Additional relevant
stats for a level 4. {IE: Snowfall is not relevant in the summer months if using
weather so an average is fine but does not give a true picture.} You are all
intelligent, I’m sure you can determine what is meaningful and above
expectations for your dataset. Have fun with this. Also, make absolutely sure
you Push the data file to me in GitHub!
"""

# Modifications:
# 31/03/20 - Organized code and created file
# 04/04/20 - Cleared and formatted main function
# 06/04/20 - Added more data analysis points
# 10/04/20 - Debugged and added average
# 11/04/20 - Formatting

# date,location,new_cases,new_deaths,total_cases,total_deaths
# Structure of data for reference

input_file = open('../FarzadRA3Q2/Covid19.csv', "r")     # refers to the data file
output_file = open("Summary.txt", "w+")

# Constants
date = 0
country = 1
new_case = 2
new_death = 3
total_case = 4
total_death = 5


def find_extremes(message, extreme, dataset, all_data=0, country_list=0, date=0):
    """
    To write to the summary file a max or min of data.


    :param message: Message to be written to output file.
    :param extreme: "max" or "min" of dataset.
    :param dataset: the data being searched.
    :param country: the list of countries being searched.
    :param date: list of dates being searched.
    :return: None
    """

    for i in range(len(dataset)):
        if dataset[i] == extreme(dataset):
            if date==0:
                output_file.write(message + str(dataset[i]) + " " + str(all_data[i][country]) + "\n")
            else:
                output_file.write(message + str(dataset[i]) + " " + str(country_list[i]) + "\n")
    

def main():
    output_file.write("Covid 19 vs the world \nSummary File \n \nNot all countries may be reporting accurate results. \n\n \n")

    # Data sets within this data set
    full_list = []
    date_list = []
    country_list = []
    new_case_list = []
    new_death_list = []
    total_case_list = []
    total_death_list = []



    # Read In Data
    for line in input_file:
        line = line.split(",")
        if line[date] == "date":
            continue
        if line[country] == "World":
            continue

        full_list.append(line)
        date_list.append(line[date])
        new_case_list.append(int(line[new_case]))
        new_death_list.append(int(line[new_death]))

        if line[date] != "2020-03-28":
            continue

        country_list.append(line[country])
        total_case_list.append(int(line[total_case]))
        total_death_list.append(int(line[total_death][0:len(line[total_death])-1]))  # Removes the \n from the end.

    find_extremes("Most New Cases in a day: ", max, new_case_list,all_data=full_list)

    find_extremes("Least New Cases in a day: ", min, new_case_list,all_data=full_list)


    find_extremes("Most New Deaths in a day: ", max, new_death_list, all_data=full_list)


    # Finds average total cases of the countries by March 28
    sum_total_cases = 0
    for elem in total_case_list:
        sum_total_cases += elem
    average_total_case = sum_total_cases/len(total_case_list)
    output_file.write("\n \nThere is an average of " + str(round(average_total_case,2)) + "  cases in each country by March 28. \n \n \n")

    find_extremes("Highest Total # of Cases by March 28: ", max, total_case_list, country_list=country_list, date=1)

    find_extremes("Lowest Total # of Cases by March 28: ", min, total_case_list, country_list=country_list, date=2)

    # Finds average total deaths of the countries by March 28
    sum_total_deaths = 0
    for elem in total_death_list:
        sum_total_deaths += elem
    average_total_deaths = sum_total_deaths/len(total_death_list)
    output_file.write("\n \n \nThere is an average of " + str(round(average_total_deaths,2)) + " total deaths in each country by March 28. \n \n \n \n")


    find_extremes("Highest Total # of Deaths by March 28: ", max, total_death_list, country_list=country_list, date=1)

    find_extremes("Lowest Total # of Deaths by March 28: ", min, total_death_list, country_list=country_list, date=1)


    output_file.close()
    input_file.close()


main()







