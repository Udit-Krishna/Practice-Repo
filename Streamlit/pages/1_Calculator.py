import streamlit as st
import pandas as pd

st.title("Loan Repayment Calculator")

st.write("### Input Data")
principle_amount = st.number_input("Principal Amount", min_value=0, max_value=100_000_000_000)
col1, col2 = st.columns(2)
rate_of_interest = col1.number_input("Rate of Interest", min_value=0.0, max_value=100.0, step=0.1)
months = col2.number_input("Number of Months", min_value=1, max_value=100_000)

simple_interest = principle_amount*rate_of_interest*(months/12) / 100
compound_interest = (principle_amount * ((1 + (rate_of_interest*0.01)) ** (months/12))) - principle_amount

st.write("### Interest Amount")
col1, col2 = st.columns(2)
col2.metric(label="Simple Interest", value=f"{simple_interest:,.2f}")
col1.metric(label="Compound Interest", value=f"{compound_interest:,.2f}")
interest = pd.DataFrame(
    [["Simple Interest" , round(simple_interest,2)],["Compound Interest", round(compound_interest,2)]], columns=["Interest Type", "Interest Amount"]
).set_index("Interest Type")
st.bar_chart(interest)
