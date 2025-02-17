import pickle
import numpy as np

def get_prediction(plotnost, modulupr, amount, epoks, tepm, poverkhplotn, smol, shag, plotnostn, mat, ugol):
    print(plotnost)
    print(modulupr)
    print(amount)
    print(epoks)
    print(tepm)
    print(poverkhplotn)
    print(smol)
    print(shag)
    print(plotnostn)
    print(mat)
    print(ugol)


    with open("models/best_linearRegression.pkl","rb") as f:
        model = pickle.load(f)

    with open("models/scaler_x.pkl","rb") as f:
        scaler_x = pickle.load(f)

    with open("models/scaler_y.pkl","rb") as f:
        scaler_y = pickle.load(f)   

    params = np.array([[plotnost], [modulupr], [amount], [epoks], [tepm], [poverkhplotn], [smol], [shag], [plotnostn], [mat], [ugol]]) 
    params = scaler_x.transform(params)  
    y_pred = model.predict(params) 

    return scaler_y.inverse_transform([y_pred])