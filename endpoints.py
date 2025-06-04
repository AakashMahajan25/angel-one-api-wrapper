ROOT_API_ENDPOINT = "https://apiconnect.angelone.in"

# User APIs
AUTHENTICATE = ROOT_API_ENDPOINT + "/rest/auth/angelbroking/user/v1/loginByPassword"
GENERATE_TOKEN = ROOT_API_ENDPOINT + "/rest/auth/angelbroking/jwt/v1/generateTokens"
GET_PROFILE = ROOT_API_ENDPOINT + "/rest/secure/angelbroking/user/v1/getProfile"

# Order APIs
PLACE_ORDER = ROOT_API_ENDPOINT + "/rest/secure/angelbroking/order/v1/placeOrder"
CANCEL_ORDER = ROOT_API_ENDPOINT + "/rest/secure/angelbroking/order/v1/cancelOrder"
GET_ORDER_BOOK = ROOT_API_ENDPOINT + "/rest/secure/angelbroking/order/v1/getOrderBook"
GET_TRADE_BOOK = ROOT_API_ENDPOINT + "/rest/secure/angelbroking/order/v1/getTradeBook"
