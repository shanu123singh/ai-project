def generate_newsletter(summaries):

    newsletter = "# Weekly AI Agent Newsletter\n\n"

    for idx, article in enumerate(summaries, start=1):

        newsletter += f"## {idx}. {article['title']}\n\n"

        newsletter += f"{article['summary']}\n\n"

        newsletter += f"Read More: {article['url']}\n\n"

        newsletter += "---\n\n"

    return newsletter