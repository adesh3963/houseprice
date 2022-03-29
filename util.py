import json
import pickle
import numpy as np

__location= None
__data_columns= None
__model= None
__loaded_scaler= None

def get_estimated_price(total_sqft,bath,balcony,bhk,location):
    arr_input= np.zeros(len(__data_columns))
    arr_input[0]= total_sqft
    arr_input[1]= bath
    arr_input[2]= balcony
    arr_input[3]= bhk
    
    
    
    try:
        loc_idx= __data_columns.index(location.lower())
    except:
        loc_idx= -1
    if loc_idx >=0:
        arr_input[loc_idx]=1
    
    arr_input= arr_input.reshape(1,-1)
    
    arr_input= __loaded_scaler.transform(arr_input)
    


    return round(__model.predict(arr_input)[0],2)


def get_location_names():
    print("hey util location")
    return __location


def load_save_artifacts():
    print("loading saved artifacts...")
    global __data_columns
    global __location
    global __model
    global __loaded_scaler
    with open("./artifacts/columns.json","rb") as f:
        __data_columns=json.load(f)["data_column"]
        __location=__data_columns[4:]

    with open("./artifacts/linear_model.pkl","rb") as f:
        __model= pickle.load(f)

    with open("./artifacts/scaler.pkl","rb") as f:
        __loaded_scaler= pickle.load(f)

    
    print("loading artifacts done..")
if __name__ == "__main__":
    load_save_artifacts()
    get_location_names()
    # print(get_estimated_price(1500,3,2,3,"1st Phase JP Nagar"))
    # print(get_estimated_price(1000,3,2,5,"1st Phase JP Nagar"))
    # print(get_estimated_price(1000,3,2,3,"Kalhalli"))