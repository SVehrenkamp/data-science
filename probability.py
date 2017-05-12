import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

test_data = x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#Frequency of data
c = collections.Counter(test_data)
test_sum = sum(c.values())

for k,v in c.items():
    print("The frequency of number %s is %s" % (k, float(v)/test_sum))

#box plot
plt.figure()
plt.boxplot(test_data)
plt.savefig("graphs/boxplt.png")

#histogram
plt.figure()
plt.hist(test_data, histtype='bar')
plt.savefig("graphs/hist.png")

plt.figure()
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("graphs/qq.png")
