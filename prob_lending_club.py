import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


loansData = pd.read_csv("data/loansData.csv")
loansData.dropna(inplace=True)

# Box Plot
plt.figure()
loansData.boxplot(column="Amount.Requested")
plt.savefig("graphs/loansData.AmountRequested.boxplot.png")

# Hist Plot
plt.figure()
loansData.hist(column="Amount.Requested")
plt.savefig("graphs/loansData.AmountRequested.histogram.png")

# QQ Plot
plt.figure()
graph = stats.probplot(loansData["Amount.Requested"], dist="norm", plot=plt)
plt.savefig("graphs/loansData.AmountRequested.QQ.png")
