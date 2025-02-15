import streamlit as st
from datetime import datetime

# Title of the app
st.title("Price Prediction Calculator")

# Input fields
st.header("Input Data")
start_time = st.text_input("Start Date and Time (YYYY-MM-DD HH:MM)", "2024-02-12 05:00")
start_price = st.number_input("Start Price", value=0.5500, step=0.0001)
end_time = st.text_input("End Date and Time (YYYY-MM-DD HH:MM)", "2024-02-13 03:41")
end_price = st.number_input("End Price", value=0.6225, step=0.0001)
target_time = st.text_input("Target Date and Time (YYYY-MM-DD HH:MM)", "2024-02-14 23:32")

# Convert input strings to datetime objects
start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
target_time = datetime.strptime(target_time, "%Y-%m-%d %H:%M")

# Calculate time differences in hours
total_time = (end_time - start_time).total_seconds() / 3600
target_time_diff = (target_time - start_time).total_seconds() / 3600

# Calculate growth rate per hour
growth_rate = (end_price / start_price) ** (1 / total_time) - 1

# Calculate predicted price
predicted_price = start_price * (1 + growth_rate) ** target_time_diff

# Display the result
st.header("Predicted Price")
st.write(f"Predicted price at {target_time}: **{predicted_price:.4f}**")