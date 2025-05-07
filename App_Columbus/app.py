import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'modelMD.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Cylinder Cost Prediction-Columbus")

# Extract values from session_state
bore = st.session_state["bore"]
stroke = st.session_state["stroke"]
rpc = st.session_state["rpc"]
rod = st.session_state["rod"]

# Convert to DataFrame for model
defaults = pd.DataFrame([{
    'Bore': bore,
    'Stroke': stroke,
    'RPC': rpc,
    'Rod': rod,
}])


for key, default in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = default
    if f"{key}_input" not in st.session_state:
        st.session_state[f"{key}_input"] = default

# Define callbacks
def update_bore_input(): st.session_state["bore_input"] = st.session_state["bore"]
def update_bore_slider(): st.session_state["bore"] = st.session_state["bore_input"]

def update_stroke_input(): st.session_state["stroke_input"] = st.session_state["stroke"]
def update_stroke_slider(): st.session_state["stroke"] = st.session_state["stroke_input"]

def update_rpc_input(): st.session_state["rpc_input"] = st.session_state["rpc"]
def update_rpc_slider(): st.session_state["rpc"] = st.session_state["rpc_input"]

def update_rod_input(): st.session_state["rod_input"] = st.session_state["rod"]
def update_rod_slider(): st.session_state["rod"] = st.session_state["rod_input"]

# Bore
col1, col2 = st.columns([3, 1])
with col1:
    st.slider("Bore", 0.0, 20.0, step=0.1, key="bore", on_change=update_bore_input)
with col2:
    st.number_input(" ", 0.0, 20.0, step=0.1, key="bore_input", on_change=update_bore_slider)

# Stroke
col3, col4 = st.columns([3, 1])
with col3:
    st.slider("Stroke", 0.0, 500.0, step=1.0, key="stroke", on_change=update_stroke_input)
with col4:
    st.number_input("  ", 0.0, 500.0, step=1.0, key="stroke_input", on_change=update_stroke_slider)

# RPC
col5, col6 = st.columns([3, 1])
with col5:
    st.slider("RPC", 0.0, 500.0, step=0.1, key="rpc", on_change=update_rpc_input)
with col6:
    st.number_input("   ", 0.0, 500.0, step=0.1, key="rpc_input", on_change=update_rpc_slider)

# Rod
col7, col8 = st.columns([3, 1])
with col7:
    st.slider("Rod", 0.0, 20.0, step=0.5, key="rod", on_change=update_rod_input)
with col8:
    st.number_input("    ", 0.0, 20.0, step=0.5, key="rod_input", on_change=update_rod_slider)

# Yes/No Inputs (converted to 0/1)
rbearing = st.selectbox("R bearing", ["No", "Yes"])
bbearing = st.selectbox("B bearing", ["No", "Yes"])
block = st.selectbox("Block", ["No", "Yes"])
vala = st.selectbox("Val A", ["No", "Yes"])

# Convert to DataFrame for model
data = pd.DataFrame([{
    'Bore': bore,
    'Stroke': stroke,
    'RPC': rpc,
    'Rod': rod,
    'Bore2': bore ** 2,
    'Bore_RPC': bore * rpc,
    'Bore_Stroke': rpc * stroke,
    'Bore_Rod': bore * rod,
    'R bearing_Y': 1 if rbearing == 'Yes' else 0,
    'B bearing_Y': 1 if bbearing == 'Yes' else 0,
    'Block_Y': 1 if block == 'Yes' else 0,
    'Val A_Y': 1 if vala == 'Yes' else 0
}])

# Predict
pred_log = model.predict(data)[0]
pred_cost = np.expm1(pred_log)

st.subheader(f"Predicted Total Cost: ${pred_cost:.2f}")
