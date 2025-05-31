import streamlit as st
import langchain_helper

st.set_page_config(page_title="Startup Name & Pitch Generator", page_icon="🚀")
st.title("🚀 Startup Name & Elevator Pitch Generator")

industry = st.sidebar.selectbox("Select an Industry", [
    "Healthcare", "Fintech", "Education", "AI", "E-commerce", "Gaming", "Sustainability"
])

if industry:
    result = langchain_helper.generate_startup_name_and_pitch(industry)

    st.subheader("🧠 Startup Name")
    st.success(result['startup_name'].strip())

    st.subheader("💡 Elevator Pitch")
    st.markdown(result['pitch'].strip())
