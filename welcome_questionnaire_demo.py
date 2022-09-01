# import module (library) dependencies so we can use their classes and functions
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# open the CSV file and load its data into a Pandas Dataframe
dataframe = pd.read_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire F22.csv")
print(dataframe)
# remove the identifiable columns
# dataframe = dataframe.drop(["Username", "Last Name", "First Name"], axis=1)
# shuffle the ordering of the rows
dataframe = dataframe.sample(frac=1)
# reset the ordering of the rows to start again from 0
dataframe = dataframe.reset_index(drop=True)
print(dataframe)
dataframe.to_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire Cleaned F22.csv")

# get a sense of the central tendency for the Likert scale questions
print("Fall 2022")
print("Programming experience median:", dataframe["Answer 1"].median()) # programming experience
print("Python experience median:", dataframe["Answer 2"].median()) # python experience
print("Command line experience median:", dataframe["Answer 3"].median()) # command line experience
print("Github experience median:", dataframe["Answer 4"].median()) # github experience

# create a histogram plot using Matplotlib
plt.hist([dataframe["Answer 1"], dataframe["Answer 2"], dataframe["Answer 3"], dataframe["Answer 4"]], 5, label=["Programming experience", "Python experience", "Command line experience", "Github experience"])
plt.xticks(range(1, 6))
plt.xlabel("Likert Response")
plt.ylabel("Student Count")
plt.legend()
plt.title("CPSC 222 Likert Data (N=%d)" %(len(dataframe)))
plt.show()

# test if there is there significantly different command line experience than github experience in the class?
print("Command line vs Github experience t-test:", stats.ttest_rel(dataframe["Answer 2"], dataframe["Answer 3"]))

# test if there is a significant difference between skill levels this semester compared to last semester
print()
print("Spring 2022")
dataframe_last_sem = pd.read_csv("/Users/sprint/My Drive/GU/CPSC 222/Welcome Questionnaire Cleaned S22.csv")
print("Programming experience median:", dataframe_last_sem["Answer 1"].median()) # programming experience
print("Python experience median:", dataframe_last_sem["Answer 2"].median()) # python experience
print("Command line experience median:", dataframe_last_sem["Answer 3"].median()) # command line experience
print("Github experience median:", dataframe_last_sem["Answer 4"].median()) # github experience

print("Programming experience t-test:", stats.ttest_ind(dataframe["Answer 1"], dataframe_last_sem["Answer 1"]))
print("Python experience t-test:", stats.ttest_ind(dataframe["Answer 2"], dataframe_last_sem["Answer 2"]))
print("Command line experience t-test:", stats.ttest_ind(dataframe["Answer 3"], dataframe_last_sem["Answer 3"]))
print("Github experience t-test:", stats.ttest_ind(dataframe["Answer 4"], dataframe_last_sem["Answer 4"]))


