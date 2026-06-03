import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="EduPredict AI",
    page_icon="🎓",
    layout="wide"
)

# =========================================
# LOAD MODEL
# =========================================

model = joblib.load("advanced_student_model.pkl")

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #050816,
        #0b1026,
        #111c44
    );
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0a0f25;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Title */
.main-title {
    font-size: 58px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #8b5cf6,
        #ec4899
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.sub-text {
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 25px;
}

/* Glass Card */
.glass {
    background: rgba(17, 25, 40, 0.75);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 0 30px rgba(0,0,0,0.3);
}

/* Metric Cards */
.metric-card {
    background: rgba(17, 25, 40, 0.8);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-5px);
}

/* Predict Button */
.stButton button {
    width: 100%;
    height: 60px;
    border-radius: 18px;
    border: none;
    font-size: 22px;
    font-weight: 700;
    background: linear-gradient(
        90deg,
        #4f46e5,
        #9333ea,
        #ec4899
    );
    color: white;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
}

/* Slider */
.stSlider > div > div {
    color: #8b5cf6 !important;
}

/* Table */
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
}

/* Input */
.stTextInput input {
    border-radius: 12px;
    background-color: rgba(255,255,255,0.05);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.markdown("""
# 🎓 EduPredict AI
### Smart Student Analytics
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Prediction Dashboard",
        "Analytics"
    ]
)

# =========================================
# DASHBOARD
# =========================================

if page == "Prediction Dashboard":

    st.markdown("""
    <div class='main-title'>
    Student Prediction Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub-text'>
    Predict student performance using Machine Learning
    </div>
    """, unsafe_allow_html=True)

    # =====================================
    # INPUT SECTION
    # =====================================

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("🧑 Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        student_name = st.text_input(
            "Student Name"
        )

        hours = st.slider(
            "Study Hours",
            0,
            15,
            5
        )

    with col2:

        sleep = st.slider(
            "Sleep Hours",
            0,
            12,
            7
        )

        attendance = st.slider(
            "Attendance Percentage",
            0,
            100,
            80
        )

    with col3:

        assignments = st.slider(
            "Assignments Completed",
            0,
            10,
            5
        )

        previous_score = st.slider(
            "Previous Exam Score",
            0,
            100,
            60
        )

        internet_usage = st.slider(
            "Internet Usage Hours",
            0,
            12,
            4
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # =====================================
    # INPUT DATA
    # =====================================

    input_data = pd.DataFrame({
        "Hours": [hours],
        "Sleep": [sleep],
        "Attendance": [attendance],
        "Assignments": [assignments],
        "PreviousScore": [previous_score],
        "InternetUsage": [internet_usage]
    })

    # =====================================
    # PREDICTION BUTTON
    # =====================================

    if st.button("🚀 Predict Student Performance"):

        prediction = model.predict(input_data)[0]

        prediction = round(prediction, 2)

        # =================================
        # GRADE
        # =================================

        if prediction >= 90:
            grade = "A+"
            performance = "Excellent 🔥"
            rank = "Top 5%"

        elif prediction >= 75:
            grade = "A"
            performance = "Very Good 🚀"
            rank = "Top 20%"

        elif prediction >= 60:
            grade = "B"
            performance = "Good 🙂"
            rank = "Top 35%"

        else:
            grade = "C"
            performance = "Needs Improvement ⚠️"
            rank = "Average"

        # =================================
        # SUMMARY TABLE
        # =================================

        st.write("")

        st.markdown("<div class='glass'>", unsafe_allow_html=True)

        st.subheader("📋 Student Input Summary")

        st.dataframe(
            input_data,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")

        # =================================
        # METRIC CARDS
        # =================================

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Predicted Score</h3>
            <h1>{prediction}</h1>
            <p>/100</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Grade</h3>
            <h1>{grade}</h1>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Performance</h3>
            <h2>{performance}</h2>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Rank</h3>
            <h2>{rank}</h2>
            </div>
            """, unsafe_allow_html=True)

        with c5:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>Potential</h3>
            <h2>High 📈</h2>
            </div>
            """, unsafe_allow_html=True)

        # =================================
        # DOWNLOAD REPORT
        # =================================

        report = pd.DataFrame({
            "Student Name": [student_name],
            "Study Hours": [hours],
            "Sleep Hours": [sleep],
            "Attendance": [attendance],
            "Assignments": [assignments],
            "Previous Score": [previous_score],
            "Internet Usage": [internet_usage],
            "Predicted Score": [prediction],
            "Grade": [grade],
            "Performance": [performance],
            "Generated On": [datetime.now()]
        })

        csv = report.to_csv(index=False)

        st.download_button(
            "📥 Download Report",
            csv,
            file_name="student_report.csv",
            mime="text/csv"
        )

# =========================================
# ANALYTICS PAGE
# =========================================

elif page == "Analytics":

    st.markdown("""
    <div class='main-title'>
    Analytics Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='glass'>
    <h2>📊 Performance Insights</h2>
    <p>
    Students with higher attendance,
    balanced sleep, and lower internet
    distraction tend to score higher.
    </p>
    </div>
    """, unsafe_allow_html=True)