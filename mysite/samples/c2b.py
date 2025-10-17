import requests
from requests.auth import HTTPBasicAuth
import keys
from access_token import generate_access_token
access_token = generate_access_token()

def register_c2b_url():
    


    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "ShortCode": keys.c2b_shortcode,
        "ResponseType": "Completed", 
        "ConfirmationURL": "https://favoredly-sorriest-vida.ngrok-free.dev/api/payments/confirmation/",
        "ValidationURL":   "https://favoredly-sorriest-vida.ngrok-free.dev/api/payments/validation/",
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
# register_c2b_url()

def simulate_c2b_transaction():
    my_access_token = access_token

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": keys.c2b_shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "myaccnumber",
    }

    response = requests.post(api_url, json=request, headers=headers)



    print(response.text)


simulate_c2b_transaction()