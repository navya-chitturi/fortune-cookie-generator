import streamlit as st
import random

st.set_page_config(page_title="Fortune Cookie", page_icon="🥠")

fortunes = [
    "Good luck is following you today. 🍀",
    "You will meet someone you've been wanting to see very soon. 🤍",
    "Your kindness will return to you tenfold. 🤗",
    "Something you've secretly wished for is about to happen. ✨",
    "You'll receive good news when you least expect it. 💌",
    "Someone you've been thinking about will think of you too. 🩷",
]

st.title("🥠 Fortune Cookie Generator")

st.write("Enter your name and click the button below!")

name = st.text_input("👤 What's your name?")

if st.button("🥠 Open My Fortune"):
    if name.strip():
        st.success(f"💖 Hi, {name}!")
        st.subheader("🔮 Your Daily Fortune 🔮")
        st.write(random.choice(fortunes))
    else:
        st.warning("Please enter your name first!")

st.markdown("---")
st.caption("Made with ❤️ by Navya")
