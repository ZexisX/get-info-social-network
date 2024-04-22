from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
# lỗi là ae chưa thêm cookie và access_token nhe

@app.route('/', methods=['GET'])
def check():
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Vui lòng cung cấp một username"}), 400

    url = f"https://twitter.com/i/api/graphql/qW5u-DAuXpMEG0zA1F7UGQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Atrue%2C%22hidden_profile_subscriptions_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_is_identity_verified_enabled%22%3Atrue%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22responsive_web_twitter_article_notes_tab_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D&fieldToggles=%7B%22withAuxiliaryUserLabels%22%3Afalse%7D"

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8,en-GB;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'Authorization': 'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'Cookie': 'COOKIE',
        'Priority': 'u=1, i',
        'Referer': 'https://twitter.com/elonmusk',
        'Sec-Ch-Ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'X-Client-Transaction-Id': 'Re3wYQJU6m/xMApmHu2a6UJw0XrjV+G1XwaCA/c11S/X12AfhZyG04/JIikJfEBgDJ5XkkRbmv7lyFElOhBMnVFo3hGPRg',
        'X-Csrf-Token': '',
        'X-Twitter-Active-User': 'yes',
        'X-Twitter-Auth-Type': 'OAuth2Session',
        'X-Twitter-Client-Language': 'en'
    }

    # Tiến hành yêu cầu
    response = requests.get(url, headers=headers)

    # Trả về dữ liệu từ yêu cầu dưới dạng JSON
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
