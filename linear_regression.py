import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import statsmodels.api as sm
loanData = pd.read_csv('data/loansData.csv')


# Strip %'s
clean_interest_rates = loanData['Interest.Rate'].map(lambda x: float(x.split('%')[0]))
loanData['Interest.Rate'] = clean_interest_rates

# Strip Months
clean_loan_lengths = loanData['Loan.Length'].map(lambda x: int(x.split(' ')[0]))
loanData['Loan.Length'] = clean_loan_lengths

# Clean FICO range
clean_FICO_range = loanData['FICO.Range'].map(lambda x: x.split('-'))
clean_FICO_range = clean_FICO_range.map(lambda x: [int(n) for n in x])
clean_FICO_range = clean_FICO_range.map(lambda x: x[0])
loanData['FICO.Score'] = clean_FICO_range;

intrate = loanData['Interest.Rate']     # y
fico = loanData['FICO.Score']           # x1
loanamt = loanData['Amount.Requested']  # x2

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())

# plt.figure()
# p = loanData['FICO.Score'].hist()
# a = pd.scatter_matrix(loanData, alpha=0.05, figsize=(10,10), diagonal='hist')
#
# plt.show()
