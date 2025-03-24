import streamlit as st
import pandas as pd
import numpy as np
import json
from groq import Groq

# Initialize Groq API client with API key
client = Groq(api_key="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")

def analyze_threats(text_input):
    """Uses Groq API to analyze threats in text input."""
    completion = client.chat.completions.create(
        model="qwen-2.5-32b",
        messages=[{"role": "user", "content": text_input}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response

# Streamlit UI
st.title("AI-Powered Threat Detection System")
st.sidebar.header("Threat Analysis Panel")

# User input for log data or text
user_input = st.text_area("Enter network log, email content, or suspicious text:")
if st.button("Analyze Threat"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = analyze_threats(user_input)
            st.subheader("Threat Analysis Result")
            st.write(result)
    else:
        st.warning("Please enter text for analysis.")

# Simulated real-time threat data
data = pd.DataFrame({
    'IP Address': ["192.168.1.1", "203.0.113.45", "172.16.0.5", "45.67.89.12"],
    'Threat Level': ["Low", "High", "Medium", "Critical"],
    'Detected At': pd.to_datetime(["2025-03-24 12:00", "2025-03-24 12:15", "2025-03-24 12:30", "2025-03-24 12:45"])
})

st.subheader("Live Threat Intelligence")
st.dataframe(data)

# Threat Visualization
st.subheader("Threat Level Distribution")
st.bar_chart(data['Threat Level'].value_counts())
