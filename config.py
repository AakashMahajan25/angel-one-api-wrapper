from dotenv import load_dotenv
import os
import uuid
import socket
import requests

load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
JWT_TOKEN = os.environ.get("JWT_TOKEN")




def get_local_ip():
    """Get local IP address"""
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_public_ip():
    """Get public IP address using external service"""
    try:
        return requests.get("https://api64.ipify.org?format=json").json()["ip"]
    except Exception:
        return None

def get_mac_address():
    """Get system MAC address"""
    mac = uuid.getnode()
    return ':'.join(['{:02x}'.format((mac >> i) & 0xff) for i in range(40, -1, -8)])

def get_headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-ClientLocalIP": get_local_ip(),
        "X-ClientPublicIP": get_public_ip(),
        "X-MACAddress": get_mac_address(),
        "X-PrivateKey": API_KEY,
        "X-UserType": "USER",
        "X-SourceID": "WEB",
        "Authorization": f"Bearer {JWT_TOKEN}"
    }




# Payloads for POST APIs

LOGIN_PAYLOAD = {
    "clientcode":"Your_client_code",
    "password":"Your_pin",
    "totp":"enter_the_code_displayed_on_your_authenticator_app",
}

# Other modes available are OHLC and LTP
MARKET_DATA_PAYLOAD = { "mode": "FULL", "exchangeTokens": { "NSE": ["3045","881"], "NFO": ["58662"]} }


TOP_GAINERS_LOSERS_PAYLOAD = {
    "datatype":"PercOIGainers", # Type of Data you want(PercOILosers/PercOIGainers PercPriceGainers/PercPriceLosers)
    "expirytype":"NEAR" # Expiry Type (NEAR/NEXT/FAR)
}


HISTORICAL_DATA_PAYLOAD = {
     "exchange": "NSE",
     "symboltoken": "99926000",
     "interval": "ONE_HOUR",
     "fromdate": "2023-09-06 11:15",
     "todate": "2023-09-06 12:00"
}


