from tavily import TavilyClient

def research_news(api_key):

    client = TavilyClient(api_key=api_key)

    response = client.search(
        query="latest AI news",
        max_results=7
    )

    return response["results"]