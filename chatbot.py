import logging
from email_service import send_sales_email
from salesforce_api import (
    connect_salesforce,
    create_quote,
    get_account,
    get_opportunity,
    get_contacts,
    get_opportunity_products,
    get_pipeline,
    create_opportunity,
    compare_accounts
)

from ai_tools import (
    summarize_account,
    analyze_opportunity,
    generate_email,
    generate_proposal,
    summarize_contacts,
    detect_intent,
    extract_account,
    predict_risk,
    prepare_meeting,
    sales_forecast,
    summarize_products,
    extract_contact_name
)

sf = connect_salesforce()

conversation_memory = {}

logging.basicConfig(level=logging.INFO)


def chatbot(message):

    intent = detect_intent(message)

    account = extract_account(message)

    if not account:
        account = conversation_memory.get("last_account", "ABC Corp")

    conversation_memory["last_account"] = account


# SUMMARY
    if intent == "summary":

        data = get_account(sf, account)

        return summarize_account(data)


# OPPORTUNITY ANALYSIS
    elif intent == "opportunity":

        data = get_opportunity(sf, account)

        return analyze_opportunity(data)


# EMAIL
    elif intent == "email":

        return generate_email(account)


# PROPOSAL
    elif intent == "proposal":

        return generate_proposal(account)


# CONTACTS
    elif intent == "contacts":

        data = get_contacts(sf, account)

        return summarize_contacts(data)


# RECENT OPPORTUNITIES
    elif intent == "recent-opps":

        data = get_opportunity(sf, account)

        return "\n".join([
            f"{o['Name']} | {o['StageName']} | ${o['Amount']} | Close: {o['CloseDate']}"
            for o in data[:3]
        ])


# DASHBOARD
    elif intent == "dashboard":

        data = get_pipeline(sf)

        total = len(data)

        value = sum([o["Amount"] or 0 for o in data])

        return f"""
Sales Dashboard

Total Deals: {total}
Total Pipeline Value: ${value}

Top Opportunities:
""" + "\n".join([f"{o['Name']} - ${o['Amount']}" for o in data[:3]])


# RISK ANALYSIS
    elif intent == "risk":

        data = get_opportunity(sf, account)

        return predict_risk(data)


# MEETING PREP
    elif intent == "meeting-prep":

        data = get_opportunity(sf, account)

        return prepare_meeting(account, data)


# FORECAST
    elif intent == "forecast":

        data = get_pipeline(sf)

        return sales_forecast(data)


# CREATE OPPORTUNITY
    elif intent == "create-opportunity":

        parts = message.split()

        amount = parts[-2]

        name = parts[-1]

        return create_opportunity(sf, account, amount, name)


# COMPARE
    elif intent == "compare":

        parts = message.split("and")

        acc1 = parts[0].replace("compare", "").strip()

        acc2 = parts[1].strip()

        data = compare_accounts(sf, acc1, acc2)

        return str(data)

    # PRODUCTS SEARCH
    elif intent == "products":

        data = get_products(sf)

        return "\n".join([
            f"{p['Name']} | Code: {p['ProductCode']} | Category: {p['Family']}"
            for p in data
        ])

    elif intent == "send-email":

        contacts = get_contacts(sf, account)

        if not contacts:
            return "No contacts found for this account."

        contact_name = extract_contact_name(message)

        selected_contact = None

        if contact_name:
            for c in contacts:
                if contact_name.lower() in c["Name"].lower():
                    selected_contact = c
                    break
        else:
            selected_contact = contacts[0]

        if not selected_contact.get("Email"):
            return f"No email found for {selected_contact['Name']}."

        email_body = generate_email(account, selected_contact["Name"])

        success = send_sales_email(
            selected_contact["Email"],
            f"Follow-up regarding {account}",
            email_body
        )

        if success:
            return f"✅ Email sent to {selected_contact['Name']} ({selected_contact['Email']})"
        else:
            return "❌ Email sending failed."

        
    elif intent == "last-deal":

        data = get_opportunity(sf, account)

        if not data:
            return "No deals found."

        deal = data[0]

        return f"""
    Latest Deal

    Opportunity: {deal['Name']}
    Stage: {deal['StageName']}
    Amount: ${deal['Amount']}
    Close Date: {deal['CloseDate']}
    """


    # QUOTE GENERATION
    elif intent == "generate-quote":
        opps = get_opportunity(sf, account)
        if not opps: return "No opportunity found to quote."
        
        # In a real app, you'd find the specific Opp ID
        quote = create_quote(sf, opps[0]['Id'], f"Quote for {account}")
        return f"📄 Quote created successfully in Salesforce for {account}."
    elif intent == "purchased-products":

        data = get_opportunity(sf, account)

        if not data:
            return "No opportunities found for this account."

        opp_name = data[0]["Name"]

        products = get_opportunity_products(sf, opp_name)

        return summarize_products(products)

    else:

        return """
You can ask things like:

Tell me about ABC Corp
What opportunities exist for ABC Corp
Draft email for ABC Corp
Create proposal for ABC Corp
Show dashboard
Forecast sales
Prepare meeting for ABC Corp
Compare ABC Corp and XYZ Inc
"""
