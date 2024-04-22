from flask import Flask, request, jsonify
import requests
# lỗi là ae chưa thêm cookie nhe
app = Flask(__name__)

def get_uid(username):
    url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
    headers = {'X-IG-App-ID': '936619743392459'}

    response = requests.get(url, headers=headers)
    data = response.json()

    if 'user' in data['data']:
        user_id = data['data']['user']['id']
        return user_id
    else:
        return None

def get_info(user_id):
    graphql_url = "https://www.instagram.com/api/graphql"
    profile_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "COOKIE"
    }
    payload = {
        "av": user_id,
        "__d": "www",
        "__user": "0",
        "__a": "1",
        "__req": "1",
        "__hs": "19834.HYP:instagram_web_pkg.2.1..0.1",
        "dpr": "2",
        "__ccg": "UNKNOWN",
        "__rev": "1012939231",
        "__s": "8cwelx:j0yapf:wy5yef",
        "__hsi": "7360394715559736033",
        "__dyn": "7xeUjG1mxu1syUbFp40NonwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEd86a3a1YwBgao6C0Mo2swaOfK0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azo7u1xwIw8O321LwTwKG1pg2Xwr86C1mwrd6goK68jDyUrAwHyokxK3Oq",
        "__csr": "n1b6jPihsICykBsAqII8OSOkBQHXEyr5nCiqzLWKAvLKeHuiiqHAhkFHGj8iqBxmjQnhaCgWiC6oyuiiAQaV8igB4aHKuJ2e5ahA8yXybxucKECq8RUXChpoHzazQeGiXBKmaypbCByoO39005j-e7U1_8K3G1UCy89AEhxa0f2DhE08345EC8yfc2x0kcHDgGywywGwopo2ig3mx62l0EzC0py1pw2cU4R0ygb8l80p7zpVQaw3n43W1lw0qqS06DE0Yi",
        "__comet_req": "7",
        "fb_dtsg": "NAcO3ucj8q6NENFfSlY3iUOcvyrdpamsGi5OJ5OY4W6C3bPBLREXm5A:17843696212148243:1711204821",
        "jazoest": "26109",
        "lsd": "vZdyiA3EZjzPimyUmR8FN7",
        "__spin_r": "1012939231",
        "__spin_b": "trunk",
        "__spin_t": "1713725439",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "PolarisProfilePageContentQuery",
        "variables": "{\"id\":\"" + user_id + "\",\"relay_header\":false,\"render_surface\":\"PROFILE\"}",
        "server_timestamps": "true",
        "doc_id": "8257302777620075",
    }
    graphql_response = requests.post(graphql_url, headers=profile_headers, data=payload)

    graphql_data = graphql_response.json()
    user_details = graphql_data.get("data", {}).get("user", {})
    
    return user_details

@app.route('/', methods=['GET'])
def check():
    username = request.args.get('username')
    user_id = get_uid(username)
    
    if user_id:
        user_details = get_info(user_id)
        return jsonify({"user_id": user_id, "user_details": user_details})
    else:
        return jsonify({"error": "User ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)