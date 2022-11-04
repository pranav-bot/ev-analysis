import numpy as  np
import pickle
import pandas as pd

import streamlit as st

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

def prediction(fuel_date,odometer,trip_distance, qunatity, city, motor_way, country_roads, ac, park_heating, ecr_deviation, avg_speed, tire_type, driving_style_moderate, driving_style_normal):
    x2 = np.array([fuel_date,odometer,trip_distance, qunatity, city, motor_way, country_roads, ac, park_heating, ecr_deviation, avg_speed, tire_type, driving_style_moderate, driving_style_normal])
    x2 = x2.reshape(1, -1)
    scaler.fit_transform(x2)
    predictions = model.predict(x2)
    print(predictions)
    return predictions

def main():
    st.title("Consumption Analysis Of Ev's")
    fuel_date = st.date_input("Enter Fuel Date")
    odometer = st.number_input("Enter Odometer value in decimal(KM)")
    trip_distance = st.number_input("Enter Trip Distance in decimal(KM)")
    qunatity = st.number_input("Enter Quantity in decimal(KM)")
    city = st.number_input("Enter If in city or offroad, 0.0 for offroad and 1.0 for City")
    motor_way = st.number_input("Enter If motor way, 0.0 for No and 1.0 for Yes")
    country_roads = st.number_input("Enter If country or road, 0.0 for No and 1.0 for Yes")
    ac = st.number_input("Enter If A/C off or on, 0.0 for Off and 1.0 for On")
    park_heating = st.number_input("Enter If park heating off or on, 0.0 for Off and 1.0 for On")
    ecr_deviation = st.number_input("Enter Ecr Deviation in decimal")
    avg_speed = st.number_input("Average Speed in decimal(Km/h)")
    tire_type = st.number_input("Enter Tyre type, 0.0 for Summer and 1.0 for Winter")
    driving_style_moderate = st.number_input("Enter Driving style moderate or not, 0.0 for Off and 1.0 for On")
    driving_style_normal =  st.number_input("Enter Driving style normal or not, 0.0 for Off and 1.0 for On")
    result  =""
    fuel_date = fuel_date.strftime('%Y%d%m%H%M%S')
    if st.button("Predict"):
        result = prediction(fuel_date,odometer,trip_distance, qunatity, city, motor_way, country_roads, ac, park_heating, ecr_deviation, avg_speed, tire_type, driving_style_moderate, driving_style_normal)
        st.success("The consumption is {} km/h".format(result))

if __name__ == "__main__":
    main()