import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def costFunction(y, h0):
    return sum((h0-y)**2)*(1/(2*len(y)))


df = pd.DataFrame({
    'Model': ['Acura MDX', 'Honda Accord', 'Honda Civic', 'Honda Civic',
              'Nissan Altima', 'Acura MDX', 'Lexus RX350', 'Toyota Prius',
              'Toyota Prius'],
    'Luxury?': [1, 0, 0, 0, 0, 1, 1, 0, 0],
    'Year': [2017, 2017, 2012, 2016, 2016, 2015, 2015, 2014, 2013],
    'MPG': [20, 25, 23, 24, 30, 18, 21, 45, 40],
    'Horsepower': [290, 190, 160, 170, 180, 280, 270, 120, 120],
    'Price': [50000, 25000, 10000, 18000, 25000, 38000, 40000, 28000, 24000]
})

X = df[['Luxury?', 'Year', 'MPG', 'Horsepower']]
y = df['Price']

h1 = X.dot(np.array([1000, 5, 100, 150])) - 15000
h2 = X.dot(np.array([900, 10, 80, 120])) - 10000

cf1 = costFunction(y, h1)
cf2 = costFunction(y, h2)

print(f'''Model 1 Cost Function: {cf1}
Model 2 Cost Function: {cf2}
''')

if cf1 < cf2:
    print("Model 1 is a better fit than model 2.")
else:
    print("Model 2 is a better fit than model 1.")

reg = LinearRegression().fit(X, y)

h3 = X.dot(np.array(reg.coef_)) + reg.intercept_
cf3 = costFunction(y, h3)

if cf3 < cf1 and cf3 < cf2:
    print(f'''
There is a better model:
h_0(x) = {reg.coef_[0]}*x1 + {reg.coef_[1]}*x2 + {reg.coef_[2]}*x3 + {reg.coef_[3]}*x4 + {reg.intercept_}

Its cost function returns {cf3}.
''')
