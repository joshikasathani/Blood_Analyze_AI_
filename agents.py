## Importing libraries and files
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import search_tool, pdf_tool

load_dotenv()

### Loading LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.1,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a senior researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="To provide the most accurate and up-to-date information on blood test reports to the user: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "With a Ph.D. in medical research and over 20 years of experience, you are a leading expert in interpreting blood test results."
        "Your skills in analyzing complex medical data and staying current with the latest research are unparalleled."
        "You are known for your meticulous attention to detail and your ability to provide clear, evidence-based insights."
    ),
    tools=[search_tool, pdf_tool],
    llm=llm,
    allow_delegation=True
)

# Creating a support agent
support_agent = Agent(
    role="Health Support Agent",
    goal="To provide compassionate and clear explanations of the research findings to the user.",
    verbose=True,
    memory=True,
    backstory=(
        "As a former registered nurse with a passion for patient education, you excel at breaking down complex medical information into easy-to-understand language."
        "You are known for your empathy, patience, and ability to create a supportive and reassuring environment for users."
        "Your goal is to empower users with the knowledge they need to understand their health better."
    ),
    tools=[search_tool, pdf_tool],
    llm=llm,
    allow_delegation=True
)
