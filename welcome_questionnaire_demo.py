# import module (library) dependencies so we can use their classes and functions
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# open the CSV file and load its data into a Pandas Dataframe
dataframe = pd.read_csv("/Users/sprint/Google Drive/GU/CPSC 222/Welcome Questionnaire Demo.csv")
print(dataframe)
# remote the identifiable columns
#dataframe = dataframe.drop(["Username", "Last Name", "First Name"], axis=1)
# shuffle the ordering of the rows
dataframe = dataframe.sample(frac=1)
# reset the ordering of the rows to start again from 0
dataframe = dataframe.reset_index(drop=True)
print(dataframe)

# get a sense of the central tendency for the Likert scale questions
print(dataframe["Answer 1"].median()) # programming experience
print(dataframe["Answer 2"].median()) # command line experience
print(dataframe["Answer 3"].median()) # github experience

# create a histogram plot using Matplotlib
plt.hist([dataframe["Answer 1"], dataframe["Answer 2"], dataframe["Answer 3"]], 5, label=["Programming experience", "Command line experience", "Github experience"])
plt.xticks(range(1, 6))
plt.xlabel("Likert Response")
plt.ylabel("Student Count")
plt.legend()
plt.title("CPSC 222 Likert Data")
plt.show()

# test if there is there significantly different command line experience than github experience in the class?
print(stats.ttest_rel(dataframe["Answer 2"], dataframe["Answer 3"]))
