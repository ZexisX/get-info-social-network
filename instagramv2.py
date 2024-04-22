from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_user_info():
    username = request.args.get('username')
    
    url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
    headers = {'X-IG-App-ID': '936619743392459'}

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'user' in data['data']:
        user_info = data['data']['user']
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
