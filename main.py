import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

serp_api_key = os.getenv("SERPAPI_API_KEY")
if not serp_api_key:
    os.environ["SERPAPI_API_KEY"] = "your-serpapi-key-here"  # Replace with actual key

# Initialize LLM
llm = OpenAI(temperature=0.3)

# Initialize search wrapper
search = SerpAPIWrapper()

# Define search tool
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="A tool to search Google for information."
)


print("🔍 Searching Google...")
try:
    search_result = search_tool.run("Who is the president of the USA?")
    print("✅ Search Result:", search_result)
except Exception as e:
    print("❌ Search Failed:", e)

# Define AI Agent with tools
agent = initialize_agent(
    tools=[search_tool],  
    llm=llm,  
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  
    verbose=True  
)

# **Using AI Agent in your project**
cities = ["Pakistan", "USA", "India"]

for city in cities:
    question = f"What is the capital of {city}?"
    response = agent.run(question)
    print(f"📍 {city} → {response}")
