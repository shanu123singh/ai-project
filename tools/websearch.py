from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("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")
)

def search_ai_news(query):

    response = client.search(
        query=query,
        max_results=7
    )

    return response["results"]