import streamlit as st

# --- STYLING ---
st.set_page_config(page_title="IT Support Assistant", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp { color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #1e1e26; border-right: 2px solid #3d3d4d; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #4CAF50; color: white; }
    .stButton>button:hover { background-color: #45a049; border: 1px solid white; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: TOOLS & GUIDE ---
st.sidebar.title("🛠️ IT Toolbox")

# Feature 1: Email Generator
st.sidebar.header("📧 Email Generator")
issue = st.sidebar.text_input("Issue Fixed", placeholder="e.g. VPN Error")
if st.sidebar.button("Generate Email"):
    st.sidebar.code(f"Subject: Fixed: {issue}\n\nHi Team,\nThis is resolved. Please restart.")

st.sidebar.markdown("---")

# Feature 2: Troubleshooting Guide (ALWAYS VISIBLE NOW)
st.sidebar.header("🔍 Quick Fix Guide")
st.sidebar.info("""
**1. Connection:** Check VPN & WiFi
**2. System:** Restart Laptop
**3. Apps:** Clear Browser Cache
""")

# Feature 3: Reset Button (Fixes the "Persistent Response" issue)
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# --- MAIN INTERFACE: CHATBOT ---
st.title("🤖 AI IT Support Assistant")
st.caption("Tier 1 Support Simulation")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask me a technical question..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and add assistant response to state
    with st.chat_message("assistant"):
        response = f"I've analyzed your request: **'{prompt}'**. Have you checked the 'Quick Fix Guide' in the sidebar? If that fails, I can escalate this to a human technician."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- RESPONSIBLE AI FOOTER ---
st.markdown("---")
st.warning("⚠️ **Responsible AI Disclaimer:** This tool is for troubleshooting assistance. Do not share passwords. For hardware damage, see a human tech.")
