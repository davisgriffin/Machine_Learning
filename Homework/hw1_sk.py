from sklearn.metrics import mean_absolute_error as MAE
from sklearn.metrics import mean_absolute_percentage_error as MAPE
from sklearn.metrics import mean_squared_error as MSE

dining_halls = {
    "Dougherty": {
        "actual": 4.5,
        "predicted1": 4.7,
        "predicted2": 3.9,
    },
    "Exchange": {
        "actual": 4.7,
        "predicted1": 4.3,
        "predicted2": 4.5,
    },
    "HG_CEER": {
        "actual": 4.3,
        "predicted1": 4.6,
        "predicted2": 4.4,
    },
    "Belle_Air": {
        "actual": 4.5,
        "predicted1": 4.9,
        "predicted2": 4.2,
    },
    "Freshens": {
        "actual": 3.9,
        "predicted1": 3.9,
        "predicted2": 4.7,
    },
    "HG_Conn": {
        "actual": 4.8,
        "predicted1": 4.1,
        "predicted2": 4.2,
    },
    "Driscoll": {
        "actual": 4.7,
        "predicted1": 4.2,
        "predicted2": 4.3,
    },
    "HG_Falvey": {
        "actual": 4.1,
        "predicted1": 4.4,
        "predicted2": 4.4,
    },
}

actual, predicted1, predicted2 = list(zip(*[ (hall['actual'], hall['predicted1'], hall['predicted2']) for hall in dining_halls.values()]))

MAE1 = MAE(actual, predicted1)
MAE2 = MAE(actual, predicted2)
MAPE1 = MAPE(actual, predicted1)*100
MAPE2 = MAPE(actual, predicted2)*100
MSE1 = MSE(actual, predicted1)
MSE2 = MSE(actual, predicted2)
RMSE1 = MSE1**.5
RMSE2 = MSE2**.5

print(f'''
MAE Prediction 1 = {MAE1}
MAPE Prediction 1 = {MAPE1}%
MSE Prediction 1 = {MSE1}
RMSE Prediction 1 = {RMSE1}
MAE Prediction 2 = {MAE2}
MAPE Prediction 2 = {MAPE2}%
MSE Prediction 2 = {MSE2}
RMSE Prediction 2 = {RMSE2}
''')

# evalute on which has the least error in the most cases
# if tied, prioritize MSE
wins = [MAE1 < MAE2, MAPE1 < MAPE2, MSE1 < MSE2, RMSE1 < RMSE2]
p1Count = wins.count(True)
if p1Count > 2 or (p1Count == 2 and wins[2]):
    print('Prediction 1 has the better model')
else:
    print('Prediction 2 has the better model')

print('\n---------------------------------- QUESTION 2 ----------------------------------')

actual = [20, 100, 300]
predicted1 = [20, 80, 300]
predicted2 = [60, 80, 270]

print(f'''
Actual Values: {actual}
Model 1 Predictions: {predicted1}
Model 2 Predictions : {predicted2}
''')

MAE1 = MAE(actual, predicted1)
MSE2 = MAE(actual, predicted2)
MAPE1 = MAPE(actual, predicted1)
MAPE2 = MAPE(actual, predicted2)

print(f'''
MAE Prediction 1:  {MAE1}
MAPE Prediction 1: {MAPE1*100}%
MAE Prediction 2:  {MAE2}
MAPE Prediction 2: {MAPE2*100}%

Model 1 has a much higher mean absolute error than model 2 and yet model 2 has
the higher mean absolute percentage error. With this case in mind, it cannot be
said that lower mean absolute error always means lower mean absolute percentage
error.
''')