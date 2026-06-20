import streamlit as st

st.set_page_config(
    page_title="🌸 TeenHealth - Menstrual Anemia & Diet Advisor", 
    page_icon="🩸", 
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #fdfafb; }
    div.stButton > button:first-child {
        background-color: #e03152 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 12px 28px !important;
    }
    .status-card, .food-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        border-left: 6px solid #e03152;
        margin-bottom: 20px;
    }
    .guide-box {
        background-color: #fff5f6;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ffdae0;
    }
    </style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

with st.expander("🚨 **EMERGENCY PAIN RELIEF GUIDE**"):
    st.write("1. **Apply Heat:** Use a hot water bottle on your lower tummy.")
    st.write("2. **Hydrate:** Sip warm water or ginger tea.")
    st.write("3. **Rest:** Lie down on your side in a curled fetal position.")

st.title("🌸 TeenHealth: Menstrual Anemia Advisor")
st.caption("⚠️ Educational tool only. Does not replace professional medical evaluation.")
st.divider()

tab1, tab2, tab3 = st.tabs(["📊 Diagnostic Checkup", "🍉 Smart Food Engine", "💡 Absorption Guide"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 Menstrual Cycle Profile")
        flow_days = st.radio("How many consecutive days does bleeding last?", ["Less than 7 days", "7 days or longer"])
        pad_frequency = st.selectbox("How often do you change pads on heavy days?", ["Every 4-6 hours", "Every 2-3 hours", "Every 1-2 hours"])
        clots = st.radio("Do you notice blood clots larger than a coin?", ["No", "Yes"])
        fatigue = st.radio("Describe your day-to-day energy level:", ["Normal", "Mild fatigue", "Severe exhaustion"])
        diet_habit = st.radio("Daily intake of green vegetables/lentils:", ["Consistent", "Intermittent", "Rarely"])
        calculate = st.button("Run Anemia Assessment", use_container_width=True)

    with col2:
        st.subheader("🎯 Evaluation Summary")
        if calculate:
            score = 0
            if flow_days == "7 days or longer":
                score = score + 2
            if pad_frequency == "Every 1-2 hours":
                score = score + 4
            if clots == "Yes":
                score = score + 2
            if fatigue == "Severe exhaustion":
                score = score + 3
            if diet_habit == "Rarely":
                score = score + 2

            if score >= 6:
                st.error("### ⚠️ Assessment: High Risk for Menstrual Anemia")
                st.warning("Please consult a school nurse or doctor for a routine hemoglobin checkup.")
            elif score >= 3:
                st.warning("### 🟡 Assessment: Moderate Risk for Menstrual Anemia")
                st.info("Boosting your target nutrition can reverse early iron loss quickly.")
            else:
                st.success("### ✅ Assessment: Healthy Profile")
            st.write("Head over to the **Smart Food Engine** tab to see tailored iron recipe plans!")

with tab2:
    st.subheader("🍉 Interactive Anemia Diet Planner")
    food_choice = st.radio("Select Category:", ["⚡ Quick Snacks", "🍛 Full Meals", "🍹 Drinks"], horizontal=True)
    
    if food_choice == "⚡ Quick Snacks":
        st.markdown("<div class='food-card'><h4>🥜 Jaggery & Peanuts (Gur Chana)</h4><p>Highly concentrated iron boost for rapid fatigue recovery.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='food-card'><h4>🌴 Dates & Raisins</h4><p>Packed with iron and magnesium to reduce cycle cramps.</p></div>", unsafe_allow_html=True)
    elif food_choice == "🍛 Full Meals":
        st.markdown("<div class='food-card'><h4>🥬 Spinach Paratha (Palak / Methi)</h4><p>Puree fresh greens into dough. Squeeze lemon juice on top to activate iron absorption.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='food-card'><h4>🫘 Lentil Stew (Dal / Chickpea Chana Masala)</h4><p>Excellent building blocks for healthy red blood cells.</p></div>", unsafe_allow_html=True)
    elif food_choice == "🍹 Drinks":
        st.markdown("<div class='food-card'><h4>🥤 Red Juice (Beetroot, Carrot & Amla)</h4><p>Beetroot supplies iron, while Amla delivers high-impact Vitamin C for maximum absorption.</p></div>", unsafe_allow_html=True)

with tab3:
    st.subheader("💡 Iron Absorption Rules")
    cg1, cg2 = st.columns(2)
    with cg1:
        st.markdown("<div class='guide-box'><b>✅ DO THIS:</b> Pair iron foods with Vitamin C (lemons/oranges). Cook in traditional cast iron pots.</div>", unsafe_allow_html=True)
    with cg2:
        st.markdown("<div class='guide-box'><b>❌ AVOID THIS:</b> Never drink tea or coffee within 1 hour of a meal. Tannins block iron completely!</div>", unsafe_allow_html=True)
