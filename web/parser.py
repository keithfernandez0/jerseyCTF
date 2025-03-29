import hashlib
import hmac
import requests
import json

# Set the URL for the verification endpoint
verify_url = "http://a-hash-too-far.aws.jerseyctf.com:5000/verify"

# Define the secret key (32-byte string, for example)
secret_key = b"32-byte-secret-key-here-12345678"

# Define the required message
message = "meet at the following coordinates:23,28'57\"S 124,34'34\"W"

# Encode the message in Latin-1 encoding
message_encoded = message.encode('latin-1')

# Calculate the HMAC-SHA256 signature using the secret key and message
signature = hmac.new(secret_key, message_encoded, hashlib.sha256).hexdigest()

# Create the JSON payload
data = {
    'message': message,
    'signature': signature
}

# Send the data to the verification endpoint with the correct Content-Type
headers = {'Content-Type': 'application/json'}
response = requests.post(verify_url, data=json.dumps(data), headers=headers)

# Print the response from the server
print("Response:", response.text)
