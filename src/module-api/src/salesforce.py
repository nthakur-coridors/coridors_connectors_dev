# import requests
from simple_salesforce import Salesforce

def salesforce_login():
    user_name = "nthakur.coridors@gmail.com"
    password = "sf@Code.123"
    security_token = "7WdiFAYTLe5HcmDX4NgkJZV6"
    version = "58.0"
    domain = 'login'
    sf_session = Salesforce(user_name, password, security_token, domain, version)
    print(sf_session.base_url.split('/')[2])
    return sf_session.base_url.split('/')[2]