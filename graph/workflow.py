from agents.planner import create_plan
from agents.research import research_news
from agents.summarizer import summarize_articles
from agents.writer import generate_newsletter
from agents.critic import critique_newsletter
from agents.solver import improve_newsletter
from agents.sender import simulate_send

from tools.HTML_generator import markdown_to_html
from tools.save_file import save_output


def run_newsletter_agent(goal, human_in_loop=False):

    print("\nGOAL:")
    print(goal)

    plan = create_plan(goal)

    print("\nPLAN:")
    for step in plan:
        print("-", step)

    articles = research_news()

    summaries = summarize_articles(articles)

    newsletter = generate_newsletter(summaries)

    feedback = critique_newsletter(newsletter)

    improved_newsletter = improve_newsletter(
        newsletter,
        feedback
    )

    html_output = markdown_to_html(
        improved_newsletter
    )

    save_output(
        improved_newsletter,
        "output/newsletter.md"
    )

    save_output(
        html_output,
        "output/newsletter.html"
    )

    simulate_send(improved_newsletter)

    return improved_newsletter