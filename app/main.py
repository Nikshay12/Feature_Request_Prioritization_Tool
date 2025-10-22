import streamlit as st
import pandas as pd
from scoring import calculate_priority
from visualize import plot_priority

st.title("🧩 Feature Request Prioritization Tool")
st.write("Prioritize product features based on Impact, Feasibility, Value, and Urgency.")

uploaded_file = st.file_uploader("Upload feature request CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    prioritized_df = calculate_priority(df)
    
    st.subheader("Prioritized Features")
    st.dataframe(prioritized_df)
    
    st.subheader("Visualization")
    plt = plot_priority(prioritized_df)
    st.pyplot(plt)
else:
    st.info("Please upload a CSV file to begin.")
