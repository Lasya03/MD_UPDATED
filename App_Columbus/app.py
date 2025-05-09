import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# App title
st.title("Cylinder Cost Prediction")

# Sidebar dropdown
model_names = [
    "HD", "HDE", "HDI", "LD", "LDH",
    "MD", "NR", "H", "L", "M", "N"
]
selected_model = st.sidebar.selectbox("Select Dataset/Model", model_names)

