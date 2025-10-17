# ==============================
# FILE: access_token.py
# PURPOSE: Generate M-Pesa API Access Token
# ==============================

import requests
from requests.auth import HTTPBasicAuth
import keys  # This should contain your consumer_key and consumer_secret

def generate_access_token():
    """
    Generate OAuth access token required by Safaricom APIs.
    Tokens expire after ~1 hour.
    """

    # Endpoint for requesting the access token (Sandbox)
    token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    # Your credentials from the Safaricom Developer Portal
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret

    # Send GET request with HTTP Basic Auth using consumer key & secret
    response = requests.get(token_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # Convert response to JSON (Safaricom returns { "access_token": "...", "expires_in": "3599" })
    json_response = response.json()

    # Extract token from JSON
    access_token = json_response.get("access_token")

    print("✅ Access Token Generated Successfully:")
    print(access_token)

    return access_token


# Uncomment below line to test this file directly
# generate_access_token()
