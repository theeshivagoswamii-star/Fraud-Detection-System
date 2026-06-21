import streamlit as st
import pandas as pd
import joblib
model = joblib.load("fraud_detection.pkl")
st.title("Fraud Detection prediction app")
st.markdown("hy man/lady enter the transaction details and use the predict button ")
st.divider()
transaction_type=st.selectbox("Transaction Type",["payment","transfer","cash_out","deposit"])
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance(Sender)",min_value=0.0,value=1000.0)
newbalanceOrgi=st.number_input("New Balance(Sender)",min_value=0.0,value=0.00)
oldbalance=st.number_input("Old Balance",min_value=0.0,value=0.0)
newbalance=st.number_input("New Balance(Reciver)",min_value=0.0,value=0.0)
if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        oldbalanceOrg:oldbalance,
        newbalanceOrig:newbalanceOrig,
        oldbalanceDest:oldbalanceDist
        "newbalanceDest":newbalanceDest
    }])
    prediction=model.predict(input_data)[0]
    st.subheader("Prediction:"{int(prediction)}"")
    if prediction==1:
        st.error("Transaction was successful")
    else:
        st.error("Transaction was not successful")