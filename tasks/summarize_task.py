from crewai import Task
from agents.summarizer_agent import summarizer_agent


summarize_task = Task(
    description=(
        "Take the raw research findings and create a clear, well-structured summary. "
        "Analyze the information, identify the most important points, and organize them logically. "
        "Create a concise yet comprehensive summary that highlights key trends, insights, and takeaways. "
        "Make the summary easy to understand for someone who wants to quickly grasp the main points."
    ),
    expected_output=(
        "A polished summary report with:\n"
        "- Executive summary (2-3 sentences overview)\n"
        "- Key Points (3-5 main findings in bullet points)\n"
        "- Trends and Insights (notable patterns or developments)\n"
        "- Conclusion (brief takeaway or recommendation)\n"
        "- Well-organized, professional formatting"
    ),
    agent=summarizer_agent
)
