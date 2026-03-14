## Agentforce-Based Intelligent Sales Assistant & Proposal Automation

An AI-powered WhatsApp chatbot that integrates with Salesforce to automate sales workflows such as account summarization, opportunity analysis, personalized email generation, and proposal creation.

The system uses AI models from Groq and messaging services from Twilio to provide real-time responses directly on WhatsApp.

## Project Overview

Sales representatives often spend significant time manually searching through CRM records, analyzing opportunities, writing follow-up emails, and preparing proposals.

This project introduces an AI-powered sales assistant chatbot that automates these tasks using CRM data.

The chatbot connects to Salesforce, analyzes account data, and responds to user queries through WhatsApp.

## Features
<!-- 1. Account History Summarization -->

Automatically reads account information from Salesforce and generates a concise summary including:

Customer profile

Industry

Relationship description

Business interests

Example command:

summary ABC Corp
<!-- 2. Opportunity Analysis -->

The system analyzes opportunity data such as:

Deal stage

Deal value

Customer engagement

Potential risks

Example command:

opportunity ABC Corp

The AI provides:

Win probability

Risk factors

Recommended sales strategy

<!-- 3. Next Best Action Recommendation -->

Based on CRM insights, the AI suggests actions like:

Scheduling a meeting

Sending pricing details

Providing product demo

Following up with the client

<!-- 4. Personalized Email Generation -->

The chatbot automatically generates professional emails based on CRM context.

Example:

email ABC Corp

Output example:

Subject: Follow-up on AI Solutions Discussion

Dear ABC Corp Team,

Thank you for attending our recent product demonstration...
<!-- 5. Automated Proposal Generation -->

The system generates a customized proposal including:

Customer overview

Problem statement

Proposed solution

Pricing details

Implementation timeline

## Example command:

proposal ABC Corp
System Architecture
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

Technologies Used
Technology	        Purpose
Python	            Backend development
Flask	            Web server
Salesforce CRM	    Customer and opportunity data
Twilio	            WhatsApp messaging integration
Groq API	        AI text generation
Simple-Salesforce	Salesforce API integration
Ngrok	            Public webhook for local server


## Project Structure
sales_ai_whatsapp_bot
│
├── app.py
├── chatbot.py
├── ai_tools.py
├── salesforce_api.py
├── .env
├── requirements.txt
└── README.md


## Running the Application

Start the server:

python app.py

Expose the server using ngrok:

ngrok http 5000

Use the generated URL as the Twilio webhook.
