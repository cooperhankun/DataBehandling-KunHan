import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def find_missing_values(name_of_the_file):
    file_missing = name_of_the_file.isnull().sum()
    plt.figure(figsize=(20,5))
    return sns.barplot(x=file_missing[file_missing!=0].index, y=file_missing[file_missing!=0].values)