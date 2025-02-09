import pickle
import numpy as np

def get_prediction(plotnost, modulupr, amount, epoks, tepm, poverkhplotn, smol, shag, plotnostn, mat, ugol):

    with open ('models/best_linearRegression.pkl','wb') as f:
        model = pickle.load(f)

    with open ('models/scaler_x.pkl','wb') as f:
        model = pickle.load(f)

    with open ('models/scaler_y.pkl','wb') as f:
        model = pickle.load(f)   

    params = np.array([plotnost], [modulupr], [amount], [epoks], [tepm], [poverkhplotn], [smol], [shag], [plotnostn], [mat], [ugol]) 
    params = scaler_x.transform(params)  
    y_pred = model.predict(params)  

    return scaler_y.inverse_transform([y_pred])