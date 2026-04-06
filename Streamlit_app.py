import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Energy Consumption Limiter", layout="centered")

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "reg" not in st.session_state:
    st.session_state.reg = ""

# ---------------- SIDEBAR ----------------
menu = ["Home", "Theory", "Principle", "Quiz", "Scorecard", "Feedback"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ----------------
if choice == "Home":
    st.title("⚡ Smart Energy Consumption Limiter")

    st.session_state.name = st.text_input("Enter Your Name")
    st.session_state.reg = st.text_input("Enter Register Number")

    if st.session_state.name and st.session_state.reg:
        st.success(f"Welcome {st.session_state.name} (Reg No: {st.session_state.reg})")

    st.markdown("""
    ### 🚀 Project Overview
    This system ensures that electricity consumption stays within a safe limit.

    💡 Goal: Prevent overload and improve energy efficiency.
    """)

    st.info("“Efficient energy management is not a choice, it is a necessity for a sustainable future.”")

# ---------------- THEORY ----------------
elif choice == "Theory":
    st.title("📘 Theory")
    st.write("""
    The Smart Energy Consumption Limiter monitors electrical usage using current sensors.
    When usage exceeds a predefined threshold, the system automatically cuts off power.

    Advantages:
    - Prevents overload
    - Saves electricity
    - Improves safety
    """)

# ---------------- PRINCIPLE ----------------
elif choice == "Principle":
    st.title("⚙️ Working Principle")
    st.write("""
    1. Current sensor measures electricity usage  
    2. Data sent to microcontroller  
    3. Compared with threshold value  
    4. If exceeded → Relay turns OFF power  
    """)

# ---------------- QUIZ ----------------
elif choice == "Quiz":
    st.title("🧠 Quiz (25 Questions)")

    questions = [
        ("Which sensor is used to measure current?", ["ACS712", "LM35", "IR"], "ACS712"),
        ("Main function of relay?", ["Switch ON/OFF", "Store data", "Heat"], "Switch ON/OFF"),
        ("Purpose of system?", ["Save energy", "Waste energy", "Lighting"], "Save energy"),
        ("Device used for control?", ["Arduino", "Battery", "Fan"], "Arduino"),
        ("Sensor type?", ["Analog", "Digital", "Both"], "Analog"),
        ("Overload means?", ["Excess current", "Low current", "No current"], "Excess current"),
        ("System cuts power when?", ["Below limit", "Above limit", "Always"], "Above limit"),
        ("Component for display?", ["LCD", "Resistor", "Capacitor"], "LCD"),
        ("Voltage unit?", ["Volt", "Amp", "Watt"], "Volt"),
        ("Current unit?", ["Ampere", "Volt", "Ohm"], "Ampere"),
        ("Power formula?", ["V*I", "V/I", "I/V"], "V*I"),
        ("Energy unit?", ["kWh", "Volt", "Amp"], "kWh"),
        ("Controller type?", ["Microcontroller", "Motor", "Switch"], "Microcontroller"),
        ("Relay works as?", ["Switch", "Sensor", "Storage"], "Switch"),
        ("IoT stands for?", ["Internet of Things", "Input of Things", "Index"], "Internet of Things"),
        ("Sensor measures?", ["Current", "Color", "Sound"], "Current"),
        ("Main safety feature?", ["Cutoff", "Alarm only", "Display"], "Cutoff"),
        ("System improves?", ["Efficiency", "Heat", "Waste"], "Efficiency"),
        ("Limit is set by?", ["User", "Sensor", "Wire"], "User"),
        ("Real-time means?", ["Instant", "Delayed", "Stored"], "Instant"),
        ("Load means?", ["Device usage", "Wire", "Voltage"], "Device usage"),
        ("Circuit protection?", ["Fuse", "Fan", "LED"], "Fuse"),
        ("Smart system uses?", ["Automation", "Manual", "None"], "Automation"),
        ("Data monitoring?", ["Yes", "No", "Maybe"], "Yes"),
        ("Main goal?", ["Control energy", "Increase bill", "Heat"], "Control energy")
    ]

    score = 0

    for i, (q, options, correct) in enumerate(questions):
        answer = st.radio(f"{i+1}. {q}", options, key=f"q{i}")

        if answer:
            if answer == correct:
                st.success(f"Q{i+1}: Correct ✅")
                score += 1
            else:
                st.error(f"Q{i+1}: Wrong ❌")

    if st.button("Submit Quiz"):
        st.session_state.score = score
        st.session_state.submitted = True
        st.success("Quiz Submitted! Go to Scorecard")

# ---------------- SCORECARD ----------------
elif choice == "Scorecard":
    st.title("📊 Scorecard")

    if st.session_state.submitted:

        score = st.session_state.score
        total = 25
        percentage = (score / total) * 100

        if percentage >= 90:
            grade = "A+"
            credit = 10
        elif percentage >= 75:
            grade = "A"
            credit = 9
        elif percentage >= 60:
            grade = "B"
            credit = 8
        elif percentage >= 50:
            grade = "C"
            credit = 7
        else:
            grade = "Fail"
            credit = 0

        st.subheader("👤 Student Details")
        st.write(f"Name: {st.session_state.name}")
        st.write(f"Register Number: {st.session_state.reg}")

        st.subheader("📈 Performance")
        st.write(f"Score: {score} / {total}")
        st.write(f"Percentage: {percentage:.2f}%")
        st.write(f"Grade: {grade}")
        st.write(f"Credit Score: {credit}")

        if grade == "A+":
            st.balloons()

    else:
        st.warning("Please complete the quiz first!")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":
    st.title("📝 Feedback")

    name = st.text_input("Enter your name")
    feedback = st.text_area("Enter your feedback")

    if st.button("Submit"):
        st.success("Thank you for your feedback!")
