import pickle
import numpy as np

def get_prediction(plotnost, modulupr, amount, epoks, tepm, poverkhplotn, smol, shag, plotnostn, mat, ugol):



    with open("best_linearRegression.pkl","rb") as f:
        model = pickle.load(f)
   

    with open("scaler_x.pkl","rb") as f:
        scaler_x = pickle.load(f)
    

    with open("scaler_y.pkl","rb") as f:
        scaler_y = pickle.load(f)  
   
        
    temp = [plotnost, modulupr, amount, epoks, tepm, poverkhplotn, smol, shag, plotnostn, mat, ugol]
    params = np.array([temp]) 
   
    params = scaler_x.transform(params)  
    
    y_pred = model.predict(params) 
    

    return scaler_y.inverse_transform(y_pred)