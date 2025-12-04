import os
from dotenv import load_dotenv

# Import both agent systems
from pydantic_ai_agent import run_pydantic_agent
from crew import run_crew

# Load environment variables
load_dotenv()


def main():
    """
    Main function to test both PydanticAI and CrewAI agents with custom tools.
    """
    # Test queries
    queries = [
        "latest trends in generative AI",
        "current top programming languages"
    ]
    
    print("\n" + "="*80)
    print("AI AGENTS WITH CUSTOM INTERNET RESEARCH TOOLS")
    print("="*80)
    
    # Choose which agent(s) to run
    print("\nSelect which agent system to run:")
    print("1. PydanticAI Agent")
    print("2. CrewAI Multi-Agent System")
    print("3. Both (run sequentially)")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    # Get user query or use default
    print("\nEnter your research query (or press Enter to use default):")
    user_query = input("> ").strip()
    
    if not user_query:
        user_query = queries[0]
        print(f"Using default query: {user_query}")
    
    # Run selected agent(s)
    if choice == "1":
        run_pydantic_agent(user_query)
    
    elif choice == "2":
        run_crew(user_query)
    
    elif choice == "3":
        # Run PydanticAI first
        run_pydantic_agent(user_query)
        
        # Then run CrewAI
        print("\n" + "="*80)
        print("Now running CrewAI Multi-Agent System...")
        print("="*80 + "\n")
        run_crew(user_query)
    
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
