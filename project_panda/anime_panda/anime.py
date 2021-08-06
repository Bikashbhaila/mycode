#!/usr/bin/python

import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plot

def main():
    # import data source
    input_file ="anime.csv"
    
    # create panda dataframe
    anime = pd.read_csv(input_file, index_col=0)
    print(anime.shape)
    
    # remove duplicates 
    anime.drop_duplicates(inplace=True)
    print(anime.shape) # no dupes found

    # find top 10 anime with highest rating and plot it to chart
    rating_sorted = anime.sort_values(["rating"], ascending=False) 
    
    top10_rated = rating_sorted.head(10)
    print(top10_rated)
    
    top10_rated["votes"].plot(kind="barh")
    plot.savefig("/home/student/static/bar_votes.png", bbox_inches='tight')
    
    # pie chart
    
    


if __name__ == "__main__":
    main()
