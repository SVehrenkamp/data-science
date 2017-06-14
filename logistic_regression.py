import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import math

loanData = pd.read_csv('data/loansData_clean.csv')

loanData['IR_TF'] = loanData['Interest.Rate'].map(lambda x: 1 if x >= 12 else 0)
loanData['Intercept'] = 1.0

print( loanData[loanData['Interest.Rate'] == 10].head() )

ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

X = loanData[ind_vars]
y = loanData['IR_TF']
logit = sm.Logit(y,X)
result = logit.fit()

coeff = result.params
print(coeff)
def logistic_function(score, amt, coeff):
    FICO = coeff[1]
    AR = coeff[2]
    p = 1/(1 + math.exp(coeff[0] + coeff[1]*score - coeff[2]*amt))
    return p

print(logistic_function(680, 10000, coeff))
