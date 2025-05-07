import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="BMP Fishbone Form", layout="centered")
st.title("BMP Fishbone Diagram (Manual Entry)")

with st.form("bmp_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        na = st.number_input("Na", step=0.1)
        k = st.number_input("K", step=0.1)
    with col2:
        cl = st.number_input("Cl", step=0.1)
        hco3 = st.number_input("HCO3", step=0.1)
    with col3:
        bun = st.number_input("BUN", step=0.1)
        cr = st.number_input("Cr", step=0.1)
    glucose = st.number_input("Glucose", step=0.1)
    
    submitted = st.form_submit_button("Generate Diagram")

if submitted:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")

    ax.plot([0.2, 0.5], [0.5, 0.5], 'k', lw=2)
    for x in [0.3, 0.4]:
        ax.plot([x, x], [0.5, 0.6], 'k', lw=2)
        ax.plot([x, x], [0.5, 0.4], 'k', lw=2)
    ax.plot([0.5, 0.6], [0.5, 0.6], 'k', lw=2)
    ax.plot([0.5, 0.6], [0.5, 0.4], 'k', lw=2)

    fontsize = 47
    ax.text(0.25, 0.52, f"{na:g}", ha='center', fontsize=fontsize)
    ax.text(0.35, 0.52, f"{cl:g}", ha='center', fontsize=fontsize)
    ax.text(0.45, 0.52, f"{bun:g}", ha='center', fontsize=fontsize)

    ax.text(0.25, 0.44, f"{k:g}", ha='center', fontsize=fontsize)
    ax.text(0.35, 0.44, f"{hco3:g}", ha='center', fontsize=fontsize)
    ax.text(0.45, 0.44, f"{cr:g}", ha='center', fontsize=fontsize)

    ax.text(0.54, 0.5, f"{glucose:g}", va='center', ha='left', fontsize=fontsize)

    st.pyplot(fig)
