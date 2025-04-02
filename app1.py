import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model=joblib.load('loan_dataset1.joblib')
gender=st.number_input('Enter gender Male:0 Female:1')
married=st.number_input('Enter marital status Married:1 Unmarried:0')
income=st.number_input('Enter applicant income in thousands')
la=st.number_input('Enter loan amount in thousands')
if st.button('predict approval'):
    prediction=model.predict([[gender,married,income,la]])
    if prediction=='Y':
        st.text('Loan Approved')
    else:
        st.text('loan Rejected')
