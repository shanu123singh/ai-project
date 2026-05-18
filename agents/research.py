from tools.websearch import search_ai_news

def research_news():

    query = "Latest AI agent news this week"

    articles = search_ai_news(query)

    return articles