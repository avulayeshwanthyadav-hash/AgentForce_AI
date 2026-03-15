from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_llm(prompt):
    """
    Send a prompt to the LLM and return its response
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def summarize_account(data):
    if not data:
        return "No account data available."
    accounts = "\n".join([f"{a['Name']} ({a.get('Industry','')}) - {a.get('Phone','')}" for a in data])
    prompt = f"Summarize this CRM customer data:\n{accounts}\nInclude: customer profile, relationship status."
    return ask_llm(prompt)


def analyze_opportunity(data):
    if not data:
        return "No opportunity data available."
    # Added "Be concise" and "Keep it under 1000 characters"
    prompt = f"Analyze these sales opportunities:\n{data}\nProvide: win probability, risks, recommendations. BE CONCISE. Keep the response under 1000 characters."
    return ask_llm(prompt)

def generate_email(account, contact_name):

    prompt = f"""
    Write a professional sales follow-up email.

    Customer Company: {account}
    Contact Person: {contact_name}

    Requirements:
    - Address the person by name
    - Keep it under 800 characters
    - Professional tone
    """

    return ask_llm(prompt)


def generate_proposal(account):
    prompt = f"""
    Create a CONCISE sales proposal for {account}.
    Structure:
    * Overview
    * Challenge
    * Solution
    * Price
    Keep it under 1400 characters. Use bullet points.
    """
    return ask_llm(prompt)

def summarize_contacts(data):
    if not data:
        return "No contacts available for this account."
    contacts_list = "\n".join([f"👤 {c['Name']} - {c.get('Title','')}" for c in data])
    return f"*Contacts for Account:*\n\n{contacts_list}\n\nReply with 'email [Name]' to draft a message."

def detect_intent(message):

    prompt = f"""
    Classify the user request.

    Message: {message}

    Return ONLY one word from this list:

    summary
    opportunity
    send-email
    email
    proposal
    contacts
    recent-opps
    dashboard
    purchased-products
    forecast
    compare
    create-opportunity
    meeting-prep
    """

    return ask_llm(prompt).strip().lower()


def extract_account(message):

    prompt = f"""
    Extract the company name from this message.

    Message: {message}

    Return ONLY the company name.
    """

    return ask_llm(prompt).strip()


def predict_risk(data):

    prompt = f"""
    Analyze this opportunity data.

    {data}

    Provide:
    Risk Score (Low/Medium/High)
    Reasons
    Recommended actions
    """

    return ask_llm(prompt)


def prepare_meeting(account, data):

    prompt = f"""
    Prepare a meeting brief for {account}.

    Opportunity Data:
    {data}

    Provide:
    Company overview
    Talking points
    Strategy
    """

    return ask_llm(prompt)


def sales_forecast(data):

    prompt = f"""
    Based on this pipeline data:

    {data}

    Generate a quarterly sales forecast.
    Include expected revenue and top deals.
    """

    return ask_llm(prompt)

def summarize_products(data):
    if not data:
        return "No products found for this opportunity."
    
    details = "\n".join([f"- {p['Product2']['Name']}: {p['Quantity']} x ${p['UnitPrice']}" for p in data])
    return f"*Items being purchased:*\n{details}\n\n*Total Value:* ${data[0]['TotalPrice'] if data else 0}"

def format_automated_email(to_name, body_content):
    """
    Wraps the AI text into a formal email structure
    """
    return f"""
    Subject: Follow-up from our Sales Team
    
    Dear {to_name},
    
    {body_content}
    
    Best regards,
    The AgentForce Team
    """

def extract_contact_name(message):

    prompt = f"""
    Extract the contact person's name from this message.

    Message: {message}

    Return ONLY the name if present.
    If no name exists return NONE.
    """

    name = ask_llm(prompt).strip()

    if name.upper() == "NONE":
        return None

    return name
