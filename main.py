
import langchain

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()  # Load env variables
api_key = os.getenv("OPENAI_API_KEY")
import openai

# Initialize LLM
llm = OpenAI(temperature=0.3)

# Print a simple LLM response
print(llm.predict("What is the meaning of life?"))

# Define a correct Prompt Template
prompt = PromptTemplate(
    input_variables=["place"],
    template="What is the capital of {place}?"
)

# Create LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Define cities list
cities = ["Pakistan", "USA", "India"]

# Loop through cities and get LLM output
for city in cities:
    output = chain.run(place=city)
    print(output)
