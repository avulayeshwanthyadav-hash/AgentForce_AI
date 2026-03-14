# Agentforce-Based Intelligent Sales Assistant & Proposal Automation

An AI-powered WhatsApp chatbot that integrates with Salesforce to automate sales workflows such as **account summarization, opportunity analysis, personalized email generation, and proposal creation**.

The system uses AI models from **Groq** and messaging services from **Twilio** to provide real-time responses directly on WhatsApp.

---

# Project Overview

Sales representatives often spend significant time manually:

- Searching CRM records
- Analyzing opportunities
- Writing follow-up emails
- Preparing sales proposals

This project introduces an **AI-powered sales assistant chatbot** that automates these tasks using CRM data.

The chatbot connects to Salesforce, analyzes account data, and responds to user queries through **WhatsApp**.

---

# Features

## 1. Account History Summarization

Automatically reads account information from Salesforce and generates a concise summary including:

- Customer profile
- Industry
- Relationship description
- Business interests

### Example Command


summary ABC Corp


---

## 2. Opportunity Analysis

The system analyzes opportunity data such as:

- Deal stage
- Deal value
- Customer engagement
- Potential risks

### Example Command


opportunity ABC Corp


The AI provides:

- Win probability
- Risk factors
- Recommended sales strategy

---

## 3. Next Best Action Recommendation

Based on CRM insights, the AI suggests actions such as:

- Scheduling a meeting
- Sending pricing details
- Providing a product demo
- Following up with the client

---

## 4. Personalized Email Generation

The chatbot automatically generates professional sales emails based on CRM context.

### Example Command


email ABC Corp


### Example Output


Subject: Follow-up on AI Solutions Discussion

Dear ABC Corp Team,

Thank you for attending our recent product demonstration.
We believe our AI-powered solutions can significantly enhance
your operational efficiency. Please let us know a convenient
time for a follow-up discussion.


---

## 5. Automated Proposal Generation

The system generates a customized proposal including:

- Customer overview
- Problem statement
- Proposed solution
- Pricing details
- Implementation timeline

### Example Command


proposal ABC Corp


---

# System Architecture


User (WhatsApp)
↓
Twilio WhatsApp API
↓
Python Backend (Flask)
↓
Salesforce CRM
↓
Groq AI Model
↓
Response sent back to WhatsApp


---

# Technologies Used

| Technology | Purpose |
|-----------|--------|
| Python | Backend development |
| Flask | Web server |
| Salesforce CRM | Customer and opportunity data |
| Twilio | WhatsApp messaging integration |
| Groq API | AI text generation |
| Simple-Salesforce | Salesforce API integration |
| Ngrok | Public webhook for local server |

---

# Running the Application

## 1. Start the Server


python app.py


## 2. Expose the Server Using Ngrok


ngrok http 5000


## 3. Configure Twilio Webhook

Use the generated ngrok URL as the Twilio webhook.

Example:


https://your-ngrok-url/whatsapp


---

# Example WhatsApp Commands


summary ABC Corp
opportunity ABC Corp
email ABC Corp
proposal ABC Corp


---

# Conclusion

This project demonstrates how **AI + CRM + messaging platforms** can be combined to build an **intelligent sales assistant** that improves productivity and automates repetitive sales tasks.

The chatbot acts as a **virtual sales assistant**, enabling real-time CRM insights and automated customer communication directly through WhatsApp.
