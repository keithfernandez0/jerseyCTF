import hashlib
import hmac
import requests
import json

# Challenge and verification URLs
challenge_url = "http://a-hash-too-far.aws.jerseyctf.com:5000/challenge"
verify_url = "http://a-hash-too-far.aws.jerseyctf.com:5000/verify"

# Original Query
query = "SELECT * FROM meetings WHERE appearance='public'"

# Altered Query (Attempting to Access Private Data)
altered_query = "SELECT * FROM meetings"

# Unknown Secret Key (Replace with actual value if known)
secret_key = b"your-actual-32-byte-secret-key"

# Compute HMAC-SHA256 hashes
query_encoded = query.encode('latin-1')
altered_query_encoded = altered_query.encode('latin-1')

original_hash = hmac.new(secret_key, query_encoded, hashlib.sha256).hexdigest()
altered_hash = hmac.new(secret_key, altered_query_encoded, hashlib.sha256).hexdigest()

print(f"Original Query Hash: {original_hash}")
print(f"Altered Query Hash: {altered_hash}")

# Send the request (Trying different formats)
data = {
    "query": altered_query,
    "original_query": query,  # Keeping original query in case it's needed
    "32_byte_secret_plus_query_hash": altered_hash
}

headers = {"Content-Type": "application/json"}
response = requests.post(verify_url, data=json.dumps(data), headers=headers)

print("Response:", response.text)
