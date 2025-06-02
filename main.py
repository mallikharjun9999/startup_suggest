
import streamlit as st
import langchain_helper

st.set_page_config(
    page_title="AI Startup Generator Suite", 
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI-Powered Startup Generator Suite")
st.markdown("*Generate comprehensive startup insights powered by AI*")

# Sidebar for industry selection
st.sidebar.header("🎯 Select Your Industry")
industry = st.sidebar.selectbox("Choose an Industry", [
    "Healthcare", "Fintech", "Education", "AI", "E-commerce", "Gaming", "Sustainability"
])

if industry:
    # Generate core startup info
    with st.spinner("🧠 Generating startup insights..."):
        result = langchain_helper.generate_startup_name_and_pitch(industry)
        startup_name = result['startup_name'].strip()
        pitch = result['pitch'].strip()
    
    # Display core info at the top
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 Startup Name")
        st.success(startup_name)
    
    with col2:
        st.subheader("💡 Elevator Pitch")
        st.info(pitch)
    
    st.markdown("---")
    
    # Organize features in tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📍 Location & Market", 
        "💰 Finance & Business", 
        "🎯 Audience & Competition", 
        "🛠️ Tech & Tools", 
        "🚀 Launch Strategy"
    ])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📍 Ideal Launch Location")
            with st.spinner("Finding best locations..."):
                location = langchain_helper.generate_ideal_location(industry)
            st.markdown(location)
        
        with col2:
            st.subheader("🎯 Target Audience")
            with st.spinner("Analyzing target audience..."):
                audience = langchain_helper.generate_target_audience(industry)
            st.markdown(audience)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Cost Breakdown")
            with st.spinner("Calculating startup costs..."):
                costs = langchain_helper.generate_cost_estimate(industry)
            st.markdown(costs)
        
        with col2:
            st.subheader("💼 Business Model")
            with st.spinner("Designing business model..."):
                business_model = langchain_helper.generate_business_model(industry)
            st.markdown(business_model)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🧑‍💻 Competitor Analysis")
            with st.spinner("Researching competitors..."):
                competitors = langchain_helper.generate_competitor_analysis(industry)
            st.markdown(competitors)
        
        with col2:
            st.subheader("💬 One-Liner Pitch")
            with st.spinner("Crafting perfect pitch..."):
                one_liner = langchain_helper.generate_one_liner_pitch(startup_name, industry)
            st.success(f"🎯 {one_liner}")
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🧠 Tech Stack Recommendations")
            with st.spinner("Selecting tech stack..."):
                tech_stack = langchain_helper.generate_tech_stack(industry)
            st.markdown(tech_stack)
        
        with col2:
            st.subheader("🌐 Domain Name Suggestions")
            with st.spinner("Generating domain names..."):
                domains = langchain_helper.generate_domain_names(startup_name, industry)
            st.markdown(domains)
    
    with tab5:
        st.subheader("📅 6-Month Launch Roadmap")
        with st.spinner("Creating launch roadmap..."):
            roadmap = langchain_helper.generate_launch_roadmap(industry)
        st.markdown(roadmap)
    
    # Footer
    st.markdown("---")
    st.markdown("*Powered by LangChain + Groq (LLaMA 3) 🤖*")
    
else:
    st.info("👈 Please select an industry from the sidebar to get started!")
    
    # Add some helpful info when no industry is selected
    st.markdown("""
    ## 🌟 Features Include:
    
    - **🏢 Startup Name & Pitch Generation**
    - **📍 Ideal Launch Location Analysis**
    - **💰 Comprehensive Cost Breakdown**
    - **🎯 Target Audience Insights**
    - **🧠 Tech Stack Recommendations**
    - **💼 Business Model Strategies**
    - **🧑‍💻 Competitor Analysis**
    - **📅 6-Month Launch Roadmap**
    - **🌐 Domain Name Suggestions**
    - **💬 Catchy One-Liner Pitches**
    
    Select an industry to generate comprehensive AI-powered startup insights!
    """)
