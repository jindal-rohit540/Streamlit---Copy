import pandas as pd
import streamlit as st
import datetime
import pickle

cars_df = pd.read_csv("cars24.csv")

st.write("""

# Cars24 Used car prediction
""")

st.dataframe(cars_df)


## Categorical to Numerical ## gIVEN BY THE MODELLING TEAM 
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


def model_predict(fuel_type, transmission_type ,engine, seats):

    ## Load the model 

    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)

        #year	seller_type	km_driven	fuel_type	transmission_type	mileage	engine	max_power	seats

        input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.3, seats ]]

        return reg_model.predict(input_features)



## Asking as inputs from the user 

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
engine = col1.slider("Set the engine power", 500, 5000, step= 100)

transmission_type  = col2.selectbox("Select the transmission type", ["Manual", "Automatic"])
seats = col2.selectbox("Enter the no of seats", [4,5,6,7,8,9,10,11,12])


if (st.button("Predict Price")):

    used_car_price = model_predict(encode_dict["fuel_type"][fuel_type], encode_dict["transmission_type"][transmission_type] ,engine, seats)
    st.text(f"The price of your car is {used_car_price}")


