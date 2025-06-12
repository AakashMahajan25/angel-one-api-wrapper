from wrapper import AngelAPIWrapper
from config import CLIENT_ID, PASSWORD, TOTP
import asyncio


# Payloads for POST APIs

LOGIN_PAYLOAD = {
    "clientcode": CLIENT_ID,
    "password": PASSWORD,
    "totp": TOTP,
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


async def main():
    # Create an instance of the wrapper
    api = AngelAPIWrapper()
    
    try:
        # Call the get_profile method
        profile = await api.get_historical_data()
        print("Profile:", profile)
    except Exception as e:
        print(f"Error occurred: {e}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())