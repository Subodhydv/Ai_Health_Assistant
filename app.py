import streamlit as st
from openai import OpenAI

client = OpenAI()

st.set_page_config(page_title="AI Health Assistant", page_icon="🩺")

st.title("🩺 AI Health Assistant")
st.write("Enter your symptoms below:")

# Prediction logic
def predict(symptoms):
    s = symptoms.lower()

    if "fever" in s and "cough" in s:
        return "Flu or Viral Infection", "Medium"
    elif "chest pain" in s or "breathing" in s:
        return "Possible Serious Condition", "High"
    elif "headache" in s:
        return "Migraine or Infection", "Medium"
    else:
        return "General Condition", "Low"

# AI explanation
def explain(symptoms, disease):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Symptoms: {symptoms}, Condition: {disease}. Give simple advice."}
        ]
    )
    return response.choices[0].message.content

symptoms = st.text_area("Symptoms")

if st.button("Analyze"):
    disease, risk = predict(symptoms)

    st.subheader("Result")
    st.write("Condition:", disease)
    st.write("Risk Level:", risk)

    if risk == "High":
        st.error("⚠️ Seek medical attention immediately")

    # ✅ FIXED PART (correct indentation)
    try:
        advice = explain(symptoms, disease)
    except:
        advice = "Stay hydrated, take rest, and consult a doctor if symptoms persist."

    st.subheader("Advice")
    st.write(advice)

st.caption("⚠️ This is not a medical diagnosis tool")