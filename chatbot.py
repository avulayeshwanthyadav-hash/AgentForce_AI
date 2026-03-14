from salesforce_api import connect_salesforce, get_account, get_opportunity
from ai_tools import summarize_account, analyze_opportunity, generate_email, generate_proposal


sf = connect_salesforce()


def chatbot(user_input):

    user_input = user_input.lower()

    if "summary" in user_input:

        account = "ABC Corp"

        data = get_account(sf, account)

        return summarize_account(data)


    elif "opportunity" in user_input:

        account = "ABC Corp"

        data = get_opportunity(sf, account)

        return analyze_opportunity(data)


    elif "email" in user_input:

        return generate_email("ABC Corp")


    elif "proposal" in user_input:

        return generate_proposal("ABC Corp")


    else:

        return "I can help with account summary, opportunity analysis, email or proposal."