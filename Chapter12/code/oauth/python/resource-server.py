from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Simulated token store (shared with auth server in real world)
valid_tokens = {}
AUTH_SERVER = "http://localhost:5000"

@app.route("/userinfo")
def userinfo():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "missing_token"}), 401

    token = auth_header.split(" ")[1]
    print("valid tokens:", valid_tokens)

    # check validity of token with /introspect
    token_response = requests.post(f"{AUTH_SERVER}/introspect", data={
      "token": token
    })

    token_data = token_response.json()
    is_active = token_data.get("active", False)

    if not is_active:
        return jsonify({"error": "invalid_token"}), 403

    return jsonify({
        "sub": "user123",
        "name": "Chris",
        "email": "chris@example.com"
    })

if __name__ == "__main__":
    PORT = 5001
    print(f"Resource server started on {PORT}")
    app.run(port=PORT)
    # Simulate shared token store
    from auth_server import access_tokens
    valid_tokens.update(access_tokens)
