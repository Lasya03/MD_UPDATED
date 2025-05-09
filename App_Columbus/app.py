import streamlit as st

# App title
st.title("Cylinder Cost Prediction")

# Sidebar dropdown
model_names = [str(i) for i in range(1, 12)]
selected_model = st.sidebar.selectbox("Select Dataset/Model", model_names)

# Layout: Two columns
col1, col2 = st.columns(2)

# ------------------- Left Column: Slider + Input (A–D) ------------------- #
with col1:
    st.subheader("Numerical Features")

    feature_config = {
        "A": (0, 100),
        "B": (0, 200),
        "C": (10, 500),
        "D": (1, 50),
    }

    for feature, (min_val, max_val) in feature_config.items():
        st.markdown(f"**{feature}**")
        slider_col, input_col = st.columns([3, 1])

        # Keys
        slider_key = f"{feature}_slider"
        input_key = f"{feature}_input"

        # Initialize state
        if slider_key not in st.session_state:
            st.session_state[slider_key] = (min_val + max_val) // 2
        if input_key not in st.session_state:
            st.session_state[input_key] = st.session_state[slider_key]

        # If input changed, override slider
        if st.session_state[input_key] != st.session_state[slider_key]:
            st.session_state[slider_key] = st.session_state[input_key]

        # Draw widgets (they update session_state directly)
        slider_col.slider(
            label=feature,
            min_value=min_val,
            max_value=max_val,
            key=slider_key,
            label_visibility="collapsed"
        )
        input_col.number_input(
            label=feature,
            min_value=min_val,
            max_value=max_val,
            key=input_key,
            label_visibility="collapsed"
        )

        # Re-sync input to match slider if slider changed
        if st.session_state[slider_key] != st.session_state[input_key]:
            st.session_state[input_key] = st.session_state[slider_key]

# ------------------- Right Column: Yes/No ------------------- #
with col2:
    st.subheader("Yes/No Features")

    for feature in ["R", "B", "Bl", "VA", "VB"]:
        label_col, select_col = st.columns([1, 2])
        with select_col:
            st.selectbox(f"{feature.upper()}", ["No", "Yes"], key=f"{feature}_select")
