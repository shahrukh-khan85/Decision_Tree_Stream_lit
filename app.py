import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("Bank Deposit Prediction app")
# st.help(st.selectbox)
with st.form(key = "form1", clear_on_submit =True):
    df2 = {"Select the option": np.NAN, "Admin":0,"blue-color":1,"entrepreneur":2,"housemaid":3,"management":4,"retired":5,"self-employed":6,"services":7,"student":8,"technician":9,"unemployed":10}
    df3 = {"Select the option": np.NAN,"Divorced":0,"Married":1, "Single":2}
    df4 = {"Select the option": np.NAN,"primary":0,"secondary":1,"tertiary":2}
    df5 = {"Select the option": np.NAN, "No":0,"Yes":1}
    df6 = {"Select the option": np.NAN, "Jan":4,"Feb":3,"Mar":7,"Apr":0,"May":8,"Jun":6,"July":5,"Aug":1,"Sep":11,"Oct":10,"Nov":9,"Dec":2}
    df7 = pd.DataFrame({"Day": range(0,31)})

    age = st.number_input("Enter your age")

    job1 = st.selectbox("Select your job role", df2)
    job = df2[job1]

    mar = st.selectbox("Select your Martial Status", df3)
    marital= df3[mar]

    edu = st.selectbox("Select your highest education level", df4)
    education = df4[edu]

    default = st.selectbox("Have you ever defaulted on loan", df5)
    defa = df5[default]

    balance = st.number_input("Enter your balance")

    housing = st.selectbox("Do you have housing loan", df5)
    house = df5[housing]

    loan = st.selectbox("Have you any loan", df5)
    loans = df5[loan]

    day = st.selectbox("day", df7)

    month = st.selectbox("Enter month", df6)
    mont = df6[month]

    duration = st.number_input("Enter in seconds")

    campaign = st.number_input("Enter number of days")
    pdays = st.number_input("Enter number of pdays")

    previous = st.number_input("Enter number of previous")
        
    submit = st.form_submit_button(label = "Predict")


model = joblib.load("bank.pkl")

result = model.predict([[age, job, marital, education, defa, balance, house,loans,day, mont, duration, campaign, pdays, previous]])
    
if result==1:
    out = "Person will deposit the amount"
else:
    out = "Person will not deposit the amount"

st.title("Predictions")
st.success(out)