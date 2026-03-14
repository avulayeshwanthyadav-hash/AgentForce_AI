from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content


def summarize_account(data):

    prompt = f"""
    Summarize this CRM customer data.

    {data}

    Include:
    customer profile
    relationship status
    """

    return ask_llm(prompt)


def analyze_opportunity(data):

    prompt = f"""
    Analyze this sales opportunity.

    {data}

    Provide:
    win probability
    risks
    recommendations
    """

    return ask_llm(prompt)


def generate_email(account):

    prompt = f"""
    Write a professional sales follow-up email for {account}.
    """

    return ask_llm(prompt)


def generate_proposal(account):

    prompt = f"""
    Create a sales proposal for {account}.

    Include:
    customer overview
    problem
    solution
    pricing
    implementation plan
    """

    return ask_llm(prompt)