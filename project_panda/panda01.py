#!/usr/bin/python3

import pandas as pd
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot

def main():
    # import the data source
    input_file = "movies.xls"
    
    # read each sheets from input file
    movies_sheet1 = pd.read_excel(input_file, sheet_name = 0, index_col=0)
    movies_sheet2 = pd.read_excel(input_file, sheet_name = 1, index_col=0)
    movies_sheet3 = pd.read_excel(input_file, sheet_name = 2, index_col=0)
 
 # concatenate sheets in movies file and create panda dataframe
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # print to ensure concat
    print(movies.shape)
        # export 5 movies from the top dataframe to excel
    movies_sheet1.head(5).to_excel("5movies.xlsx")
    
    movies.drop_duplicates(inplace=True)
    print(movies.shape)

    # sort DataFrame based on Gross Earnings
    sorted_by_IMDB = movies.sort_values(["IMDB Score"], ascending=False)

    # Data is sorted by values in a column
    # display the top 10 movies by Gross Earnings.
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_IMDB.head(10))

    # create a stacked bar graph
    sorted_by_IMDB['IMDB Score'].head(10).plot(kind="barh")
    # save the figure as stackedbar.png
    plot.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')


if __name__ == "__main__":
    main()

