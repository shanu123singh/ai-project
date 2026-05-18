import streamlit as st
from graph.workflow import run_newsletter_agent

st.title("AI Newsletter Agent")

goal = st.text_area("Enter Goal")

human_mode = st.toggle("Human Mode")

if st.button("Run"):

    if not goal:
        st.warning("Enter goal")
        st.stop()

    result = run_newsletter_agent(goal, human_in_loop=human_mode)

    st.success("Done")
    st.write(result)