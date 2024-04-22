from flask import Flask, request, jsonify
import requests

# lỗi là ae chưa thêm cookie nhe

app = Flask(__name__)

@app.route('/', methods=['GET'])
def check():
    username = request.args.get('username') 
    if username:
        url = "https://www.threads.net/api/graphql"
        payload = {
            "av": "17841453625747943",
            "__user": "0",
            "__a": "1",
            "__req": "i",
            "__hs": "19834.HYP:barcelona_web_pkg.2.1..0.1",
            "dpr": "2",
            "__ccg": "UNKNOWN",
            "__rev": "1012939231",
            "__s": "gjl2na:22ttvu:e3jfx7",
            "__hsi": "7360391824589661123",
            "__dyn": "7xeUmwlEnwn8K2Wmh0cm5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2swwwNwKwHw8Xxm16wa-7U1bobodEGdwtU2ewbS1LwTwKG0hq1Iwqo9EpwUwiUfEowLwHxW17y9Ukw",
            "__csr": "gB6jNvuPYcmysBiWKV7TWAEi9HDg8QSK9K00qr6a40Nxm5EgU7uOPe2AsyemzIMI92E3GDw58gm6Bmshga8Vw8t06EomwYP2A7Q2-05-yJ7k8G2l0Eyzw5h8",
            "__comet_req": "29",
            "fb_dtsg": "NAcMy9FzXjhL6Ng1jN-2dLnPcqjxWF5tulAGO36uhgjYpExCXqkk2SQ:17864863018060157:1713724442",
            "jazoest": "26335",
            "lsd": "2CWc722Z7EYc8fBzSu0sw-",
            "__spin_r": "1012939231",
            "__spin_b": "trunk",
            "__spin_t": "1713724766",
            "__jssesw": "1",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "BarcelonaUsernameHoverCardImplQuery",
            "variables": "{\"username\":\"" + username + "\",\"__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider\":false}",
            "server_timestamps": "true",
            "doc_id": "7686674168061744"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "COOKIE",
            "Origin": "https://www.threads.net",
            "Referer": "https://www.threads.net/",
        }

        response = requests.post(url, headers=headers, data=payload)

        return jsonify(response.json())
    else:
        return jsonify({"error": "Vui lòng nhập tên người dùng."})

if __name__ == '__main__':
    app.run(debug=True)
