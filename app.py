import streamlit as st

# --- PAGE CONFIGURATION & ARCHITECTURE ---
st.set_page_config(
    page_title="🌸 TeenHealth - Menstrual Anemia & Diet Advisor", 
    page_icon="🩸", 
    layout="wide"
)

# Custom webpage-style design framework
st.markdown("""
    <style>
    .main { background-color: #fdfafb; }
    div.stButton > button:first-child {
        background-color: #e03152 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 12px 28px !important;
        font-size: 16px !important;
    }
    div.stButton > button:first-child:hover { background-color: #bd1f3c !important; }
    .status-card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        border-left: 6px solid #e03152;
        margin-bottom: 20px;
    }
    .food-card {
        background-color: #fff9fa;
        padding: 18px;
        border-radius: 10px;
        border-top: 4px solid #e03152;
        margin-bottom: 15px;
    }
    .guide-box {
        background-color: #fff5f6;
        padding: 18px;
        border-radius: 8px;
        border: 1px solid #ffdae0;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

# --- EMERGENCY CRISIS SYSTEM ---
with st.expander("🚨 **EMERGENCY: Experiencing Severe Period Pain or Extreme Dizziness Right Now?**", expanded=False):
    st.error("### 🛑 Immediate Action Plan:")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("""
        * **Apply Local Heat:** Position a hot water bottle or warming pad across your lower tummy to soothe cramps.
        * **Hydrate Immediately:** Drink warm water or fresh ginger infusion tea to encourage smooth muscle relaxation.
        """)
    with col_c2:
        st.markdown("""
        * **Fetal Posture Rest:** Recline on your side, bringing knees up up toward your chest to reduce physical abdominal strain.
        * **Alert an Adult:** Immediately communicate with a parent, school nurse, or teacher if you feel faint or nauseous.
        """)

st.title("🌸 TeenHealth: Menstrual Anemia Advisor")
st.caption("⚠️ *Disclaimer: This app utilizes international nutritional guidelines as an educational tool and does not substitute formal medical evaluation.*")

# --- ORGANIC VIRAL WHATSAPP SHARE ENGINE ---
current_url = "https://streamlit.app"
whatsapp_share_url = "https://wa.me" + current_url

st.markdown(f"""
    <a href="{whatsapp_share_url}" target="_blank" style="text-decoration: none;">
        <button style="background-color:#25D366; color:white; border:none; border-radius:8px; padding:12px 24px; font-weight:bold; font-size:15px; cursor:pointer; display:flex; align-items:center; box-shadow:0 4px 6px rgba(0,0,0,0.1); margin-top:10px;">
            🟢 Share with Friends on WhatsApp
        </button>
    </a>
""", unsafe_allow_html=True)

st.divider()

# --- HORIZONTAL LAYOUT ENGINE TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Diagnostic Checkup", 
    "🍉 Smart Food Suggestion Engine", 
    "💡 Critical Absorption Guide", 
    "📜 My Health History"
])

# ==================== TAB 1: DIAGNOSTIC ====================
with tab1:
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.subheader("📋 Menstrual Cycle Profile")
        st.write("Provide your specific cycle data based on the clinical **7-2-1 Rule**.")
        
        flow_days = st.radio(
            "1. How many consecutive days does your bleeding usually last?",
            ["Less than 7 days", "7 days or longer (Clinical Alert Indicator)"]
        )
        
        pad_frequency = st.selectbox(
            "2. During your heaviest days, how often must you change pads/tampons?",
            ["Normal (Every 4-6 hours)", "Frequently (Every 2-3 hours)", "Severely Heavy (Every 1-2 hours or less)"]
        )
        
        clots = st.radio(
            "3. Do you routinely notice blood clots larger than a 1-coin (1 inch wide)?",
            ["No, rarely or small size", "Yes, regularly during my cycle"]
        )

        st.subheader("⚡ Systemic Deficiency Markers")
        fatigue = st.radio(
            "4. Describe your day-to-day energy level outside your period:",
            ["Energetic / Balanced Baseline", "Mild fatigue / Periodic breathlessness", "Severe exhaustion / Frequent dizzy spells"]
        )

        diet_habit = st.radio(
            "5. Daily intake of iron-rich items (greens, legumes, fortified flour):",
            ["Consistent every day", "Intermittent / Variable", "Rarely consumed"]
        )
        
        calculate = st.button("📈 Run Efficient Anemia Assessment", use_container_width=True)

    with col2:
        st.subheader("🎯 Diagnostic Evaluation Summary")
        
        if calculate:
            risk_score = 0
            condition_summary = ""
            menstrual_severity = "Standard Flow Profile"

            if flow_days == "7 days or longer (Clinical Alert Indicator)": risk_score += 2
            if pad_frequency == "Severely Heavy (Every 1-2 hours or less)": 
                risk_score += 4
                menstrual_severity = "Abnormal / Heavy Menstrual Bleeding (HMB)"
            elif pad_frequency == "Frequently (Every 2-3 hours)": 
                risk_score += 2
            if clots == "Yes, regularly during my cycle": risk_score += 2
            
            if fatigue == "Severe exhaustion / Frequent dizzy spells": risk_score += 3
            elif fatigue == "Mild fatigue / Periodic breathlessness": risk_score += 1
            if diet_habit == "Rarely consumed": risk_score += 2

            if risk_score >= 6:
                condition_summary = "High Risk for Menstrual Anemia"
                st.error(f"### ⚠️ Assessment: {condition_summary}")
                st.markdown(f"**Menstrual Evaluation:** *{menstrual_severity}* Detected.")
                st.warning("🚨 **Direct Medical Guidance:** Heavy period blood loss is stripping away your body's iron stores faster than you can eat them. Please schedule a blood test with a doctor to check your **Hemoglobin and Ferritin levels**. Head over to the **Smart Food Suggestion Engine** tab to immediately check out meal options designed to help recover lost iron.")
            elif 3 <= risk_score < 6:
                condition_summary = "Moderate Risk for Menstrual Anemia"
                st.warning(f"### 🟡 Assessment: {condition_summary}")
                st.info("👉 **Targeted Period Advice:** You are losing iron quickly during your cycle. You can protect your body from sliding into severe anemia by selecting targeted iron foods from the recipe tab specifically during your period week.")
            else:
                condition_summary = "Healthy Baseline Profile"
                st.success(f"### ✅ Assessment: {condition_summary}")
                st.write("🎉 Great status! Your current cycle parameters and baseline nutrition habits indicate protective iron reserves.")

            st.session_state.history.append({"Condition": condition_summary, "Flow": pad_frequency, "Fatigue": fatigue})
        else:
            st.info("Input your current cycle variables on the left panel, then press **Run Efficient Anemia Assessment** to display your specific report framework instantly.")

# ==================== TAB 2: SMART FOOD SUGGESTION ENGINE ====================
with tab2:
    st.subheader("🍉 Interactive Anemia Diet Planner")
    st.write("When fighting anemia, you need iron combined with Vitamin C for absorption. Select what kind of food options you want to view right now:")
    
    food_choice = st.radio(
        "I am looking for:",
        ["⚡ Quick Snacks & Sweet Treats", "🍛 Full Iron-Rich Meals", "🍹 Refreshing Drinks & Smoothies"],
        horizontal=True
    )
    
    st.write("---")
    
    if food_choice == "⚡ Quick Snacks & Sweet Treats":
        st.markdown("""
        <div class='food-card'>
            <h4>🥜 Jaggery & Roasted Peanut Mix (Gur Chana / Chikki)</h4>
            <p><b>Why it works:</b> Jaggery (Gur) is a highly concentrated plant iron source. Combined with roasted peanuts or roasted chickpeas, it gives a rapid energy boost during a fatigue crash.</p>
            <p><b>💡 Pro-Tip:</b> Eat a small piece of this snack daily during your period week!</p>
        </div>
        <div class='food-card'>
            <h4>🌴 Sweet Iron Dates & Raisins</h4>
            <p><b>Why it works:</b> Dark dates and black raisins are packed with iron and magnesium, which help reduce muscle cramps.</p>
            <p><b>💡 Pro-Tip:</b> Soak 5-6 raisins in water overnight and chew them in the morning for best results.</p>
        </div>
        <div class='food-card'>
            <h4>🌻 Sesame Seed Bars (Til Gajak / Til Ladoo)</h4>
            <p><b>Why it works:</b> Sesame seeds (Til) contain extremely high quantities of mineral iron and calcium to help strengthen your body.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif food_choice == "🍛 Full Iron-Rich Meals":
        st.markdown("""
        <div class='food-card'>
            <h4>🥬 Iron-Boosted Green Leafy Flatbread (Spinach Palak Paratha / Methi Puri)</h4>
            <p><b>Why it works:</b> Pureeing fresh spinach (Palak) or fenugreek leaves (Methi) directly into your grain dough creates an invisible, delicious iron-rich meal.</p>
            <p><b>🍊 Vitamin C Catalyst Required:</b> Always squeeze fresh lemon juice over the hot flatbread to activate the iron!</p>
        </div>
        <div class='food-card'>
