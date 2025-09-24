from langchain_tavily import TavilySearch
from langchain_core.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY not found! "
        "Set it in your .env file for local dev or as an environment variable in production."
    )

@tool
def web_search(query:str) -> dict:
    """Use this tool to search the web for recent information and retrieve relevant content."""
    search = TavilySearch(tavily_api_key=TAVILY_API_KEY,max_results=1,include_raw_content=True,include_images=True,search_depth="advanced",topic="general")
    result = search.invoke({"query": query})
    texts = [r['content'] for r in result['results']]
    image_urls = result.get('images', [])
    return ({
        "content":"\n".join(texts),
        "images":image_urls
    })
if __name__ == "__main__":
    query = "Latest advancements in AI technology"
    print(web_search.invoke(query))