import os
from tavily import TavilyClient

# Get API key safely
TAVILY_API_KEY = os.getenv("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")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing. Set it in environment variables.")

client = TavilyClient(api_key=TAVILY_API_KEY)


def search_ai_news(query):
    response = client.search(
        query=query,
        max_results=7
    )
    return response["results"]