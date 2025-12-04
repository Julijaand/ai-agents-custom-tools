# AI Agents with Custom Internet Research Tools

Practice exercise demonstrating both **PydanticAI** and **CrewAI** agents with custom-built internet research capabilities.

## Overview

This project implements two agent systems that use a custom internet research tool (no pre-built framework tools):

1. **PydanticAI Agent**: Single agent that searches and summarizes information
2. **CrewAI Multi-Agent System**: Two-agent collaboration
   - **Research Agent**: Gathers information using the custom tool
   - **Summarizer Agent**: Analyzes and summarizes research findings

## Architecture

### Custom Tool: Internet Research
- Built from scratch using `requests` and `BeautifulSoup4`
- Searches DuckDuckGo (no API key required)
- Extracts and cleans search result snippets
- Returns formatted research data

### PydanticAI Implementation
- Single agent with custom tool registration
- Direct query → search → summarize workflow
- Uses Groq's Llama 3.3 70B model

### CrewAI Implementation
- **Research Agent**: Uses custom tool to gather data
- **Summarizer Agent**: Processes raw findings into structured summaries
- Sequential task execution with context passing

## Project Structure

```
7_5_practice_exercise_ai_agents_with_custom_tools/
├── agents/
│   ├── research_agent.py       # CrewAI research agent
│   └── summarizer_agent.py     # CrewAI summarizer agent
├── tasks/
│   ├── research_task.py        # Research task definition
│   └── summarize_task.py       # Summarization task definition
├── tools/
│   └── internet_research_tool.py  # Custom internet search tool
├── pydantic_ai_agent.py        # PydanticAI agent implementation
├── crew.py                     # CrewAI crew orchestration
├── main.py                     # Main entry point
├── requirements.txt            # Python dependencies
├── env_template.txt            # Environment variable template
└── README.md                   # This file
```

## Setup

### 1. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `env_template.txt` to `.env` and add your API key:

```powershell
Copy-Item env_template.txt .env
```

Edit `.env`:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

Get a free Groq API key at: https://console.groq.com/

## Usage

### Run Interactive Mode

```powershell
python main.py
```

You'll be prompted to:
1. Choose which agent system to run (PydanticAI, CrewAI, or both)
2. Enter your research query

### Example Queries

- "latest trends in generative AI"
- "current top programming languages"
- "recent developments in quantum computing"
- "best practices for microservices architecture"

### Run Individual Components

**Test PydanticAI Agent:**
```powershell
python pydantic_ai_agent.py
```

**Test Custom Tool:**
```powershell
python -c "from tools.internet_research_tool import search_internet; print(search_internet('Python 3.13 features'))"
```

## How It Works

### PydanticAI Flow
1. User provides query
2. Agent receives query and decides to use `search_internet_tool`
3. Tool fetches internet results
4. Agent analyzes results and generates summary
5. Final answer returned to user

### CrewAI Flow
1. User provides topic
2. **Research Agent** executes `research_task`
   - Uses `get_internet_research` tool to fetch data
   - Returns detailed findings
3. **Summarizer Agent** executes `summarize_task`
   - Receives research findings as context
   - Creates structured summary with key insights
4. Final polished summary returned to user

## Custom Tool Details

**File:** `tools/internet_research_tool.py`

**Features:**
- No API key required (uses DuckDuckGo HTML search)
- Parses HTML with BeautifulSoup
- Extracts up to 5 relevant snippets
- Error handling for network issues
- Clean, formatted output

**CrewAI decorator:**
```python
@tool("Internet Research Tool")
def get_internet_research(query: str) -> str:
    """Custom tool for searching the internet"""
    return search_internet(query)
```

**PydanticAI registration:**
```python
@pydantic_agent.tool
def search_internet_tool(query: str) -> str:
    """Search the internet for information"""
    return search_internet(query)
```

## Expected Output

### PydanticAI Agent
```
==============================================================
PydanticAI Agent - Researching: latest trends in generative AI
==============================================================

[Agent calls search_internet_tool]
[Agent analyzes results]

--- PydanticAI Agent Result ---
Based on recent search results, here are the latest trends in generative AI:

1. **Multimodal AI Models**: Integration of text, image, and video...
2. **AI Agents and Automation**: Growing use of autonomous agents...
[...]
```

### CrewAI Multi-Agent System
```
==============================================================
CrewAI Multi-Agent System - Researching: latest trends in generative AI
==============================================================

[Research Agent gathers information]
Agent: Internet Research Specialist
Task: Research the following topic...

[Summarizer Agent creates summary]
Agent: Information Summarizer and Analyst
Task: Take the raw research findings...

==============================================================
Final Result:
==============================================================

**Executive Summary:**
Generative AI is rapidly evolving with multimodal capabilities...

**Key Points:**
- Advanced language models with improved reasoning
- Integration of vision and language understanding
[...]
```

## Troubleshooting

### Import Errors
Ensure virtual environment is activated and all packages installed:
```powershell
pip install -r requirements.txt
```

### API Key Issues
- Verify `.env` file exists and contains valid `GROQ_API_KEY`
- Check API key has sufficient quota at https://console.groq.com/

### Network/Search Issues
- Tool uses DuckDuckGo which doesn't require authentication
- If search fails, check internet connection
- Some networks may block web scraping (try different network)

### LiteLLM Not Available
Install litellm:
```powershell
pip install litellm
```

## Learning Outcomes

This exercise demonstrates:
✅ Building custom tools from scratch (no framework dependencies)
✅ Integrating tools with both PydanticAI and CrewAI frameworks
✅ Single-agent vs multi-agent architectures
✅ Task orchestration and context passing between agents
✅ Real-world internet research automation
✅ Proper error handling and environment configuration

## Next Steps

**Enhancements you can try:**
- Add more specialized agents (fact-checker, citation formatter)
- Implement caching to avoid redundant searches
- Add support for other search engines (Google Custom Search, Bing)
- Create a Streamlit UI for interactive queries
- Add web scraping for deeper content extraction
- Implement result ranking and relevance scoring

## License

Educational project for learning AI agent development.