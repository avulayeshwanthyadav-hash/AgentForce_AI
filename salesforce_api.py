import os
import requests
from simple_salesforce import Salesforce
from dotenv import load_dotenv

load_dotenv()


def connect_salesforce():
    """
    Connect to Salesforce via OAuth2 Password Grant
    """
    url = "https://login.salesforce.com/services/oauth2/token"

    data = {
        "grant_type": "password",
        "client_id": os.getenv("SF_CONSUMER_KEY"),
        "client_secret": os.getenv("SF_CONSUMER_SECRET"),
        "username": os.getenv("SF_USERNAME"),
        "password": os.getenv("SF_PASSWORD") + os.getenv("SF_TOKEN")
    }

    response = requests.post(url, data=data)
    auth = response.json()

    if "access_token" not in auth:
        raise Exception(f"OAuth failed: {auth}")

    sf = Salesforce(
        instance_url=auth["instance_url"],
        session_id=auth["access_token"]
    )

    return sf


def get_account(sf, name):
    """
    Fetch Account data with extra fields
    """
    query = f"""
    SELECT Name, Industry, Description, Phone, Website
    FROM Account
    WHERE Name = '{name}'
    """
    result = sf.query(query)
    return result['records']


def get_opportunity(sf, name):
    """
    Fetch top 5 recent Opportunities for the account
    """
    query = f"""
    SELECT Name, StageName, Amount, CloseDate, Probability
    FROM Opportunity
    WHERE Account.Name='{name}'
    ORDER BY CloseDate DESC
    LIMIT 5
    """
    result = sf.query(query)
    return result['records']


def get_contacts(sf, name):
    """
    Fetch contacts related to an account
    """
    query = f"""
    SELECT Name, Email, Phone, Title
    FROM Contact
    WHERE Account.Name='{name}'
    """
    result = sf.query(query)
    return result['records']

def get_pipeline(sf):

    query = """
    SELECT Name, StageName, Amount
    FROM Opportunity
    """

    result = sf.query(query)

    return result["records"]


def create_opportunity(sf, account_name, amount, name):

    account_query = f"""
    SELECT Id FROM Account WHERE Name='{account_name}'
    """

    acc = sf.query(account_query)

    if not acc["records"]:
        return "Account not found"

    account_id = acc["records"][0]["Id"]

    sf.Opportunity.create({
        "Name": name,
        "StageName": "Prospecting",
        "CloseDate": "2026-06-01",
        "Amount": amount,
        "AccountId": account_id
    })

    return "Opportunity created successfully"


def compare_accounts(sf, acc1, acc2):

    query = f"""
    SELECT Name, Industry
    FROM Account
    WHERE Name IN ('{acc1}','{acc2}')
    """

    return sf.query(query)["records"]

def get_opportunity_products(sf, opp_name):
    """
    Fetch what products are attached to a specific opportunity
    """
    query = f"""
    SELECT Opportunity.Name, Product2.Name, Quantity, UnitPrice, TotalPrice
    FROM OpportunityLineItem
    WHERE Opportunity.Name = '{opp_name}'
    """
    result = sf.query(query)
    return result['records']

def get_products(sf):

    query = """
    SELECT Name, ProductCode, Family
    FROM Product2
    ORDER BY CreatedDate DESC
    LIMIT 5
    """

    result = sf.query(query)

    return result["records"]

def get_orders(sf, account_name):
    """
    Fetch purchasing history/orders for an account
    """
    query = f"""
    SELECT OrderNumber, TotalAmount, Status, EffectiveDate
    FROM Order
    WHERE Account.Name = '{account_name}'
    """
    result = sf.query(query)
    return result['records']

def create_quote(sf, opp_id, quote_name):
    """
    Generate a formal Quote record in Salesforce
    """
    quote_data = {
        "OpportunityId": opp_id,
        "Name": quote_name
    }
    return sf.Quote.create(quote_data)
