import streamlit as st

st.title("LegalEase AI")
st.write("Legal Document Assistant")
st.divider()

a = st.selectbox("Doc Type", ["NDA", "Rental", "Job"])
b = st.text_area("Details:")

if st.button("Generate"):
    if b:
        st.success("Generated!")
        st.write(a)
        st.write(b)
        st.write("Draft by LegalEase AI")
    else:
        st.warning("Enter details")