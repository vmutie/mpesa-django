# ==============================
# FILE: stk_push
# PURPOSE: Send Lipa Na M-Pesa (STK Push) Payment Requests
# ==============================

import requests
import base64
from datetime import datetime
import keys  # Holds your credentials (business_shortcode, passkey, etc.)
from access_token import generate_access_token  # Import from file 1

def lipa_na_mpesa():
    """
    Initiates an STK Push request to simulate a customer payment.
    """

    # ==============================
    # STEP 1: Generate timestamp
    # ==============================
    # Format must be YYYYMMDDHHMMSS (e.g., 20251017215811)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # ==============================
    # STEP 2: Create Base64 encoded password
    # ==============================
    # Password = Base64Encode(BusinessShortCode + Passkey + Timestamp)
    data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + timestamp
    encoded_password = base64.b64encode(data_to_encode.encode()).decode("utf-8")

    # ==============================
    # STEP 3: Get access token
    # ==============================
    access_token = generate_access_token()

    # ==============================
    # STEP 4: Prepare request details
    # ==============================
    stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}

    request_data = {
        "BusinessShortCode": keys.business_shortcode,     # Your Paybill or Till number
        "Password": encoded_password,                     # Base64 encoded password
        "Timestamp": timestamp,                           # Same timestamp used above
        "TransactionType": "CustomerPayBillOnline",        # Always this for Paybill
        "Amount": "1",                                    # Amount (KES)
        "PartyA": keys.phone_number,                      # Customer phone number (e.g., 2547...)
        "PartyB": keys.business_shortcode,                # Your shortcode
        "PhoneNumber": keys.phone_number,                 # Same as PartyA
        "CallBackURL": "https://favoredly-sorriest-vida.ngrok-free.dev/api/payments/lnm/",
        "AccountReference": "TestAccount",
        "TransactionDesc": "Test Payment via STK Push",
    }

    # ==============================
    # STEP 5: Send STK Push request
    # ==============================
    response = requests.post(stk_url, json=request_data, headers=headers)

    # Print and return Safaricom API response
    print("📡 STK Push Response:")
    print(response.text)


# Uncomment below to test STK Push directly
lipa_na_mpesa()
