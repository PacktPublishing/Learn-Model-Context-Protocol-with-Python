import requests
from urllib.parse import urlparse, parse_qs

# Configuration
AUTH_SERVER = "http://localhost:5000"
RESOURCE_SERVER = "http://localhost:5001"
CLIENT_ID = "abc"
REDIRECT_URI = "http://localhost:3000/callback"
STATE = "xyz"
CODE_CHALLENGE = "123"
CODE_VERIFIER = "123"


# TODO, 1a. add existing token use case
# add code that says, if you have a valid token, then call /introspect
# 2a, if all is good there then continue
# 2b, token is not valid, continue with 1b 

# 1b, no existing token, we start our journey with /authorize

# Step 1: Simulate browser redirect to /authorize
authorize_url = f"{AUTH_SERVER}/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state={STATE}&code_challenge={CODE_CHALLENGE}&code_challenge_method=plain"
print(f"Requesting authorization: {authorize_url}")
response = requests.get(authorize_url, allow_redirects=False)

# Step 2: Extract authorization code from redirect
redirect_location = response.headers.get("Location")
if not redirect_location:
    print("Authorization server did not redirect. Is it running?")
    exit(1)

parsed_url = urlparse(redirect_location)
query_params = parse_qs(parsed_url.query)
auth_code = query_params.get("code", [None])[0]
print(f"Received authorization code: {auth_code}")

# Step 3: Exchange code for access token
token_response = requests.post(f"{AUTH_SERVER}/token", data={
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": REDIRECT_URI,
    "client_id": CLIENT_ID,
    "code_verifier": CODE_VERIFIER
})
token_data = token_response.json()
access_token = token_data.get("access_token")
print(f"Access token: {access_token}")

# Step 4: Call resource server
resource_response = requests.get(f"{RESOURCE_SERVER}/userinfo", headers={
    "Authorization": f"Bearer {access_token}"
})
print("User info response:")
print(resource_response.json())