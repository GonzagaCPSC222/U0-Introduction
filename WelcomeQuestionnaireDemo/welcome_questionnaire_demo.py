# import module (library) dependencies so we can use their classes and functions
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# open the CSV file and load its data into a Pandas Dataframe
dataframe = pd.read_csv("welcome_responses_S25.csv")
print(dataframe)
# remove the identifiable columns
# dataframe = dataframe.drop(["Username", "Last Name", "First Name"], axis=1)
# shuffle the ordering of the rows
dataframe = dataframe.sample(frac=1)
# reset the ordering of the rows to start again from 0
dataframe = dataframe.reset_index(drop=True)
# fill with middle value
dataframe.fillna(3, inplace=True) 
dataframe.to_csv("welcome_responses_S25_cleaned.csv")

# get a sense of the central tendency for the Likert scale questions
print("Spring 2025")
for col_name in dataframe.columns:
    print(col_name, "experience median:", dataframe[col_name].median())

# create a Matplotlib figure with 5 axes all in a row
fig, ax = plt.subplots(1, len(dataframe.columns), sharex=True, sharey=True) # one row, four columns
fig.suptitle("CPSC 222 Welcome Questionnaire Likert Data (N=%d)" %(len(dataframe)))
ax[0].set_ylabel("Student Count")
# create one histogram for each question
colors = ["blue", "orange", "green", "red", "purple"]
for i in range(len(dataframe.columns)):
    col_name = dataframe.columns[i]
    values_ser = dataframe[col_name].value_counts().sort_index()
    ax[i].bar(values_ser.index, values_ser, edgecolor="black", facecolor=colors[i])
    ax[i].set_title(col_name)
    ax[i].set_xlabel("Likert Response")
    ax[i].set_xlim([0.5, 5.5])

# set the figure to be nice and wide
fig.set_size_inches(12, 3.5)
plt.tight_layout()
plt.savefig("welcome_likert_hist.png")

# test if there is there significantly different command line experience than github experience in the class?
print("Command line vs Github experience t-test:", stats.ttest_rel(dataframe["Command line"], dataframe["Github"]))

# test if there is a significant difference between skill levels this semester compared to last semester
print()
print("Fall 2022")
dataframe_last_sem = pd.read_csv("welcome_responses_F22_cleaned.csv")
print("Programming experience median:", dataframe_last_sem["Answer 1"].median()) # programming experience
print("Python experience median:", dataframe_last_sem["Answer 2"].median()) # python experience
print("Command line experience median:", dataframe_last_sem["Answer 3"].median()) # command line experience
print("Github experience median:", dataframe_last_sem["Answer 4"].median()) # github experience

print("Programming experience t-test:", stats.ttest_ind(dataframe["Programming (w/o/AI)"], dataframe_last_sem["Answer 1"]))
print("Python experience t-test:", stats.ttest_ind(dataframe["Python"], dataframe_last_sem["Answer 2"]))
print("Command line experience t-test:", stats.ttest_ind(dataframe["Command line"], dataframe_last_sem["Answer 3"]))
print("Github experience t-test:", stats.ttest_ind(dataframe["Github"], dataframe_last_sem["Answer 4"]))


