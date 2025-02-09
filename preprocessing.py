import pickle
import numpy as np

def get_prediction(plotnostn):
    with open ('models/best_linearRegression.pkl','wb') as f:
        model = pickle.load(f)

    with open ('models/scaler_x.pkl','wb') as f:
        model = pickle.load(f)

    with open ('models/scaler_y.pkl','wb') as f:
        model = pickle.load(f)   

    params = np.array([[plotnostn]]) 
    params = scaler_x.transform(params)  
    y_pred = model.predict(params)  

    return scaler_y.inverse_transform([y_pred])