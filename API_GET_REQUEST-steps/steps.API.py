from behave import given, when, then
import requests

global_general_variables = {}

@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint
url = "https://api.coinbase.com/v2/currencies"
response = requests.get(url)
assert response.status_code == 200
print(response)

@given(u'Set GET API endpoint with changed EUR Param "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint
url = "https://api.coinbase.com/v2/exchange-rates"
r = requests.get(url, params={'currency' : 'EUR'})
print(r.status_code)
print(r.text)
assert response.status_code == 200
