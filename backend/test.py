import requests

# Define the server URL
SERVER_URL = "http://localhost:5000"

def test_chat_endpoint():
    test_query = {"query": "What is the latest technology news?"}
    response = requests.post(f"{SERVER_URL}/chat", json=test_query)
    print("Chat Response:", response.json())

def test_retrieve_endpoint():
    test_query = {"query": "Artificial Intelligence"}
    response = requests.post(f"{SERVER_URL}/retrieve", json=test_query)
    print("Retrieve Response:", response.json())

if __name__ == "__main__":
    print("Testing /chat endpoint...")
    test_chat_endpoint()
    print("\nTesting /retrieve endpoint...")
    test_retrieve_endpoint()
