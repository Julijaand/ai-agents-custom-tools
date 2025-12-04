from crewai import Task
from agents.research_agent import research_agent


research_task = Task(
    description=(
        "Research the following topic thoroughly using internet search: {topic}. "
        "Use the internet research tool to gather comprehensive information. "
        "Collect data on current trends, recent developments, key facts, and important insights. "
        "Provide detailed findings with relevant information from your search."
    ),
    expected_output=(
        "A detailed research report containing:\n"
        "- Key findings and facts about the topic\n"
        "- Current trends and recent developments\n"
        "- Important statistics or data points\n"
        "- Relevant insights from search results\n"
        "- Raw information organized by subtopics"
    ),
    agent=research_agent
)
