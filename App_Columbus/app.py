import streamlit as st

# App title
st.title("Cylinder Cost Prediction")

# Sidebar dropdown
model_names = [str(i) for i in range(1, 12)]
selected_model = st.sidebar.selectbox("Select Dataset/Model", model_names)

# Layout: Two columns for main UI
col1, col2 = st.columns(2)

# ------------------------ Left Column: A–D (Slider + Input) ------------------------ #
with col1:
    st.subheader("Numerical Features")

    feature_config = {
        "A": (0, 100),
        "B": (0, 200),
        "C": (10, 500),
        "D": (1, 50),
    }

    for feature, (min_val, max_val) in feature_config.items():
        key_slider = f"{feature}_slider"
        key_input = f"{feature}_input"

        # Set default session state if not already set
        if key_slider not in st.session_state:
            st.session_state[key_slider] = (min_val + max_val) // 2
        if key_input not in st.session_state:
            st.session_state[key_input] = st.session_state[key_slider]

        # Define callbacks
        def make_slider_callback(feature):
            def callback():
                st.session_state[f"{feature}_input"] = st.session_state[f"{feature}_slider"]
            return callback

        def make_input_callback(feature):
            def callback():
                st.session_state[f"{feature}_slider"] = st.session_state[f"{feature}_input"]
            return callback

        st.markdown(f"**{feature}**")
        slider_col, input_col = st.columns([3, 1])  # Adjust width ratios here

        # Create slider and number input
        slider_col.slider(
            f"{feature} slider", min_val, max_val,
            key=key_slider, label_visibility="collapsed",
            on_change=make_slider_callback(feature)
        )
        input_col.number_input(
            f"{feature} input", min_val, max_val,
            key=key_input, label_visibility="collapsed",
            on_change=make_input_callback(feature)
        )

# ------------------------ Right Column: R, B, Bl, VA, VB (Yes/No) ------------------------ #
with col2:
    st.subheader("Yes/No Features")

    yes_no_features = {}
    for feature in ["R", "B", "Bl", "VA", "VB"]:
        label_col, select_col = st.columns([1, 2])  # Adjust label vs dropdown size
        with select_col:
            yes_no_features[feature] = st.selectbox(
                f"{feature.upper()}", ["No", "Yes"], key=f"{feature}_select"
            )
