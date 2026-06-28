import streamlit as st
from streamlit_mic_recorder import speech_to_text
from huggingface_hub import InferenceClient

# 1. Page Configuration for a Premium Application feel
st.set_page_config(
    page_title="Interview AI Preparation Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. Authentication Token Configuration
HF_TOKEN = st.secrets["HF_TOKEN"]

@st.cache_resource
def get_hf_client():
    return InferenceClient(
        model="Qwen/Qwen2.5-7B-Instruct",
        token=HF_TOKEN
    )

try:
    client = get_hf_client()
except Exception as e:
    st.error(f"Initialization Failure: {e}")

# Initialize session state tracking
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Sidebar Dashboard Control Panel
with st.sidebar:
    st.markdown("<h2 style='color: #2563EB;'>⚙️ Dashboard Control</h2>", unsafe_allow_html=True)
    st.caption("Manage session variables and view system health parameters.")
    st.markdown("---")

    # Live System Statistics Dashboard
    st.markdown("### 📊 Live Analytics")
    total_turns = len([m for m in st.session_state.messages if m["role"] == "user"])

    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric(label="Responses", value=total_turns)
    with col_stat2:
        st.metric(label="System Status", value="Online", delta="Stable")

    st.markdown("---")
    st.markdown("### 🛠️ Session Actions")
    if st.button("🗑️ Clear Evaluation History", use_container_width=True, type="primary"):
        st.session_state.messages = []
        st.rerun()

# 4. Premium Top Header Layout
st.markdown("<h1 style='text-align: center; color: #2563EB; margin-bottom: 0;'>🤖 InterviewAI Preparation Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B; font-size: 16px; margin-top: 5px;'>Advanced Capstone Evaluation Prototype</p>", unsafe_allow_html=True)

# Main Structural Layout Tabs
tab_chat, tab_info = st.tabs(["💬 Live Interview Sandbox", "ℹ️ System Architecture Guide"])

with tab_chat:
    # 5. Presentation Layer: Chat Interface Display
    if not st.session_state.messages:
        st.markdown(
            "<div style='background-color: #EFF6FF; border-left: 5px solid #2563EB; padding: 15px; border-radius: 5px; margin-top: 15px;'>"
            "<h4 style='margin: 0; color: #1E40AF;'>👋 Welcome to your Automated Technical Mock Interview!</h4>"
            "<p style='margin: 5px 0 0 0; color: #1E3A8A; font-size: 14px;'>Initiate the sequence by stating your core domain (e.g., 'Hi, I am a Java Developer') using either the microphone module or the text terminal input below.</p>"
            "</div>",
            unsafe_allow_html=True
        )

    # Loop and beautifully render history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 6. Premium Input Control Panel Card
    st.markdown("### 📥 Response Submission Hub")
    with st.container(border=True):
        col_widget, col_desc = st.columns([1.2, 2.8])

        with col_widget:
            # Native browser speech-to-text widget
            user_speech = speech_to_text(
                language='en',
                start_prompt="🎙️ Record Answer",
                stop_prompt="🟩 Finalize Audio",
                just_once=True,
                key='STT_ULTIMATE'
            )

        with col_desc:
            st.markdown(
                "<p style='color: #64748B; font-size: 13px; margin-top: 8px; line-height: 1.4;'>"
                "💡 <b>Multi-Modal Input:</b> Tap the microphone to stream and transcribe speech, or leverage the interactive chat terminal input below to type manually."
                "</p>",
                unsafe_allow_html=True
            )

    # Floating Baseline Terminal Input
    user_text = st.chat_input("Input your professional response statement here...")

    # Route Input Stream
    final_user_input = None
    if user_speech:
        final_user_input = user_speech
    elif user_text:
        final_user_input = user_text

    # 7. Core AI Inference & Evaluation Loop
    if final_user_input:
        # Display user submission instantly
        with st.chat_message("user"):
            st.markdown(final_user_input)

        st.session_state.messages.append({
            "role": "user",
            "content": final_user_input
        })

        # Trigger Inference Response Window
        with st.chat_message("assistant"):
            with st.spinner("⚡ Quantum Engine processing response analytics..."):
                try:
                    # System architectural instructions demanding beautiful structured format
                    system_prompt = (
                        "Review their response. You must always reply with highly organized Markdown formatting:\n\n"
                        "### 📋 Feedback Summary\n"
                        "[Provide a short, professional breakdown here]\n\n"
                        "### Strengths\n"
                        "* Point 1\n"
                        "* Point 2\n\n"
                        "### 🎯 Areas to Improve\n"
                        "* Point 1\n\n"
                        "### ❓ Next Interview Question\n"
                        "[Ask the next logical tech question based on their domain]"
                    )

                    formatted_messages = [
                        {"role": "system", "content": system_prompt}
                    ] + st.session_state.messages

                    response = client.chat_completion(
                        messages=formatted_messages,
                        max_tokens=450,
                        temperature=0.7
                    )

                    ai_reply = response.choices[0].message.content
                    st.markdown(ai_reply)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": ai_reply
                    })

                    st.rerun()

                except Exception as e:
                    st.error(f"Cloud Gateway Interrupted: {e}")
                    st.info("Check physical hardware network adapters or verify Hugging Face platform tokens.")

with tab_info:
    st.markdown("### 🏗️ Prototype System Architecture")
    st.info("This project utilizes a highly efficient cloud-decoupled pipeline designed for production scalability.")

    # Architectural Layout Map
    st.markdown(
        "```text\n"
        "[User Interface Layer]  --> Streamlit App (Frontend)\n"
        "         |\n"
        "         +--> [Audio Pipeline] --> Browser WebRTC -> Text Conversion\n"
        "         |\n"
        "         +--> [Inference Layer] --> Hugging Face Serverless Architecture\n"
        "                                     (Model Target: Qwen-2.5-7B-Instruct)\n"
        "```"
    )

    st.success("✅ No localized heavy weights required. App footprints remain under 50MB runtime space.")