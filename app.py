import streamlit as st
import tempfile

from streamlit_mic_recorder import mic_recorder

from main_pipeline import process_voice_complaint

st.title("🎙️ VoiceGov")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording",
    just_once=True
)

if audio:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio["bytes"])
        audio_path = f.name

    st.success("Recording completed!")

    with st.spinner("Processing..."):
        result = process_voice_complaint(audio_path)

    st.write("### Complaint")
    st.write(result["transcribed_text"])

    st.write("### Category")
    st.success(result["category"])

    st.write("### Urgency")
    st.warning(result["urgency"])

    st.write("### Department")
    st.info(result["department"]["department_name"])

    st.write("### Helpline")
    st.info(result["department"]["helpline"])

    st.write("### Entities")
    st.json(result["entities"])

    st.write("### Similar Complaints")
    st.dataframe(result["similar_complaints"])

    st.write("### Complaint Letter")
    st.text_area("", result["letter"], height=300)