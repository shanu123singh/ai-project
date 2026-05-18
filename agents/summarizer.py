def summarize_articles(articles):

    summaries = []

    for article in articles:

        summary = f"""
• Latest AI update about {article['title']}
• Important developments in AI agents
• New technology and trends discussed
"""

        summaries.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary
        })

    return summaries