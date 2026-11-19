import streamlit as st

st.title("📦 Streamlit Elements Demo")
st.write("Welcome! Try out a few Streamlit elements below.")

# Text input and greeting
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Demand inputs
daily_demand = st.slider("Daily demand", min_value=0, max_value=100, value=50)
days = st.number_input("Days", min_value=1, max_value=30, value=7, step=1)

total_demand = daily_demand * days
st.metric("Total demand", f"{total_demand:,}")

# Product selection
product = st.selectbox("Pick a product", ["Widget", "Gadget", "Gizmo"])
st.write(f"Selected product: **{product}**")

# Cumulative demand chart
if st.checkbox("Show cumulative demand chart"):
    chart_data = {
        "Day": list(range(1, days + 1)),
        product: [daily_demand * d for d in range(1, days + 1)],
    }
    st.line_chart(chart_data, x="Day", y=product)

# Balloons
if st.button("Celebrate 🎈"):
    st.balloons()
