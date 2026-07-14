import streamlit as st

st.set_page_config(page_title="Student Eligibility Dashboard", page_icon="🎓", layout="centered")

st.title("🎓 Student Eligibility Dashboard")
st.write("Check your eligibility for the mid exam, final exam, and course certificate.")

st.divider()

# --- Inputs ---
col1, col2, col3 = st.columns(3)

with col1:
    attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=0, step=1)

with col2:
    mid_marks = st.number_input("Mid Exam Marks (%)", min_value=0, max_value=100, value=0, step=1)

with col3:
    final_marks = st.number_input("Final Exam Marks (%)", min_value=0, max_value=100, value=0, step=1)

st.divider()

# --- Logic ---
if st.button("Check Eligibility", type="primary", use_container_width=True):

    if attendance >= 50:
        if mid_marks >= 50:
            if final_marks >= 50:
                st.success("You will get the course certificate! 😎")
                st.balloons()
            else:
                st.error("In the final exam your marks are less than 50%, so you can't get the certificate.")
        else:
            st.warning("Sorry, you are not eligible for the final exam because your mid exam marks are less than 50%.")
    else:
        st.error("Your attendance is less than 50%, you are not eligible for the mid exam. Sorry, try in the future.")

    # --- Progress overview ---
    st.divider()
    st.subheader("📊 Your Stats")

    c1, c2, c3 = st.columns(3)
    c1.metric("Attendance", f"{attendance}%", "Pass" if attendance >= 50 else "Fail")
    c2.metric("Mid Marks", f"{mid_marks}%", "Pass" if mid_marks >= 50 else "Fail")
    c3.metric("Final Marks", f"{final_marks}%", "Pass" if final_marks >= 50 else "Fail")

    st.progress(min(attendance, 100) / 100, text="Attendance")
    st.progress(min(mid_marks, 100) / 100, text="Mid Exam Marks")
    st.progress(min(final_marks, 100) / 100, text="Final Exam Marks")

st.divider()
st.caption("Made with ❤️ using Streamlit")