import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Car Sales Dashboard")

# Data Load
df = pd.read_csv("car_prices.csv")

# Show data
st.subheader("Dataset")
st.write(df.head())

# Brand filter
brand = st.selectbox("Select Car Brand", df['make'].unique())

filtered_data = df[df['make'] == brand]

st.write(filtered_data)


st.subheader("Selling Price Distribution")

fig, ax = plt.subplots()
sns.histplot(df['sellingprice'], bins=30, ax=ax)

st.pyplot(fig)


st.subheader("Top Car Brands")

brand_count = df['make'].value_counts().head(10)

fig, ax = plt.subplots()
brand_count.plot(kind='bar', ax=ax)

st.pyplot(fig)

st.subheader("Odometer vs Selling Price")

fig, ax = plt.subplots()
sns.scatterplot(x='odometer', y='sellingprice', data=df, ax=ax)

st.pyplot(fig)