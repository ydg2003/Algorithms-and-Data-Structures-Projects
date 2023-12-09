import requests
from flask import Flask, jsonify, request
from pprint import pprint

app = Flask(__name__)

# Replace these values with your actual username and token
username = 'jsgalan'
token = '89600f38d62242540816d5dd1a7a043597e23187'
base_url = 'http://jsgalan.pythonanywhere.com/'

def verify_network_access():
    url = f'{base_url}chain'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify({'message': 'Network access verified'}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error accessing the network: {e}'}), 500

def verify_token():
    url = f'{base_url}chain'  
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify({'message': 'Token is valid'}), 200
    else:
        return jsonify({'error': f'Token is invalid. Status code: {response.status_code}'}), 500

def get_chain_state():
    url = f'{base_url}chain'
    response = requests.get(url)
    if response.status_code == 200:
        chain_state = response.json()
        pprint(chain_state)
        return jsonify(chain_state), 200
    else:
        return jsonify({'error': f'Failed to get chain state. Status code: {response.status_code}'}), 500

def upload_message(sender, recipient, chat):
    url = f'{base_url}transactions/new'
    data = {'sender': sender, 'recipient': recipient, 'chat': chat}
    response = requests.post(url, json=data)

    if response.status_code == 201:
        return jsonify({'message': 'Message uploaded successfully'}), 201
    else:
        return jsonify({'error': f'Failed to upload message. Status code: {response.status_code}'}), 500

def mine_block(group_name, name):
    url = f'{base_url}mine'
    data = {'groupname': group_name, 'name': name}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return jsonify({'message': 'Block mined successfully'}), 200
    else:
        return jsonify({'error': f'Failed to mine block. Status code: {response.status_code}'}), 500

# Flask routes
@app.route('/verify_network_access', methods=['GET'])
def flask_verify_network_access():
    return verify_network_access()

@app.route('/verify_token', methods=['GET'])
def flask_verify_token():
    return verify_token()

@app.route('/get_chain_state', methods=['GET'])
def flask_get_chain_state():
    return get_chain_state()

@app.route('/upload_message', methods=['POST'])
def flask_upload_message():
    data = request.get_json()
    return upload_message(data['sender'], data['recipient'], data['chat'])

@app.route('/mine_block', methods=['POST'])
def flask_mine_block():
    data = request.get_json()
    return mine_block(data['groupname'], data['name'])

if __name__ == '__main__':
    app.run(debug=True, port=8888)