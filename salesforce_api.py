from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

load_dotenv()

def connect_salesforce():

    sf = Salesforce(
        username=os.getenv("SF_USERNAME"),
        password=os.getenv("SF_PASSWORD"),
        security_token=os.getenv("SF_TOKEN")
    )

    return sf


def get_account(sf, name):

    query = f"""
    SELECT Name, Industry, Description
    FROM Account
    WHERE Name = '{name}'
    """

    result = sf.query(query)

    return result['records']


def get_opportunity(sf, name):

    query = f"""
    SELECT Name, StageName, Amount
    FROM Opportunity
    WHERE Account.Name='{name}'
    """

    result = sf.query(query)

    return result['records']