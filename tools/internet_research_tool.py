import requests
from bs4 import BeautifulSoup
from crewai.tools import tool


def search_internet(query: str) -> str:
    """
    Custom internet research tool that searches DuckDuckGo and extracts text content.
    
    Parameters:
        query (str): The search query string.
    
    Returns:
        str: Extracted and cleaned text content from search results.
    """
    try:
        # Use DuckDuckGo HTML search (no API key required)
        url = "https://html.duckduckgo.com/html/"
        params = {"q": query}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract result snippets
        results = []
        result_divs = soup.find_all("a", class_="result__snippet", limit=5)
        
        for snippet in result_divs:
            text = snippet.get_text(strip=True)
            if text:
                results.append(text)
        
        # If no snippets found, try alternative selectors
        if not results:
            result_links = soup.find_all("a", class_="result__a", limit=5)
            for link in result_links:
                parent = link.find_parent("div", class_="result__body")
                if parent:
                    snippet = parent.find("a", class_="result__snippet")
                    if snippet:
                        results.append(snippet.get_text(strip=True))
        
        if not results:
            return f"No results found for query: {query}"
        
        # Combine results
        combined = "\n\n".join(results[:5])
        return f"Search results for '{query}':\n\n{combined}"
    
    except requests.RequestException as e:
        return f"Error performing internet search: {str(e)}"
    except Exception as e:
        return f"Unexpected error during search: {str(e)}"


@tool("Internet Research Tool")
def get_internet_research(query: str) -> str:
    """
    Custom tool for searching the internet and retrieving information.
    
    Parameters:
        query (str): The topic or question to research online.
    
    Returns:
        str: Summarized information from internet search results.
    """
    return search_internet(query)


# Test function (uncomment to test locally)
# if __name__ == "__main__":
#     result = search_internet("latest trends in generative AI")
#     print(result)
