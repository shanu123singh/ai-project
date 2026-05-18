import streamlit as st

from graph.workflow import run_newsletter_agent

st.title("AI Newsletter Agent")

goal = st.text_area(
    "Enter Goal",
    "Create a weekly newsletter on latest AI agent news and send it to subscribers."
)

human_mode = st.toggle(
    "Human-in-the-Loop Mode"
)

if st.button("Run Agent"):

    newsletter = run_newsletter_agent(
        goal,
        human_in_loop=human_mode
    )

    st.success("Newsletter Generated!")

    st.markdown(newsletter)