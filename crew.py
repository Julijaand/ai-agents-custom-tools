from crewai import Crew
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from tasks.research_task import research_task
from tasks.summarize_task import summarize_task

# Set context dependency after all imports
summarize_task.context = [research_task]


research_crew = Crew(
    agents=[research_agent, summarizer_agent],
    tasks=[research_task, summarize_task],
    verbose=True
)


def run_crew(topic: str):
    """
    Run the research crew with a given topic.
    
    Args:
        topic: The topic or question to research.
    
    Returns:
        The final summarized result from the crew.
    """
    print(f"\n{'='*60}")
    print(f"CrewAI Multi-Agent System - Researching: {topic}")
    print(f"{'='*60}\n")
    
    result = research_crew.kickoff(inputs={"topic": topic})
    
    print(f"\n{'='*60}")
    print("Final Result:")
    print(f"{'='*60}")
    print(result)
    
    return result
