import requests

VAULT_ADDR = "http://127.0.0.1:8200"
VAULT_TOKEN = "myroot"
SECRET_PATH = "secret/data/myapp"

headers = {
    "X-Vault-Token": VAULT_TOKEN
}

response = requests.get(f"{VAULT_ADDR}/v1/{SECRET_PATH}", headers=headers)

if response.status_code == 200:
    secret = response.json()["data"]["data"]["apikey"]
    print(f"Fetched secret: {secret}")
else:
    print("Error fetching secret:", response.text)

