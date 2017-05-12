import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import collections

loansData = pd.read_csv("data/loansData.csv")
loansData.dropna(inplace=True)

freq = collections.Counter(loansData["Open.CREDIT.Lines"])

chi, p = stats.chisquare(list(freq.values()))

print("chi: %s" % chi)
print("p: %s" % p)
