# app.py
# Streamlit app for Student Performance EDA

import streamlit as st
from main import load_data, get_summary, missing_values
from main import plot_gender_distribution, plot_score_distribution
from main import plot_gender_vs_math, plot_testprep_vs_total
from main import plot_parental_education_vs_total, plot_lunch_vs_total
from main import plot_correlation_heatmap

# -------------------------
# Streamlit App Title
# -------------------------
st.title("📊 Student Performance EDA Dashboard")
st.write("Explore student scores and background information interactively.")

# -------------------------
# Load Dataset
# -------------------------
df = load_data()
st.subheader("Dataset")
st.dataframe(df)

# -------------------------
# Dataset Summary & Missing Values
# -------------------------
st.subheader("Summary Statistics")
st.write(get_summary(df))

st.subheader("Missing Values")
st.write(missing_values(df))

# -------------------------
# Univariate Analysis
# -------------------------
st.subheader("Univariate Analysis")

st.write("**Gender Distribution**")
st.pyplot(plot_gender_distribution(df))

st.write("**Math Score Distribution**")
st.pyplot(plot_score_distribution(df, "math score"))

st.write("**Reading Score Distribution**")
st.pyplot(plot_score_distribution(df, "reading score"))

st.write("**Writing Score Distribution**")
st.pyplot(plot_score_distribution(df, "writing score"))

# -------------------------
# Bivariate Analysis
# -------------------------
st.subheader("Bivariate Analysis")

st.write("**Gender vs Math Score**")
st.pyplot(plot_gender_vs_math(df))

st.write("**Test Preparation Course vs Total Score**")
st.pyplot(plot_testprep_vs_total(df))

st.write("**Parental Level of Education vs Total Score**")
st.pyplot(plot_parental_education_vs_total(df))

st.write("**Lunch Type vs Total Score**")
st.pyplot(plot_lunch_vs_total(df))

# -------------------------
# Multivariate Analysis
# -------------------------
st.subheader("Multivariate Analysis")
st.pyplot(plot_correlation_heatmap(df))

# -------------------------
# Key Insights
# -------------------------
st.subheader("Key Insights")
st.markdown("""
- Students who completed the test preparation course scored higher.  
- Reading and writing scores are strongly correlated.  
- Female students performed better in reading and writing.  
- Math scores show wider variation than reading and writing.  
- Parental education slightly influences total scores.  
- Lunch type (standard vs free/reduced) also shows some effect on performance.
""")

