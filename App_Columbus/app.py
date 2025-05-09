import streamlit as st

# App title
st.title("Cylinder Cost Prediction")

# Sidebar
model_names = [str(i) for i in range(1, 12)]
selected_model = st.sidebar.selectbox("Select Dataset/Model", model_names)

# Layout
col1, col2 = st.columns(2)

# ---------------- Left Column: Sliders + Inputs ---------------- #
with col1:
    st.subheader("Numeric Features")

    feature_config = {
        "A": (0, 100),
        "B": (0, 200),
        "C": (10, 500),
        "D": (1, 50),
    }

    for feature, (min_val, max_val) in feature_config.items():
        slider_key = f"{feature}_slider"
        input_key = f"{feature}_input"

        # Initialize in session_state
        if slider_key not in st.session_state:
            st.session_state[slider_key] = (min_val + max_val) // 2
        if input_key not in st.session_state:
            st.session_state[input_key] = st.session_state[slider_key]

        # Layout
        st.markdown(f"**{feature}**")
        slider_col, input_col = st.columns([3, 1])

        # Create slider
        slider_val = slider_col.slider(
            label=f"{feature} slider",
            min_value=min_val,
            max_value=max_val,
            value=st.session_state[slider_key],
            key=slider_key
        )

        # Create input box
        input_val = input_col.number_input(
            label=f"{feature} input",
            min_value=min_val,
            max_value=max_val,
            value=st.session_state[input_key],
            key=input_key
        )

        # Sync logic
        if st.session_state[slider_key] != st.session_state[input_key]:
            # Update whichever was not just changed
            trigger = st.session_state.get(f"{feature}_trigger", "slider")
            if trigger == "slider":
                st.session_state[input_key] = st.session_state[slider_key]
            else:
                st.session_state[slider_key] = st.session_state[input_key]

        # Track last changed widget
        if slider_val != st.session_state[input_key]:
            st.session_state[f"{feature}_trigger"] = "slider"
        elif input_val != st.session_state[slider_key]:
            st.session_state[f"{feature}_trigger"] = "input"

# ---------------- Right Column: Yes/No Options ---------------- #
with col2:
    st.subheader("Yes/No Features")

    for feature in ["R", "B", "Bl", "VA", "VB"]:
        label_col, select_col = st.columns([1, 2])
        with select_col:
            st.selectbox(
                f"{feature.upper()}",
                ["No", "Yes"],
                key=f"{feature}_select"
            )
