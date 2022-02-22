
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


from statsmodels.nonparametric.smoothers_lowess import lowess
from matplotlib import collections as matcoll
from mplot import Mplot

#import warnings
#warnings.filterwarnings('ignore')

# read in data
df = pd.read_stata('http://fmwww.bc.edu/ec-p/data/wooldridge/mroz.dta')

# use a few columns
cols = ['lwage', 'exper', 'expersq', 'educ',  'age', 'kidslt6', 'kidsge6']
df = df[cols]

# droprows with missing data
df = df.dropna(how = 'any')

# fitting the model using statsmodels.formula.api
OLS_model = smf.ols('lwage ~ exper  + educ + age + kidslt6 + kidsge6', data = df).fit()

# Generating plots
for i in range(1,8):
    Mplot(OLS_model, i).plot()