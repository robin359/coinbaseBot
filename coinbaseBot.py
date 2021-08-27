import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or b'').decode()
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode()

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.pro.coinbase.com/'
API_KEY = "12af0ed42d93ef00c6c996ed3b9b727c"
API_SECRET = "PWyyZpb4atig2+EmPaopHswPiRLyBe4GOLx5UTZ5ERD2q7IrnS/+TPwB8XkPFtjygIVaSTHEswa3FXfDoa+j6w=="
API_PASS = "tqwcvgf58j"
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET,  API_PASS)

r = requests.get(api_url + 'accounts', auth=auth)
print(r.json())

order = {
    'funds': 10.00,
    'order_type':'market',
    'side': 'buy',
    'product_id': 'BTC-EUR',
}
r = requests.post(api_url + 'orders', json=order, auth=auth)
print(r.json())
