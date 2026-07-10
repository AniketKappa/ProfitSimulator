import streamlit as st

st.set_page_config(
    page_title="Live Shrimp Profitability Simulator",
    page_icon="🦐",
    layout="wide"
)

# ---------------------------
# Function
# ---------------------------

def insight(rm, fc, mv, mor, pre, norm):

    x = (rm + fc + 2) / 0.98
    y = ((x + 11) - (rm + 8)) * (mor / (100 - mor))

    z = x + 11 + y

    var_opex = z + 135
    fix_opex = 30 / mv

    total_cost_live = var_opex + fix_opex

    live_profit = (norm + pre) - total_cost_live

    normal_profit = norm - (143 + rm)

    return live_profit, normal_profit


# ---------------------------
# Title
# ---------------------------

st.title("🦐 Live Shrimp Profitability Simulator")

st.markdown("---")

# ---------------------------
# Inputs
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    rm = st.number_input(
        "Raw Material Cost (₹/kg)",
        min_value=0.0,
        value=300.0,
        step=1.0
    )

    fc = st.number_input(
        "Farmer Compensation (₹/kg)",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

    norm = st.number_input(
        "Normal Selling Price (₹/kg)",
        min_value=0.0,
        value=482.0,
        step=1.0
    )

with col2:

    mor = st.slider(
        "Mortality (%)",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        step=0.1
    )

    pre = st.slider(
        "Premium (₹/kg)",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=1.0
    )

    mv = st.slider(
        "Monthly Production Volume (MT)",
        min_value=1.0,
        max_value=500.0,
        value=150.0,
        step=1.0
    )

# ---------------------------
# Calculation
# ---------------------------

live_profit, normal_profit = insight(
    rm,
    fc,
    mv,
    mor,
    pre,
    norm
)

st.markdown("---")

# ---------------------------
# Metrics
# ---------------------------

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Live Shrimp Profit",
        f"₹ {live_profit:.2f}/kg"
    )

with c2:
    st.metric(
        "Normal Shrimp Profit",
        f"₹ {normal_profit:.2f}/kg"
    )

st.markdown("---")

# ---------------------------
# Profitability Messages
# ---------------------------

if live_profit > 0:
    st.success("✅ Live Shrimps Profitable")

else:
    st.error("❌ Live Shrimps NOT Profitable")


# Comparison

if live_profit > normal_profit:

    st.success(
        "🟢 Live Shrimps More Profitable"
    )

elif live_profit < normal_profit:

    st.warning(
        "🟠 Normal Shrimps More Profitable"
    )

else:

    st.info(
        "⚪ Both have equal profitability"
    )