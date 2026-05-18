import streamlit as st
from graph.workflow import run_newsletter_agent

st.title("🤖 AI Newsletter Agent")

goal = st.text_area("Enter Goal")

human_mode = st.toggle("Human Mode")

if st.button("Run Agent"):

    if not goal:
        st.warning("Please enter a goal")
        st.stop()

    try:
        result = run_newsletter_agent(goal, human_in_loop=human_mode)

        st.success("Newsletter Generated 🎉")
        st.markdown(result)

    except Exception as e:
        st.error("Error occurred")
        st.exception(e)