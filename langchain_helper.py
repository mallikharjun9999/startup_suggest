import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment.")

llm = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192",
    api_key=api_key
)

def generate_startup_name_and_pitch(industry):
    name_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Generate a unique and brandable startup name for a company in the {industry} industry. Only return the name."
    )
    pitch_prompt = PromptTemplate(
        input_variables=['startup_name'],
        template="Write a short, compelling elevator pitch (2-3 sentences) for a startup named {startup_name}."
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="startup_name")
    pitch_chain = LLMChain(llm=llm, prompt=pitch_prompt, output_key="pitch")

    chain = SequentialChain(
        chains=[name_chain, pitch_chain],
        input_variables=["industry"],
        output_variables=["startup_name", "pitch"]
    )

    return chain({"industry": industry})
