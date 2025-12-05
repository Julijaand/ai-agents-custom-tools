from crewai import Agent, LLM

# Initialize the LLM
# llm = LLM(
#     model="groq/llama-3.3-70b-versatile",
#     temperature=0.5
# )

# option to use claude agent
llm = LLM(
    model="anthropic/claude-3-5-sonnet-20241022",
    temperature=0.3
)

summarizer_agent = Agent(
    role="Information Summarizer and Analyst",
    goal=(
        "Take raw research data and transform it into clear, concise, and well-structured summaries. "
        "Extract key insights, identify trends, and present information in an easy-to-understand format."
    ),
    backstory=(
        "You are a skilled analyst and writer who specializes in distilling complex information into "
        "digestible summaries. You have a gift for identifying the most important points and presenting "
        "them in a logical, engaging manner. Your summaries are always accurate, insightful, and valuable."
    ),
    llm=llm,
    tools=[],
    verbose=True
)
