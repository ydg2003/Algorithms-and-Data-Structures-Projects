# FINAL EXAM
# Fidel Diaz | 3-751-509 | 1SF125 | fidel.diaz@utp.ac.pa
import requests
from pprint import pprint

def verify_network_access_and_token():
    # Algorithm 1: verify_network_access_and_token
    # Verifies network access and token validity.
    # Input: None
    # Output: Prints messages indicating network access verification and token validity.    
    token = '89600f38d62242540816d5dd1a7a043597e23187'
    url = 'http://jsgalan.pythonanywhere.com/chain'

    # Verify network access
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Network access verified.")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the network: {e}")
        exit()

    # Verify token validity
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Token is valid.")
    else:
        print(f"Token is invalid. Status code: {response.status_code}")

def get_chain_state():
    # Algorithm 2: get_chain_state
    # Retrieves and prints the current state of the blockchain.
    # Input: None
    # Output: Prints the current state of the blockchain.
    url = 'http://jsgalan.pythonanywhere.com/chain'
    response = requests.get(url)

    if response.status_code == 200:
        chain_state = response.json()
        pprint(chain_state)
    else:
        print(f"Failed to get chain state. Status code: {response.status_code}")

def upload_message(sender, recipient, chat):
    # Algorithm 3: upload_message
    # Uploads a message to the blockchain
    # Input: sender (str), recipient (str), chat (str)
    # Output: Prints messages indicating successful or failed message upload.
    url = 'http://jsgalan.pythonanywhere.com/transactions/new'
    data = {'sender': sender, 'recipient': recipient, 'chat': chat}
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("Message uploaded successfully.")
    else:
        print(f"Failed to upload message. Status code: {response.status_code}")

def mine_block(group_name, name):
    # Algorithm 4: mine_block
    # Mines a new block in the blockchain
    # Input: group_name (str), name (str)
    # Output: Prints messages indicating successful or failed block mining.
    url = 'http://jsgalan.pythonanywhere.com/mine'
    data = {'groupname': group_name, 'name': name}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Block mined successfully.")
    else:
        print(f"Failed to mine block. Status code: {response.status_code}")

if __name__ == '__main__':
    # Algorithm 5: Main Execution
    # Executes the verification, retrieval, message upload, and block mining algorithms sequentially.
    # Input: None
    # Output: Executes the entire code, demonstrating interactions with the blockchain API.
    # Section a
    verify_network_access_and_token()
    # Section b
    get_chain_state()
    # Section c
    upload_message('Fidel Diaz', 'Jovito Guevara', 'These are my 4 messages for the blockchain.')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'Hello computers!')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'Lets do it again!')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'I am mining bitcoins in blockchain!')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'Hello computers!')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'Lets do it again!')
    # Section d
    mine_block('1SF125', 'Fidel Diaz')
# This code is contributed by ChatGPT 3.5