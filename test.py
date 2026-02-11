import requests
import os
import time

base_url = 'http://localhost:5000'

print("=== Thorough Testing for DEVS System ===")
print("Checking if database exists:", os.path.exists('devs.db'))

# Test identity
print("\n--- Identity Tests ---")
response = requests.post(f'{base_url}/api/identity', json={"id": "test", "name": "Test User"})
print("POST /api/identity (valid):", response.status_code, response.json() if response.status_code == 201 else response.text)

response = requests.post(f'{base_url}/api/identity', json={"id": "test", "name": "Test User"})  # Duplicate
print("POST /api/identity (duplicate):", response.status_code, response.text)

response = requests.post(f'{base_url}/api/identity', json={})  # Invalid
print("POST /api/identity (invalid):", response.status_code, response.text)

response = requests.get(f'{base_url}/api/identity/test')
print("GET /api/identity/test (existing):", response.status_code, response.json() if response.status_code == 200 else response.text)

response = requests.get(f'{base_url}/api/identity/nonexistent')
print("GET /api/identity/nonexistent:", response.status_code, response.text)

# Test experience
print("\n--- Experience Tests ---")
response = requests.post(f'{base_url}/api/experience', json={"title": "Test Exp", "description": "desc", "user_id": "test"})
print("POST /api/experience (with desc):", response.status_code, response.json() if response.status_code == 201 else response.text)

response = requests.post(f'{base_url}/api/experience', json={"title": "AI Exp", "user_id": "test"})  # AI generate
print("POST /api/experience (AI generate):", response.status_code, response.json() if response.status_code == 201 else response.text)

response = requests.post(f'{base_url}/api/experience', json={"title": "", "user_id": "test"})  # Invalid
print("POST /api/experience (invalid):", response.status_code, response.text)

response = requests.get(f'{base_url}/api/experience/1')
print("GET /api/experience/1 (existing):", response.status_code, response.json() if response.status_code == 200 else response.text)

response = requests.get(f'{base_url}/api/experience/999')
print("GET /api/experience/999 (nonexistent):", response.status_code, response.text)

# Test ledger
print("\n--- Ledger Tests ---")
response = requests.get(f'{base_url}/api/ledger')
print("GET /api/ledger (initial):", response.status_code, response.json() if response.status_code == 200 else response.text)

start_time = time.time()
response = requests.post(f'{base_url}/api/ledger/block', json={"data": "test block"})
end_time = time.time()
print("POST /api/ledger/block (mining time: {:.2f}s):".format(end_time - start_time), response.status_code, response.json() if response.status_code == 201 else response.text)

response = requests.get(f'{base_url}/api/ledger')
print("GET /api/ledger (after add):", response.status_code, response.json() if response.status_code == 200 else response.text)

response = requests.post(f'{base_url}/api/ledger/block', json={})  # Invalid
print("POST /api/ledger/block (invalid):", response.status_code, response.text)

# Persistence test (check if data persists)
print("\n--- Persistence Test ---")
response = requests.get(f'{base_url}/api/identity/test')
print("Persistence check - GET /api/identity/test:", response.status_code, response.json() if response.status_code == 200 else response.text)

print("\nThorough testing completed.")
