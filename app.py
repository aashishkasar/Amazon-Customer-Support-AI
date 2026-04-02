import streamlit as st
import json
from utils.llm_setup import get_llm
from prompts.support_prompt import get_prompt
from pypdf import PdfReader

st.title("📦 Amazon Customer Support AI")

# 🔐 API Key Input
api_key = st.text_input("🔑 Enter GROQ API Key (optional)", type="password")

# ---------------------------
# 📥 Query Input
# ---------------------------
query = st.text_input("Enter Customer Query")

# ---------------------------
# 📄 Policy Input Options
# ---------------------------
st.subheader("📜 Policy Input")

policy_text = st.text_area("✍️ Enter Policy manually")

uploaded_file = st.file_uploader(
    "📂 Or upload policy file (.txt or .pdf)",
    type=["txt", "pdf"]
)

# ---------------------------
# 📄 Extract Policy
# ---------------------------
policy = ""

# Priority: File > Text
if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        policy = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
            policy = text

    else:
        policy = policy_text

        # ---------------------------
        # ▶️ Generate Button
        # ---------------------------
        if st.button("Generate"):

            if not query:
                st.warning("⚠️ Please enter Query")

            elif not policy:
                st.warning("⚠️ Please provide Policy (text or file)")

            else:
                with st.spinner("Thinking..."):

                    llm = get_llm(api_key)
                    prompt = get_prompt()

                    final_prompt = prompt.format(query=query, policy=policy)
                    response = llm.invoke(final_prompt)

                    try:
                        result = json.loads(response.content)

                        st.success("✅ Answer Generated")

                        st.write("### 📌 Answer")
                        st.write(result.get("answer"))

                        st.write("### 🧠 Reason")
                        st.write(result.get("reason"))

                        st.write("### 📊 Confidence")
                        st.write(result.get("confidence"))

                    except:
                        st.error("⚠️ Invalid JSON output")
                        st.code(response.content)