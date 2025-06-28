## Importing libraries and files
from crewai import Task
from agents import researcher, support_agent
from tools import search_tool, pdf_tool

## Creating a research task
research_task = Task(
    description=(
        "Analyze the user's query: {query}. "
        "Use the search tool to find relevant information and provide a detailed analysis of the blood test report."
    ),
    expected_output=(
        "A comprehensive report detailing the analysis of the blood test, including any abnormalities, potential causes, and recommendations for further tests."
    ),
    agent=researcher,
    tools=[search_tool, pdf_tool],
    async_execution=False,
)

## Creating a support task
support_task = Task(
    description=(
        "Review the research findings and provide a clear, empathetic, and actionable summary to the user."
    ),
    expected_output=(
        "A user-friendly summary of the blood test analysis, including lifestyle and dietary recommendations, and advice on when to consult a healthcare professional."
    ),
    agent=support_agent,
    tools=[search_tool, pdf_tool],
    async_execution=False,
)