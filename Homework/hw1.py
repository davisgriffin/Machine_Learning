
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

MAE1=MAPE1=MSE1=RMSE1=MAE2=MAPE2=MSE2=RMSE2 = 0

n = len(dining_halls)
for hall in dining_halls.values():
    MAE1 += abs(hall['actual'] - hall['predicted1'])
    MAE2 += abs(hall['actual'] - hall['predicted2'])
    MAPE1 += abs((hall['actual'] - hall['predicted1'])/hall['actual'])
    MAPE2 += abs((hall['actual'] - hall['predicted2'])/hall['actual'])
    MSE1 += (hall['actual'] - hall['predicted1'])**2
    MSE2 += (hall['actual'] - hall['predicted2'])**2
    
MAE1 /= n
MAE2 /= n
MAPE1 = MAPE1/n * 100
MAPE2 = MAPE2/n * 100
MSE1 /= n
MSE2 /= n
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
if wins.count(True) > 2:
    print('Prediction 1 has the better model')
else:
    print('Prediction 2 has the better model')
