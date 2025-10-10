from flask import Flask, request, redirect, jsonify
import uuid
import requests

app = Flask(__name__)

# In-memory stores
auth_codes = {}
access_tokens = {}


@app.route("/introspect", methods=["POST"])
def introspect():
    token = request.form.get("token")
    token_data = access_tokens.get(token)

    if not token_data:
        return jsonify({"active": False})

    return jsonify({
        "active": True,
        "scope": "read",
        "username": token_data["user"],
        "client_id": "abc",
        "token_type": "access_token",
        "exp": 9999999999,
        "sub": "user123"
    })


@app.route("/authorize")
def authorize():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")
    code_challenge = request.args.get("code_challenge")

    # Simulate login and consent
    code = str(uuid.uuid4())
    auth_codes[code] = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_challenge": code_challenge
    }

    return redirect(f"{redirect_uri}?code={code}&state={state}")

@app.route("/token", methods=["POST"])
def token():
    code = request.form.get("code")
    code_verifier = request.form.get("code_verifier")

    if code not in auth_codes:
        return jsonify({"error": "invalid_code"}), 400

    # Simplified PKCE check
    if auth_codes[code]["code_challenge"] != code_verifier:
        return jsonify({"error": "invalid_code_verifier"}), 400

    access_token = str(uuid.uuid4())
    access_tokens[access_token] = {"user": "chris"}

    return jsonify({
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 3600
    })

@app.route("/logout")
def logout():
    return "Logged out (simulated)", 200

if __name__ == "__main__":
    PORT = 5000
    print(f"Auth server started and running on {PORT}")
    app.run(port=PORT)
