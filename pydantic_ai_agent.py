import os
from dotenv import load_dotenv

# Pydantic AI imports
from pydantic_ai import Agent
from pydantic_ai.settings import ModelSettings

# Import custom tool function
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tools.internet_research_tool import search_internet

load_dotenv()

# Create PydanticAI agent using Groq model (without tool use - manual approach)
research_agent = Agent(
    model="groq:llama-3.3-70b-versatile",
    model_settings=ModelSettings(temperature=0.3),
    output_type=str,
    system_prompt=(
        "You are an expert internet researcher and analyst. "
        "You will be provided with search results from the internet. "
        "Analyze the information and provide a comprehensive, well-structured summary "
        "with key insights, trends, and important findings. "
        "Format your response with clear sections and bullet points."
    )
)


def run_pydantic_agent(user_query: str):
    """
    Run the PydanticAI agent with a user query.
    Uses a two-step approach:
    1. Call custom search tool directly
    2. Send results to agent for analysis
    
    Args:
        user_query: The question or topic to research.
    """
    print(f"\n{'='*60}")
    print(f"PydanticAI Agent - Researching: {user_query}")
    print(f"{'='*60}\n")
    
    try:
        # Step 1: Use custom tool to search internet
        print(f"[Step 1/2] Searching the internet for: {user_query}")
        search_results = search_internet(user_query)
        print(f"[Step 1/2] Search completed. Retrieved results.\n")
        
        # Step 2: Send search results to agent for analysis
        print(f"[Step 2/2] Analyzing search results with AI agent...")
        analysis_prompt = f"""
Based on the following internet search results about "{user_query}":

{search_results}

Please provide a comprehensive analysis with:
1. **Summary**: Overview of key findings
2. **Main Trends**: Notable patterns and developments
3. **Key Insights**: Important takeaways
4. **Conclusion**: Brief summary of the most significant points

Use clear formatting with headers and bullet points.
"""
        
        result = research_agent.run_sync(analysis_prompt)
        
        print(f"\n--- PydanticAI Agent Analysis ---")
        print(result.output)
        print(f"\n{'='*60}\n")
        
        return result.output
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# Test function
def test_agent():
    """Test the PydanticAI agent with a sample query."""
    query = "latest trends in generative AI"
    run_pydantic_agent(query)


if __name__ == "__main__":
    test_agent()
