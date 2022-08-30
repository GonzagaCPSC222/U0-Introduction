# import module (library) dependencies so we can use their classes and functions
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# open the CSV file and load its data into a Pandas Dataframe
dataframe = pd.read_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire S22.csv")
print(dataframe)
# remove the identifiable columns
# dataframe = dataframe.drop(["Username", "Last Name", "First Name"], axis=1)
# shuffle the ordering of the rows
dataframe = dataframe.sample(frac=1)
# reset the ordering of the rows to start again from 0
dataframe = dataframe.reset_index(drop=True)
print(dataframe)
dataframe.to_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire Cleaned S22.csv")

# get a sense of the central tendency for the Likert scale questions
print("Spring 2022")
print("Programming experience median:", dataframe["Answer 1"].median()) # programming experience
print("Command line experience median:", dataframe["Answer 2"].median()) # command line experience
print("Github experience median:", dataframe["Answer 3"].median()) # github experience

# create a histogram plot using Matplotlib
plt.hist([dataframe["Answer 1"], dataframe["Answer 2"], dataframe["Answer 3"]], 5, label=["Programming experience", "Command line experience", "Github experience"])
plt.xticks(range(1, 6))
plt.xlabel("Likert Response")
plt.ylabel("Student Count")
plt.legend()
plt.title("CPSC 222 Likert Data (N=%d)" %(len(dataframe)))
plt.show()

# test if there is there significantly different command line experience than github experience in the class?
print("Command line vs Github experience t-test:", stats.ttest_rel(dataframe["Answer 2"], dataframe["Answer 3"]))

# test if there is a significant difference between skill levels this year compared to last semester
print()
print("Fall 2021")
dataframeF21 = pd.read_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire Cleaned F21.csv")
print("Programming experience median:", dataframeF21["Answer 1"].median()) # programming experience
print("Command line experience median:", dataframeF21["Answer 2"].median()) # command line experience
print("Github experience median:", dataframeF21["Answer 3"].median()) # github experience

print("Programming experience t-test:", stats.ttest_ind(dataframe["Answer 1"], dataframeF21["Answer 1"]))
print("Command line experience t-test:", stats.ttest_ind(dataframe["Answer 2"], dataframeF21["Answer 2"]))
print("Github experience t-test:", stats.ttest_ind(dataframe["Answer 3"], dataframeF21["Answer 3"]))


