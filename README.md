# Agentforce-Based Intelligent Sales Assistant & Proposal Automation

An AI-powered sales chatbot that integrates with Salesforce CRM to automate sales intelligence tasks such as account summarization, opportunity analysis, email generation, and proposal creation.
This project simulates an AI assistant similar to Agentforce by connecting to Salesforce CRM data and using a Large Language Model to generate insights and sales documents.

---

## Features

- Account History Summarization  
- Opportunity Analysis and Deal Insights  
- Next Best Action Recommendation  
- Automated Sales Email Generation  
- Automated Sales Proposal Generation  
- Chatbot Interface for interacting with CRM data

---

## Technologies Used

- Python
- FastAPI
- Groq API (Llama 3 model)
- Salesforce REST API
- simple-salesforce Python library
- dotenv for environment variables

CRM platform used: Salesforce

---

## System Architecture

User  
↓  
Chatbot Interface  
↓  
Python Backend  
↓  
Salesforce CRM API  
↓  
AI Model (Groq Llama)

---

## Project Structure


sales_ai_chatbot
│
├── app.py
├── chatbot.py
├── ai_tools.py
├── salesforce_api.py
├── .env
└── README.md


---

## Setup Instructions

### 1. Clone the repository
# Agentforce-Based Intelligent Sales Assistant & Proposal Automation

An AI-powered sales chatbot that integrates with Salesforce CRM to automate sales intelligence tasks such as account summarization, opportunity analysis, email generation, and proposal creation.

This project simulates an AI assistant similar to Agentforce by connecting to Salesforce CRM data and using a Large Language Model to generate insights and sales documents.

---

## Features

- Account History Summarization  
- Opportunity Analysis and Deal Insights  
- Next Best Action Recommendation  
- Automated Sales Email Generation  
- Automated Sales Proposal Generation  
- Chatbot Interface for interacting with CRM data

---

## Technologies Used

- Python
- FastAPI
- Groq API (Llama 3 model)
- Salesforce REST API
- simple-salesforce Python library
- dotenv for environment variables

CRM platform used: Salesforce

---

## System Architecture

User  
↓  
Chatbot Interface  
↓  
Python Backend  
↓  
Salesforce CRM API  
↓  
AI Model (Groq Llama)

---

## Project Structure


sales_ai_chatbot
│
├── app.py
├── chatbot.py
├── ai_tools.py
├── salesforce_api.py
├── .env
└── README.md


---

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/yourusername/sales-ai-chatbot.git

cd sales-ai-chatbot


---

### 2. Install dependencies


pip install simple-salesforce fastapi uvicorn python-dotenv groq


---

### 3. Create Salesforce Developer Account

Go to:

https://developer.salesforce.com/signup

After signup, note the following credentials:

- Username
- Password
- Security Token

To get the token:

Settings → Reset My Security Token

---

### 4. Get Groq API Key

Visit:

https://console.groq.com

Create an API key.

---

### 5. Configure Environment Variables

Create `.env` file:


SF_USERNAME=your_salesforce_username
SF_PASSWORD=your_salesforce_password
SF_TOKEN=your_salesforce_token

GROQ_API_KEY=your_groq_api_key


---

## Running the Chatbot

Start the FastAPI server:


uvicorn app:app --reload


Open in browser:


http://127.0.0.1:8000/chat?message=show
 summary


---

## Example Chatbot Queries


show summary of ABC Corp
analyze opportunity for ABC Corp
generate email
generate proposal


---

## Example Output

Account Summary:

ABC Corp is a technology company interested in AI-based automation solutions with an active opportunity valued at $45,000.

Sales Email:

Subject: Follow-up on AI Platform Implementation

Hi John,

Thank you for discussing ABC Corp's AI platform implementation with us. We believe our solution can significantly improve automation and efficiency for your organization.

Best regards  
Sales Team

---

## Future Enhancements

- ChatGPT-style web UI  
- PDF proposal generation  
- Multi-agent AI system  
- Slack / Teams integration  
- Sales forecasting model  

---

## Author

Sunny

git clone https://github.com/yourusername/sales-ai-chatbot.git

cd sales-ai-chatbot


---

### 2. Install dependencies


pip install simple-salesforce fastapi uvicorn python-dotenv groq


---

### 3. Create Salesforce Developer Account

Go to:

https://developer.salesforce.com/signup

After signup, note the following credentials:

- Username
- Password
- Security Token

To get the token:

Settings → Reset My Security Token

---

### 4. Get Groq API Key

Visit:

https://console.groq.com

Create an API key.

---

### 5. Configure Environment Variables

Create `.env` file:


SF_USERNAME=your_salesforce_username
SF_PASSWORD=your_salesforce_password
SF_TOKEN=your_salesforce_token

GROQ_API_KEY=your_groq_api_key


---

## Running the Chatbot

Start the FastAPI server:


uvicorn app:app --reload


Open in browser:


http://127.0.0.1:8000/chat?message=show
 summary


---

## Example Chatbot Queries


show summary of ABC Corp
analyze opportunity for ABC Corp
generate email
generate proposal


---

## Example Output

Account Summary:

ABC Corp is a technology company interested in AI-based automation solutions with an active opportunity valued at $45,000.

Sales Email:

Subject: Follow-up on AI Platform Implementation

Hi John,

Thank you for discussing ABC Corp's AI platform implementation with us. We believe our solution can significantly improve automation and efficiency for your organization.

Best regards  
Sales Team

---

## Future Enhancements

- ChatGPT-style web UI  
- PDF proposal generation  
- Multi-agent AI system  
- Slack / Teams integration  
- Sales forecasting model  

---

## Author

Sunny
