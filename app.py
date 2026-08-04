import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ==========================================
# Load Trained Pipeline
# ==========================================

pipeline = joblib.load("models/house_price_pipeline.pkl")

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏡",
    layout="wide"
)
# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:2rem;
}

.big-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#1E3A8A;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:#555;
}

.card{

    background:white;

    padding:20px;

    border-radius:15px;

    box-shadow:0px 5px 15px rgba(0,0,0,0.08);

    margin-bottom:20px;

}

.prediction-card{

    background:linear-gradient(90deg,#2563eb,#1d4ed8);

    padding:25px;

    border-radius:15px;

    color:white;

    text-align:center;

}

.footer{

    text-align:center;

    color:gray;

    font-size:14px;

    margin-top:50px;

}

</style>
""", unsafe_allow_html=True)
# ==========================================
# Hide Streamlit Menu
# ==========================================

hide_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# ==========================================
# Sidebar
# ==========================================

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        font-size:90px;
        margin-top:10px;
        margin-bottom:10px;
    ">
        🏡
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("California House Price Predictor")

st.sidebar.markdown("---")

st.sidebar.success("Machine Learning Pipeline")

st.sidebar.write("✅ Ridge Regression")

st.sidebar.write("✅ OneHot Encoding")

st.sidebar.write("✅ Standard Scaling")

st.sidebar.write("✅ Streamlit")

st.sidebar.markdown("---")

st.sidebar.metric("Model Accuracy","62.5%")

st.sidebar.metric("RMSE","70,066")

st.sidebar.markdown("---")

st.sidebar.caption("Developed by Sahil Nabi")

# ==========================================
# Main Title
# ==========================================

st.markdown("""
<div style="background:linear-gradient(90deg,#2563eb,#1e40af);
padding:35px;
border-radius:18px;
color:white;
text-align:center;
margin-bottom:30px;">

<h1 style="font-size:48px;">
🏡 California House Price Predictor
</h1>

<h3>
Estimate California House Prices using a Machine Learning Pipeline
</h3>

</div>
""", unsafe_allow_html=True)

st.markdown(
"""
Predict the **estimated market value** of a California house using Machine Learning.
"""
)

st.markdown("---")

st.subheader("🏠 Property Details")

st.write(
"Fill in the information below to estimate the market value of the property."
)

# ==========================================
# Input Fields
# ==========================================

col1, col2 = st.columns(2)

with col1:

    longitude = st.number_input(
        "Longitude",
        min_value=-124.35,
        max_value=-114.31,
        value=-118.24,
        step=0.01
    )

    latitude = st.number_input(
        "Latitude",
        min_value=32.54,
        max_value=41.95,
        value=34.05,
        step=0.01
    )

    housing_median_age = st.number_input(
        "Housing Median Age",
        min_value=1,
        max_value=52,
        value=25
    )

    total_rooms = st.number_input(
        "Total Rooms",
        min_value=2,
        max_value=40000,
        value=2500,
        step=100
    )

with col2:

    total_bedrooms = st.number_input(
        "Total Bedrooms",
        min_value=1,
        max_value=7000,
        value=500,
        step=50
    )

    population = st.number_input(
        "Population",
        min_value=3,
        max_value=40000,
        value=1200,
        step=100
    )

    households = st.number_input(
        "Households",
        min_value=1,
        max_value=7000,
        value=450,
        step=10
    )

    median_income = st.number_input(
        "Median Income",
        min_value=0.5,
        max_value=15.0,
        value=6.5,
        step=0.1
    )

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "NEAR BAY",
        "ISLAND"
    ]
)
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# Prediction
# ==========================================

if st.button("🏠 Predict House Price", use_container_width=True):

    input_df = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })

    with st.spinner("🤖 AI Model is predicting..."):
        prediction = pipeline.predict(input_df)[0]

    st.markdown("---")

    st.markdown(f"""
<div style="
background: linear-gradient(90deg,#16a34a,#22c55e);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
">

<h2>💰 Estimated House Price</h2>

<h1 style="font-size:55px;">
${prediction:,.0f}
</h1>

</div>
""", unsafe_allow_html=True)

    st.progress(min(prediction / 500000, 1.0))

    if prediction < 150000:
        st.info("🏠 Budget Property")

    elif prediction < 350000:
        st.success("🏡 Mid-range Property")

    else:
        st.warning("🌟 Premium Property")

    st.balloons()
    st.subheader("📈 Price Gauge")

    max_price = 500000

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(prediction),
        number={"prefix": "$"},
        gauge={
            "axis": {"range": [0, max_price]},
            "bar": {"color": "#2563EB"},
            "steps": [
                {"range": [0, 150000], "color": "#22C55E"},
                {"range": [150000, 350000], "color": "#FACC15"},
                {"range": [350000, max_price], "color": "#EF4444"},
            ],
        },
    ))

    fig.update_layout(height=350)

    st.plotly_chart(fig, use_container_width=True)
st.subheader("📊 Property Overview")

chart_df = pd.DataFrame({
    "Feature": [
        "Rooms",
        "Bedrooms",
        "Population",
        "Households",
        "Income"
    ],
    "Value": [
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income
    ]
})

fig = px.bar(
    chart_df,
    x="Feature",
    y="Value",
    color="Feature",
    title="Property Characteristics"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("📋 Input Summary")

summary_df = pd.DataFrame({
    "Feature": [
        "Longitude",
        "Latitude",
        "Age",
        "Rooms",
        "Bedrooms",
        "Population",
        "Households",
        "Median Income",
        "Ocean Proximity"
    ],
    "Value": [
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity
    ]
})

st.dataframe(summary_df, use_container_width=True, hide_index=True)
# ==========================================
# Model Information
# ==========================================

st.markdown("---")

st.subheader("📊 Model Information")

c1, c2, c3 = st.columns(3)

c1.metric("Algorithm", "Ridge Regression")
c2.metric("RMSE", "70,066")
c3.metric("R² Score", "0.6254")

# ==========================================
# About Project
# ==========================================

st.markdown("---")

with st.expander("ℹ️ About this Project"):

    st.write("""
### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit

### Machine Learning Workflow

- Data Cleaning
- Missing Value Imputation
- One-Hot Encoding
- Feature Scaling
- Ridge Regression
- Model Evaluation
- Deployment using Streamlit

### Dataset

California Housing Dataset
""")

# ==========================================
# Footer
# ==========================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:gray;">

Made by <b>Sahil Nabi</b>

<br>

California House Price Prediction using Machine Learning

</div>
""",unsafe_allow_html=True)