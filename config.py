from dotenv import load_dotenv
import os
import uuid
import socket
import requests
import pyotp
from endpoints import AUTHENTICATE

load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
CLIENT_ID = os.environ.get("CLIENT_ID")
PASSWORD = os.environ.get("PASSWORD")
MFA_TOKEN = os.environ.get("MFA_TOKEN")


TOTP = pyotp.TOTP(MFA_TOKEN).now()


LOGIN_PAYLOAD = {
    "clientcode": CLIENT_ID,
    "password": PASSWORD,
    "totp": TOTP,
}

PLACE_ORDER_PAYLOAD = {
    "variety": "NORMAL",
    "tradingsymbol": "IDEA",          
    "symboltoken": "121",                
    "transactiontype": "BUY",
    "exchange": "NSE",
    "ordertype": "MARKET",
    "producttype": "INTRADAY",
    "duration": "DAY",
    "price": "6",                    
    "quantity": "1"
}

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


def generate_token():
    try:
        payload = get_login_payload()
        data = requests.post(AUTHENTICATE, json=payload, headers=get_headers()).json()
        print(data['data']['jwtToken'])
        return data['data']['jwtToken']

    except Exception as e:
        print(f"Error Generating Token: {str(e)}")
        

def get_login_payload():
    return {
        "clientcode": CLIENT_ID,
        "password": PASSWORD,
        "totp": TOTP
    }


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
        "Authorization": f"Bearer {generate_token()}"
    }


generate_token()

