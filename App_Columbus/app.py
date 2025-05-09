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
st.subheader(f"Enter input features:")

# Layout: Two columns
col1, col2 = st.columns(2)

# ------------------------ Left Column: a, b, c, d ------------------------ #
with col1:
    st.markdown("### Numeric Features (a–d)")
    
    # Define a dictionary to store values
    sliders = {}
    inputs = {}

    # Feature ranges (you can customize ranges here)
    feature_config = {
        "a": (0, 100),
        "b": (0, 200),
        "c": (10, 500),
        "d": (1, 50),
    }

    for feature, (min_val, max_val) in feature_config.items():
        st.markdown(f"**{feature.upper()}**")
        col_slider, col_input = st.columns([2, 1])
        
        # Create a key for synchronization
        key_slider = f"{feature}_slider"
        key_input = f"{feature}_input"

        # Initialize slider
        sliders[feature] = col_slider.slider(
            f"{feature} slider", min_val, max_val, (min_val + max_val) // 2, key=key_slider, label_visibility="collapsed"
        )
        
        # Initialize number input linked to slider
        inputs[feature] = col_input.number_input(
            f"{feature} input", min_val, max_val, sliders[feature], key=key_input, label_visibility="collapsed"
        )

        # Sync values
        if inputs[feature] != sliders[feature]:
            sliders[feature] = inputs[feature]
        else:
            inputs[feature] = sliders[feature]

# ------------------------ Right Column: e, f, g, h ------------------------ #
with col2:
    st.markdown("### Yes/No Features (e–h)")

    yes_no_features = {}
    for feature in ["e", "f", "g", "h"]:
        yes_no_features[feature] = st.selectbox(f"{feature.upper()}", ["Yes", "No"])



