import pandas as pd
import matplotlib.pyplot as plt

# Enter values below
fileName = "results.csv"

# Program
csvFile = pd.read_csv(fileName)

for columnName in csvFile.columns:
    if columnName == "NodeCount" or columnName == "PathLength":
        continue
    axes = csvFile.boxplot(column=columnName, by="NodeCount")
    plt.ylabel(columnName)
    plt.xlabel("Node Count")
    plt.suptitle("")
    plt.title(columnName + " vs " + "Node Count")
    plt.legend(["Data"])
    plt.savefig("results/" + columnName + ".png")
    
