import requests
from pprint import pprint

def verify_network_access_and_token():
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
    url = 'http://jsgalan.pythonanywhere.com/chain'
    response = requests.get(url)

    if response.status_code == 200:
        chain_state = response.json()
        pprint(chain_state)
    else:
        print(f"Failed to get chain state. Status code: {response.status_code}")

def upload_message(sender, recipient, chat):
    url = 'http://jsgalan.pythonanywhere.com/transactions/new'
    data = {'sender': sender, 'recipient': recipient, 'chat': chat}
    response = requests.post(url, json=data)

    if response.status_code == 201:
        print("Message uploaded successfully.")
    else:
        print(f"Failed to upload message. Status code: {response.status_code}")

def mine_block(group_name, name):
    url = 'http://jsgalan.pythonanywhere.com/mine'
    data = {'groupname': group_name, 'name': name}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Block mined successfully.")
    else:
        print(f"Failed to mine block. Status code: {response.status_code}")

if __name__ == '__main__':
    # Section a
    # Verify network access and token validity
    verify_network_access_and_token()

    # Section b
    # Verify blockchain state
    get_chain_state()

    # Section c
    # Upload messages
    #upload_message('Fidel Diaz', 'Jovito Guevara', 'I am mining bitcoins in blockchain!')
    upload_message('Fidel Diaz', 'Jovito Guevara', 'Hello computers!')
    #upload_message('Fidel Diaz', 'Jovito Guevara', 'Lets do it again!')

    # Section d
    # Mine the block
    mine_block('1SF125', 'Fidel Diaz')