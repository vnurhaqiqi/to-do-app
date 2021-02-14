import jwt, random, string

def random_word(length):
    random_key = string.ascii_lowercase
    
    return ''.join(random.choice(random_key) for i in range(length))

# ====== Version ======
API_VERSION = '1'
APP_VERSION = '1'
MAINTENANCE = False

# ====== Path ======
BASE_URL = '/api/v' + API_VERSION + '/'

# ====== Status =====
STATUS_CODE = {
    200: "OK", 201: "Created", 202: "Accepted", 301: "Moved Permanently", 304: "Not Modified",
    307: "Temporary Redirect", 400: "Bad Request", 401: "Unauthorized", 403: "Forbidden", 404: "Not Found",
    405: "Method Not Acceptable", 406: "Unacceptable", 413: "Payload too large", 415: "Unsupported Media Type",
    429: "Too Many Requests", 500: "Internal Server Error", 501: "Not Implemented", 503: "Service Unavailable"
}

# ====== Pagination ======
PAGE_DATA_LIMIT = 10
DEFAULT_PAGE = 1

JWT_KEY = random_word(16)

def encode_token(payload):
    return jwt.encode(payload, JWT_KEY, algorithm='HS256')

def decode_token(payload):
    if payload:
        try:
            return jwt.decode(payload, JWT_KEY, algorithm='HS256')
        except Exception as e:
            return False
    else:
        return False