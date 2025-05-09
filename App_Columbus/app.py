import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# App title
st.title("Cylinder Cost Prediction")

# Sidebar dropdown
model_names = ["HD", "HDE", "HDI", "LD", "LDH", "MD", "NR", "H", "L", "M", "N"]
selected_model = st.sidebar.selectbox("Select Dataset/Model", model_names)

# Layout: Two columns for main UI
col1, col2 = st.columns(2)

# ------------------------ Left Column: A–D (Slider + Input) ------------------------ #
with col1:
    st.subheader("Hi")
    
    sliders = {}
    inputs = {}

    feature_config = {
        "Bore": (0, 100),
        "Stroke": (0, 200),
        "RPC": (10, 500),
        "Rod": (1, 50),
    }

    for feature, (min_val, max_val) in feature_config.items():
        st.markdown(f"**{feature.upper()}**")
        slider_col, input_col = st.columns([3, 1])  # Adjust width ratios here
        
        key_slider = f"{feature}_slider"
        key_input = f"{feature}_input"

        # Get initial value
        init_val = (min_val + max_val) // 2

        # Sync slider and input dynamically
        slider_val = slider_col.slider(
            f"{feature} slider", min_val, max_val, init_val,
            key=key_slider, label_visibility="collapsed"
        )
        input_val = input_col.number_input(
            f"{feature} input", min_val, max_val, slider_val,
            key=key_input, label_visibility="collapsed"
        )

        # Override slider with number input if changed
        if input_val != slider_val:
            slider_val = input_val

        sliders[feature] = slider_val
        inputs[feature] = input_val

# ------------------------ Right Column: R, B, Bl, VA, VB (Yes/No) ------------------------ #
with col2:
    st.subheader("")

    yes_no_features = {}
    for feature in ["R bearing", "B bearing", "Block", "Val A", "Val B"]:
        label_col, select_col = st.columns([1, 2])  # Adjust label vs dropdown size
        with select_col:
            yes_no_features[feature] = st.selectbox(
                f"{feature.upper()}", ["No", "Yes"], key=f"{feature}_select"
            )
