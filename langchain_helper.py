
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
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

    # Execute chains sequentially
    name_result = name_chain({"industry": industry})
    pitch_result = pitch_chain({"startup_name": name_result["startup_name"]})
    
    return {
        "startup_name": name_result["startup_name"],
        "pitch": pitch_result["pitch"]
    }

def generate_ideal_location(industry):
    location_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Suggest the best city/country to launch a {industry} startup where customer reach, startup ecosystem, and growth opportunities are high. Provide 2-3 options with brief reasons."
    )
    
    location_chain = LLMChain(llm=llm, prompt=location_prompt, output_key="location")
    result = location_chain({"industry": industry})
    return result["location"]

def generate_cost_estimate(industry):
    cost_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Give an approximate cost breakdown to start a {industry} startup, including setup, salaries, tools, and marketing. Give numbers in USD and break it down into categories."
    )
    
    cost_chain = LLMChain(llm=llm, prompt=cost_prompt, output_key="cost")
    result = cost_chain({"industry": industry})
    return result["cost"]

def generate_target_audience(industry):
    audience_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Describe the ideal customer for a {industry} startup. Include age group, profession, location, income level, and behavior patterns."
    )
    
    audience_chain = LLMChain(llm=llm, prompt=audience_prompt, output_key="audience")
    result = audience_chain({"industry": industry})
    return result["audience"]

def generate_tech_stack(industry):
    tech_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Recommend the essential tech stack and SaaS tools needed for a {industry} startup. Include programming languages, frameworks, databases, and third-party services."
    )
    
    tech_chain = LLMChain(llm=llm, prompt=tech_prompt, output_key="tech_stack")
    result = tech_chain({"industry": industry})
    return result["tech_stack"]

def generate_business_model(industry):
    model_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Suggest suitable monetization strategies for a {industry} startup. Include revenue models like freemium, SaaS, subscriptions, marketplace fees, etc."
    )
    
    model_chain = LLMChain(llm=llm, prompt=model_prompt, output_key="business_model")
    result = model_chain({"industry": industry})
    return result["business_model"]

def generate_competitor_analysis(industry):
    competitor_prompt = PromptTemplate(
        input_variables=['industry'],
        template="List 3 known competitors in the {industry} space with a one-line description of what makes each unique or different."
    )
    
    competitor_chain = LLMChain(llm=llm, prompt=competitor_prompt, output_key="competitors")
    result = competitor_chain({"industry": industry})
    return result["competitors"]

def generate_launch_roadmap(industry):
    roadmap_prompt = PromptTemplate(
        input_variables=['industry'],
        template="Provide a 6-month startup roadmap for a {industry} company with monthly milestones including development, marketing, and business goals."
    )
    
    roadmap_chain = LLMChain(llm=llm, prompt=roadmap_prompt, output_key="roadmap")
    result = roadmap_chain({"industry": industry})
    return result["roadmap"]

def generate_domain_names(startup_name, industry):
    domain_prompt = PromptTemplate(
        input_variables=['startup_name', 'industry'],
        template="Suggest 3 available domain names for a {industry} startup named '{startup_name}'. Make them brandable and memorable."
    )
    
    domain_chain = LLMChain(llm=llm, prompt=domain_prompt, output_key="domains")
    result = domain_chain({"startup_name": startup_name, "industry": industry})
    return result["domains"]

def generate_one_liner_pitch(startup_name, industry):
    pitch_prompt = PromptTemplate(
        input_variables=['startup_name', 'industry'],
        template="Create a short, catchy one-liner pitch for a {industry} startup named '{startup_name}'. Make it memorable and impactful."
    )
    
    pitch_chain = LLMChain(llm=llm, prompt=pitch_prompt, output_key="one_liner")
    result = pitch_chain({"startup_name": startup_name, "industry": industry})
    return result["one_liner"]
