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
selected_model = st.sidebar.selectbox("Select Cylinder Type", model_names)

# Layout: Two columns
col1, col2 = st.columns(2)
col_slider, col_input = st.columns([2, 1])  # Wider slider, narrower input

with col1:
    # Define a dictionary to store values
    sliders = {}
    inputs = {}

    # Feature ranges (you can customize ranges here)
    feature_config = {
        "Bore": (0, 100),
        "Stroke": (0, 200),
        "RPC": (10, 500),
        "Rod": (1, 50),
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

    yes_no_features = {}
    for feature in ["R bearing", "B bearing", "Block", "Val A","Val B"]:
        yes_no_features[feature] = st.selectbox(f"{feature.upper()}", ["No", "Yes"])
