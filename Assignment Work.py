# Dileepa Joseph Jayamanne (ID:22031359)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker


def lineplot(dframe, headers):
    """ Function to create a lineplot. Arguments:
        A dataframe with a column "x" and other columns to be taken as y.
        A list containing the headers of the columns to plot is required as 
        headers. Then "lineplot" function will plot multiple lineplots in a 
        single figure.
    """

    plt.figure()
    # Plotting
    for head in headers:
        plt.plot(dframe["Years"], dframe[head], label=head)

    # labelling
    plt.xlabel("Years")
    plt.ylabel("GDP per capita (US $)")
    plt.legend()

    locator = matplotlib.ticker.MultipleLocator(2)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)
    # plt.savefig("lineplot.png")
    plt.show()
    return


GDP_per_capita = pd.read_csv('GDP_Per_Capita.csv')
# calling lineplot with a list of the columns to be plotted.
lineplot(GDP_per_capita, ["India", "Pakistan", "Sri Lanka",
         "Bangladesh", "Maldives", "United Kingdom"])


def pieplot(array, labels, year):
    """ Function to create a piechart. Arguments:
        array with data, the respective labels in as list of string and year 
        to print.
    """

    plt.figure()
    plt.pie(array, labels=labels, textprops={'fontsize': 9}, startangle=50)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
    plt.title("GDP " + str(year))
    # plt.savefig("pie_chart01.png")
    plt.show()
    return


GDP_df = pd.read_csv('GDP.csv')
gdp_2000 = GDP_df.iloc[0, 1:]
gdp_2020 = GDP_df.iloc[-1, 1:]
countries = ["India", "Pakistan", "Sri Lanka",
             "Bangladesh", "Maldives", "United Kingdom"]

pieplot(gdp_2000, countries, 2000)
pieplot(gdp_2020, countries, 2020)


def stacked_bar_plot(dframe, n):
    """ Function to create a stacked bar plot. Arguments:
        drame is the dataframe containing years and other features.
        Choose n to print stacked bars in every n years.
        For e.g. to print bars every 5 years,  choose n = 5
    """
    years = np.array(dframe.iloc[:, 0])
    no_of_years = years.shape[0]
    x = np.arange(years[0], years[-1]+0.01, n)    # Years
    # index to retrieve rural or urban electrity access
    indices = np.arange(0, no_of_years, n)

    Rural_access = np.array(SL_elec.iloc[:, 1])
    Urban_access = np.array(SL_elec.iloc[:, 2])
    y1 = Rural_access[indices]
    y2 = Urban_access[indices]

    # plotting
    plt.figure()
    plt.bar(x, y1, color='r', label="% of Rural Access")
    plt.bar(x, y2, bottom=y1, color='b', label="% of Urban Access")
    plt.xlabel("Years")
    plt.ylabel("Electricity Access of Sri Lanka")
    plt.title("Electricity Population Access Percentage in Sri Lanka")
    plt.legend()
    #plt.savefig("Stacked bar.png")
    plt.show()
    return


SL_elec = pd.read_csv('Sri Lanka_Electricity_Access.csv')
n = 5
stacked_bar_plot(SL_elec, n)
