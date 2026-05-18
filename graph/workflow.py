import streamlit as st
import os

from agents.planner import create_plan
from agents.research import research_news
from agents.summarizer import summarize_articles
from agents.writer import generate_newsletter
from agents.critic import critique_newsletter
from agents.solver import improve_newsletter
from agents.sender import simulate_send

from tools.HTML_generator import markdown_to_html
from tools.save_file import save_output


# ----------------------------
# LOAD SECRETS (IMPORTANT FIX)
# ----------------------------
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
TAVILY_API_KEY = st.secrets.get("TAVILY_API_KEY", os.getenv("TAVILY_API_KEY"))


def run_newsletter_agent(goal, human_in_loop=False):

    print("\nGOAL:", goal)

    # STEP 1: PLAN
    plan = create_plan(goal)

    print("\nPLAN:")
    for step in plan:
        print("-", step)

    # STEP 2: RESEARCH (PASS API KEY)
    articles = research_news(TAVILY_API_KEY)

    # STEP 3: SUMMARIZE
    summaries = summarize_articles(articles)

    # STEP 4: WRITE
    newsletter = generate_newsletter(summaries)

    # STEP 5: CRITIC
    feedback = critique_newsletter(newsletter)

    # STEP 6: IMPROVE
    improved_newsletter = improve_newsletter(newsletter, feedback)

    # STEP 7: HTML
    html_output = markdown_to_html(improved_newsletter)

    # STEP 8: SAVE FILES
    save_output(improved_newsletter, "output/newsletter.md")
    save_output(html_output, "output/newsletter.html")

    # STEP 9: SEND (SIMULATION)
    simulate_send(improved_newsletter)

    return improved_newsletter